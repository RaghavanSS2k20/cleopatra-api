from flask import Flask, request
from  dotenv import load_dotenv
import os
import google.generativeai as genai
from promptprefixes import gettitlepromptprefix, getTitleForScifi,getCharecterDescriptions, getPlotOutline, getLocationDescritptionPrompt
load_dotenv()
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key = GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')
app = Flask(__name__)

@app.route('/')
def ping():
    return {"Message":"working"}, 200


@app.route('/script', methods=['POST'])
def get_script():
    data = request.json
    logline = data.get("logline")
    print(logline)
    prompt = getCharecterDescriptions(logline)
    response = model.generate_content(prompt)
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
        print(scene_info[2])
        beat = scene_info[2].split(":")[1].strip()
        scenes.append({"place": place, "plot_element": plot_element, "beat": beat})
    placesDescription = []
    for scene in scenes:
        place = scene["place"]
        prompt = 


    
    return {"response":scenes}, 200
   


    

app.run()