def gettitlepromptprefix(lg):
    p = """
here are few examples that describe some loglines and title for it. please give a  title alone for Example 4
Example 1. Ancient Greek tragedy based upon the myth of Jason and Medea . Medea , a former princess of
the kingdom of Colchis , and the wife of Jason , finds her position in the Greek world threatened as
Jason leaves her for a Greek princess of Corinth . Medea takes vengeance on Jason by murdering his new
wife as well as her own two sons , after which she escapes to Athens . 
Title : A Feminist Tale < end >
Example 2. Ancient Greek tragedy that deals with Antigone 's burial of her brother Polynices , in
defiance of the laws of Creon and the state , and the tragic repercussions of her act of civil
disobedience . Title : In My Brother 's Name < end >
Example 3. Greek comedy that tells the story of the god Dionysus ( also known to the Greeks as Bacchus )
who , despairing of the current state of Athens ' tragedians , travels to Hades with his slave Xanthias
to bring Euripides back from the dead . Title : Dionysus in Hades < end >

Example 4. 
    """
    
    p = p+lg+" Title:? "
    # print("THE PROMPT IS : ",p)

    return p


def getTitleForScifi(lg):
    p = """
    here are few examples that describe some loglines and title for it. please give a  title alone for Example 3
Example 1. A science - fiction fantasy about a naive but ambitious farm boy from a backwater desert who
discovers powers he never knew he had when he teams up with a feisty princess , a mercenary space pilot
and an old wizard warrior to lead a ragtag rebellion against the sinister forces of the evil Galactic
Empire . Title : The Death Star 's Menace < end >
Example 2. Residents of San Fernando Valley are under attack by flying saucers from outer space . The
aliens are extraterrestrials who seek to stop humanity from creating a doomsday weapon that could
destroy the universe and unleash the living dead to stalk humans who wander into the cemetery looking
for evidence of the UFOs . The hero Jeff , an airline pilot , will face the aliens . Title : The Day The
Earth Was Saved By Outer Space . < end >
Example 3. 
"""
    p = p+lg+" Title:? "
    # print("THE PROMPT IS : ",p)
    return p



def getCharecterDescriptionPrompt(lg):
    prompt = """
    Here are the examples of characters from a user input. Generate charecterNames and its charecteristics for Example 2, look for all charecter names donot miss any thing, 
    Example 1. Ancient Greek tragedy based upon the myth of Jason and Medea . Medea , a former princess and
the wife of Jason , finds her position in the Greek world threatened as Jason leaves Medea for a Greek
princess of Corinth . Medea takes vengeance on Jason by murdering his new wife as well as Medea 's own
two sons , after which she escapes to Athens .
< character > Medea < description > Medea is the protagonist of the play . A sorceress and a princess , she
fled her country and family to live with Jason in Corinth , where they established a family of two
children and gained a favorable reputation . Jason has divorced Medea and taken up with a new family . <
stop >
< character > Jason < description > Jason is considered the play 's villain , though his evil stems more from
weakness than strength . A former adventurer , Jason abandons his wife , Medea , in order to marry the
beautiful young daughter of Creon , King of Corinth , and fuels Medea to a revenge . < stop >
< character > Women of Corinth < description > The Women of Corinth are a commentator to the action . They
fully sympathizes with Medea 's plight , excepting her decision to murder her own children . < stop >
< character > Creon < description > Creon is the King of Corinth , banishes Medea from the city . < stop >
< character > The Nurse < description > The Nurse is the caretaker of the house and of the children and
serves as Medea 's confidant . < stop >
<end >
Example 2. """+lg
    return prompt

def getCharecterDescriptions(logLine):
    prompt = """Here are the examples of characters from a user input. Generate charecterNames and its charecteristics for Example 2, look for all charecter names donot miss any thing, 
    Example 1. Ancient Greek tragedy based upon the myth of Jason and Medea . Medea , a former princess and
the wife of Jason , finds her position in the Greek world threatened as Jason leaves Medea for a Greek
princess of Corinth . Medea takes vengeance on Jason by murdering his new wife as well as Medea 's own
two sons , after which she escapes to Athens .
< character > Medea < description > Medea is the protagonist of the play . A sorceress and a princess , she
fled her country and family to live with Jason in Corinth , where they established a family of two
children and gained a favorable reputation . Jason has divorced Medea and taken up with a new family . <
stop >
< character > Jason < description > Jason is considered the play 's villain , though his evil stems more from
weakness than strength . A former adventurer , Jason abandons his wife , Medea , in order to marry the
beautiful young daughter of Creon , King of Corinth , and fuels Medea to a revenge . < stop >
< character > Women of Corinth < description > The Women of Corinth are a commentator to the action . They
fully sympathizes with Medea 's plight , excepting her decision to murder her own children . < stop >
< character > Creon < description > Creon is the King of Corinth , banishes Medea from the city . < stop >
< character > The Nurse < description > The Nurse is the caretaker of the house and of the children and
serves as Medea 's confidant . < stop >
<end >
Example 2. 
""" + logLine
    return prompt


def getPlotOutline(logline, characters):
    prompt = """
    Given is the example for generating plot outline scene wise for given description and character description. hence generate for example 2. note for response format in Example 1, strictly adhere to it, strictly generate all places which are available in logline, be precise get places, plot element, beat
    Example 1. Ancient Greek tragedy based upon the myth of Jason and Medea . Medea , a former princess and
the wife of Jason , finds her position in the Greek world threatened as Jason leaves Medea for a Greek
princess of Corinth . Medea takes vengeance on Jason by murdering his new wife as well as Medea 's own
two sons , after which she escapes to Athens .
Medea is the protagonist of the play . A sorceress and a princess , she fled her country and family to
live with Jason in Corinth , where they established a family of two children and gained a favorable
reputation . Jason has divorced Medea and taken up with a new family .
Jason can be considered the play 's villain , though his evil stems more from weakness than strength . A
former adventurer , Jason abandons his wife , Medea , in order to marry the beautiful young daughter of
Creon , King of Corinth , and fuels Medea to a revenge .
The Women of Corinth serve as a commentator to the action . They fully sympathizes with Medea 's plight ,
excepting her decision to murder her own children .
The King of Corinth Creon banishes Medea from the city .
The Messenger appears only once in the play to bear tragical news .
The Nurse is the caretaker of the house and of the children and serves as Medea 's confidant .
The Tutor of the children is a very minor character and mainly acts as a messenger
< scenes >
< scene >
Place : INT. Medea 's modest home .
Plot element : Exposition .
Beat : The Nurse recounts the chain of events that have turned Medea 's world to enmity . The Nurse
laments how Jason has abandoned Medea and his own children in order to remarry with the daughter of
Creon .
< scene >
Place : INT. Medea 's modest home .
Plot element : Inciting Incident .
Beat : The Nurse confides in the Tutor amd testifies to the emotional shock Jason 's betrayal has
sparked in Medea . The Tutor shares the Nurse 's sympathy for Medea 's plight . Medea 's first words are
cries of helplessness . Medea wishes for her own death .
Place : Medea 's modest home .
< scene >
Plot element : Conflict .
Beat : The Women of Corinth address Medea and try to reason with Medea and convince her that suicide
would be an overreaction . The Nurse recognizes the gravity of Medea 's threat .
Place : EXT. Royal Palace .
< scene >
Plot element : Rising Action .
Beat : Medea pleads to the Nurse that Jason be made to suffer for the suffering he has inflicted upon
her . Creon approaches the house and banishes Medea and her children from Corinth . Medea plans on
killing her three antagonists , Creon , his daughter and Jason .
Place : EXT. Royal Palace .
< scene >
Plot element : Dilemma .
Beat : Jason rebuke Medea for publicly expressing her murderous intentions . Jason defends his choice to
remarry . Medea refuses Jason 's offers and sends him away to his new bride .
Place : EXT. Royal Palace .
< scene >
Plot element : Climax .
Beat : When Jason returns , Medea begins to carry out her ruse . Medea fakes regret and break down in
false tears of remorse . Determined , Medea sends her children to offer poisoned gifts to Creon 's
daughter . Medea 's children face impending doom .
Place : EXT. Royal Palace .
< scene >
Plot element : Falling Action .
Beat : The Messenger frantically runs towards Medea and warns Medea to escape the city as soon as
possible . The Messenger reveals that Medea has been identified as the murderer .
Place : EXT. Royal Palace .
< scene >
Plot element : Resolution .
Beat : Medea and her two dead children are seated in a chariot drawn by dragons . Jason watches in
horror and curses himself for having wed Medea and mourns his tragic losses .
Place : INT. winged chariot .
< scene >
Plot element : Denouement .
Beat : Medea denies Jason the right to a proper burial of his children . She flees to Athens and divines
an unheroic death for Jason .
place : INT. Burial ground
<end >
Example 2: 
"""
    readyPrompt = prompt + logline
    st = ""
    for characters in characters.values():
        st = st+characters +'< scenes > ?'
    readyPrompt = readyPrompt + st
    
    return readyPrompt
    

def getLocationDescritptionPrompt(logline, place):
    prompt  = '''
    Here are the examples of a single line summarization of plot(log line), location name and a location description that closely aligns with the  logline. give description for given place alone, every location name has an reference in logline so please check thoroughly, There will be no case where you cant take description
when Allen makes new friends from a different social class . Ella turns to food to become a famous
chef .
Place : The bar .
Description : The bar is dirty , more than a little run down , with most tables empty . The odor of last
night 's beer and crushed pretzels on the floor permeates the bar . < end >
Example 2. Grandma Phyllis ' family reunion with her two grandchildren is crashed by two bikers .
Place : The Lawn in Front of Grandma Phyllis 's House .
Description : A big oak tree dominates the yard . There is an old swing set on the lawn , and a bright
white fence all around the grass . < end >
Example 3. Ancient Greek tragedy based upon the myth of Jason and Medea . Medea , a former princess and
the wife of Jason , finds her position in the Greek world threatened as Jason leaves Medea for a Greek
princess of Corinth . Medea takes vengeance on Jason by murdering his new wife as well as Medea 's own
two sons , after which she escapes to Athens .
Place : Outside the Royal Palace .
Description : In mythological Ancient Greece , in front of a modest house in Corinth , on the outskirts
of a lavish royal palace where wedding preparations are under way . < end >
Example 4. 
'''
    finalPrompt = prompt + logline +"\n place: "+ place + "Description: ?"

    return finalPrompt


def getDialogues(scene, logline):
    # place, placeDescription, charecterDescription, beat, previousBeat, plotElement, logline
    
    prompt = f"""
    Example 1.
Place : Outside the Royal Palace .
Description : Before Medea 's house in Corinth , near the royal palace of Creon .
Characters : Medea is the protagonist of the play . A sorceress and a princess , she fled her country and
family to live with Jason in Corinth , where they established a family of two children and gained a
favorable reputation . Jason has divorced Medea and taken up with a new family . Jason can be considered
the play 's villain , though his evil stems more from weakness than strength . A former adventurer ,
Jason abandons his wife , Medea , in order to marry the beautiful young daughter of Creon , King of
Corinth , and fuels Medea to a revenge . The Messenger appears only once in the play to bear tragical
news .
Plot element : Resolution .
Summary : Ancient Greek tragedy based upon the myth of Jason and Medea . Medea , a former princess and
the wife of Jason , finds her position in the Greek world threatened as Jason leaves Medea for a Greek
princess of Corinth . Medea takes vengeance on Jason by murdering his new wife as well as Medea 's own
two sons , after which she escapes to Athens .
Previous beat : The Messenger frantically warns Medea to escape the city as soon as possible . The
Messenger reveals that Medea has been identified as the murderer .
Beat : The palace opens its doors , revealing Medea and the two dead children seated in a chariot drawn
by dragons . Jason curses himself for having wed Medea and mourns his tragic losses . Medea denies Jason
the right to a proper burial of his children . Medea flees to Athens and divines an unheroic death for
Jason .

< dialog >
<WOMEN OF CORINTH>
Throw wide the doors and see thy children 's murdered corpses .
<JASON>
Haste , ye slaves , loose the bolts , undo the fastenings , that
I may see the sight of twofold woe , my murdered sons and her , whose
blood in vengeance I will shed . ( MEDEA appears above the house , on
a chariot drawn by dragons ; the children 's corpses are beside her .)
<MEDEA>
Why shake those doors and attempt to loose their bolts , in
quest of the dead and me their murderess ? From such toil desist . If
thou wouldst aught with me , say on , if so thou wilt ; but never shaltthou lay hand on me , so swift the steeds the sun , my father 's sire ,
to me doth give to save me from the hand of my foes .
<JASON>
Accursed woman ! by gods , by me and all mankind abhorred as
never woman was , who hadst the heart to stab thy babes , thou their
mother , leaving me undone and childless ; this hast thou done and still
dost gaze upon the sun and earth after this deed most impious . Curses
on thee ! now perceive what then I missed in the day I brought thee ,
fraught with doom , from thy home in a barbarian land to dwell in Hellas ,
traitress to thy sire and to the land that nurtured thee .
Perish , vile sorceress , murderess of
thy babes ! Whilst I must mourn my luckless fate , for I shall ne 'er
enjoy my new - found bride , nor shall I have the children , whom I bred
and reared , alive to say the last farewell to me ; nay , I have lost
them .
<MEDEA>
To this thy speech I could have made a long reply , but Father
Zeus knows well all I have done for thee , and the treatment thou hast
given me . Yet thou wert not ordained to scorn my love and lead a life
of joy in mockery of me , nor was thy royal bride nor Creon , who gave
thee a second wife , to thrust me from this land and rue it not . Wherefore ,
if thou wilt , call me e'en a lioness , and Scylla , whose home is in
the Tyrrhene land ; for I in turn have wrung thy heart , as well I might .
<JASON>
Thou , too , art grieved thyself , and sharest in my sorrow .
<MEDEA>
Be well assured I am ; but it relieves my pain to know thou
canst not mock at me .
<JASON>
O my children , how vile a mother ye have found !
<MEDEA>
My sons , your father 's feeble lust has been your ruin !
<JASON>
'Twas not my hand , at any rate , that slew them .
<MEDEA>
No , but thy foul treatment of me , and thy new marriage .
<JASON>
Didst think that marriage cause enough to murder them ?
<MEDEA>
Dost think a woman counts this a trifling injury ?
<JASON>
So she be self - restrained ; but in thy eyes all is evil .
<MEDEA>
Thy sons are dead and gone . That will stab thy heart .
<end >

Example 2:
Place : {scene["place"]}
Description : {scene["placeDescription"]}
Charecters : {scene["charecters"]}
Plot Element : {scene["plotElement"]}
Summary : {logline}
Previous Beat : {scene["previousBeat"]}
Beat : {scene["beat"]}

< dialogues >
"""

    return prompt
