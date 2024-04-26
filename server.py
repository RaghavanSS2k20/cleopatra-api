from flask import Flask, request
from  dotenv import load_dotenv
import json
import os
import google.generativeai as genai
from scriptutils import getCharectersForBeat
from promptprefixes import gettitlepromptprefix, getTitleForScifi,getCharecterDescriptions, getPlotOutline, getLocationDescritptionPrompt, getDialogues
load_dotenv()
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key = GOOGLE_API_KEY, transport='rest')
with open('safety_config.json', 'r') as json_file:
    config = json.load(json_file)
print("config here is : ", config)
model = genai.GenerativeModel('gemini-pro', safety_settings=config)
app = Flask(__name__)

@app.route('/')
def ping():
    return {"Message":"working"}, 200


@app.route('/script/<logline>',)
def get_script(logline):
    l = []
    try:
        # data = request.json
        # logline = data.get("logline")
        # print(logline)
        prompt = getCharecterDescriptions(logline)
        response = model.generate_content(prompt)
        print(response)
        chunks = response.text.split("< stop >")

        characters = {}
        for chunk in chunks:
            if "< character >" in chunk and "< description >" in chunk:
                # Extracting character name and description
                char_start = chunk.find("< character >") + len("< character >")
                char_end = chunk.find("< description >")
                char_name = chunk[char_start:char_end].strip()

                desc_start = char_end + len("< description >")
                char_description = chunk[desc_start:].strip()

                # Adding to dictionary
                characters[char_name] = char_description
                
        

        print(characters)
        plotOutLine = getPlotOutline(logline, characters=characters)
        resp = model.generate_content(plotOutLine)
        sceneOutlineText = resp.text
        sceneOutlineText = sceneOutlineText.replace("< scenes >", "")
        scenes_str = sceneOutlineText.split("< scene >\n")[1:]
        scenes = []
        for scene_str in scenes_str:
            scene_info = scene_str.split("\n")
            scene_info = [s for s in scene_info if s != '' ]
        
            place = scene_info[0].split(":")[1].strip()
            plot_element = scene_info[1].split(" : ")[1].strip()
            print(scene_info)
            beat = scene_info[2].split(":")[1].strip()
            scenes.append({"place": place, "plot_element": plot_element, "beat": beat})
        placesDescription = {}
        for scene in scenes:
            place = scene["place"]
            prompt = getLocationDescritptionPrompt(logline=logline, place=place)
            r = model.generate_content(prompt)
            print(place)
            
            placesDescription[place]=r.text

        # s = scenes[0]
        # place = s['place']
        # pr = getLocationDescritptionPrompt(logline=logline, place=place)
        # r = model.generate_content(pr)
        # print(r.text)

        # scenes = [
        #     {
        #         "beat": "A gang of masked criminals rob a mafia-owned bank in Gotham City, betraying and killing each other until the sole survivor, the Joker, reveals himself as the mastermind and escapes with the money.",
        #         "place": "Gotham City Bank",
        #         "plot_element": "Exposition"
        #     },
        #     {
        #         "beat": "Batman, district attorney Harvey Dent, and police lieutenant Jim Gordon ally to eliminate Gotham's organized crime.",
        #         "place": "Batcave",
        #         "plot_element": "Inciting Incident"
        #     },
        #     {
        #         "beat": "The Joker interrupts a meeting of Gotham's mafia bosses and offers to kill the Batman for half of the fortune their accountant, Lau, concealed before fleeing to Hong Kong to avoid extradition.",
        #         "place": "Gotham City Bank",
        #         "plot_element": "Conflict"
        #     },
        #     {
        #         "beat": "With the help of Wayne Enterprises CEO Lucius Fox, Batman finds Lau in Hong Kong and returns him to the custody of Gotham police. His testimony enables Dent to apprehend the crime families.",
        #         "place": "Hong Kong",
        #         "plot_element": "Rising Action"
        #     },
        #     {
        #         "beat": "The bosses accept the Joker's offer, and he kills high-profile targets involved in the trial, including the judge and police commissioner.",
        #         "place": "Gotham City",
        #         "plot_element": "Dilemma"
        #     },
        #     {
        #         "beat": "The Joker targets Dent at a fundraising dinner and throws Rachel out of a window, but Batman rescues her.",
        #         "place": "Rachel's apartment",
        #         "plot_element": "Climax"
        #     },
        #     {
        #         "beat": "Having deduced Batman's feelings for Rachel, the Joker reveals she and Dent are being held separately in buildings rigged to explode.",
        #         "place": "Batcave",
        #         "plot_element": "Falling Action"
        #     },
        #     {
        #         "beat": "Batman interrogates the Joker, who says he finds Batman entertaining and has no intention of killing him.",
        #         "place": "Police station",
        #         "plot_element": "Resolution"
        #     },
        #     {
        #         "beat": "The Joker escapes custody, extracts the fortune's location from Lau, and burns all of it, killing Lau in the process.",
        #         "place": "Gotham City",
        #         "plot_element": "Denouement"
        #     }
        # ]
        finalDraft = []
        for i in range(len(scenes)):
            finalCut = {}
            finalCut["beat"] = scenes[i]["beat"]
            finalCut["place"] = scenes[i]["place"]
            finalCut["placeDescription"] = placesDescription[scenes[i]["place"]]
            finalCut["plotElement"] = scenes[i]["plot_element"]
            if i > 0:
                finalCut["previousBeat"] = scenes[i-1]["beat"]
            else:
                finalCut["previousBeat"] = "NOT AVAILABLE"

            finalDraft.append(finalCut)
            charDescInBeat = getCharectersForBeat(scenes[i]["beat"], characters, False)
            finalCut["charecters"]  = charDescInBeat
            finalDraft.append(finalCut)
        for fd in finalDraft:
            print("{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}")
            print(fd)
            print("{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}")
        lst = []
        count = 0
        for scene in finalDraft:
            count=count+1
            dialoguePrompt = getDialogues(scene, logline)
            sceneResponse = model.generate_content(dialoguePrompt)
            
            lst.append([sceneResponse.text, count])
            
            print(lst)
        # for i in range(len(finalDraft)):
        #     scene = finalDraft[i]
        #     dialogusRaw = lst[i]
        #     charectersList = getCharectersForBeat(scenes[i]["beat"], characters, True)


        l = lst

        return {"response":lst}, 200
    except ValueError:
        return {"error":"some value error has happened"}, 500
    except IndexError:
        return {"error":"Some bad has happend"}, 500
    
   


    

if __name__ == '__main__':
    app.debug = True
    app.run()