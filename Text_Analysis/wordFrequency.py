import spacy  
import re
nlp = spacy.load("en_core_web_md")  

text = str(input("Enter a text: ")) + " "  
doc = nlp(text)
text = re.sub(r'([.,!?])', r' \1 ', text) 
new_word = str()  
text_frequency_classification = {"words":{}, "Part of Speech":{}}

# Global variables initalisation
ArticleFrequency = None
PronounsFrequency = None
PrepositionFrequency = None
AdverbFrequency = None
conjunctionsFrequency = None
AdverbFrequency = None
QuantifierFrequency = None
NegationFrequency = None
DeterminerFrequency = None
ComparativeFrequency = None
ModalVerbFrequency = None
PossessiveFrequency = None
VerbFrequency = None


def wordFrequency():
    text_data = {}  
    for token in doc: 
        if token.text.lower() in text_data:
            text_data[token.text.lower()] += 1
        else:
            text_data[token.text.lower()] = 1  

    text_frequency_classification["words"] = text_data

def partOfSpeechFrequency():
    text_data = {}
    for token in doc:
        if token.pos_ in text_data:
            text_data[token.pos_] += 1
        else:
            text_data[token.pos_] = 1 

    text_frequency_classification["Part of Speech"] = text_data  

def partOfSpeechClassification():
    text_part_of_speech_classification = {}
    for token in doc:
        if token.tag_ not in [".",",",":","''","-LRB-","-RRB-","HYPH","...","SYM"]:
            if token.tag_ not in text_part_of_speech_classification.keys():
                text_part_of_speech_classification[token.tag_] = {"words":[], "Total Size":0}
            
            if token.text.lower() not in text_part_of_speech_classification[token.tag_]["words"]:
                text_part_of_speech_classification[token.tag_]["words"].append(token.text.lower())
            text_part_of_speech_classification[token.tag_]["Total Size"] +=1

def Pronouns(token):
    PronounsList = {
        "Personal":["i","me","my","mine","we","us","our","ours","you","your","yours","he","him","his","she","her","hers","it","its","they","them","their","theirs"],
        "Impersonal":["it", "this","that","these","those","one","ones"],
        "Relative":["who","whom","whose","which","what"],
        "Demonstrative":["this","that","these","those"]
    }
    global PronounsFrequency
    if PronounsFrequency == None:
        PronounsFrequency = {x:{"Pronoun Frequency":0} for x in PronounsList.keys() }
    values = [value for key in PronounsList for value in PronounsList[key]]
    
    if token.text.lower() in values:
        for key in PronounsList:
            if token.text.lower() in PronounsList[key]:
                PronounsFrequency[key]["Pronoun Frequency"] += 1

def Articles(token):
    ArticlesList ={
        "Definite":["a","an"],
        "Indefinite":["the"]
    }
    global ArticleFrequency 
    if ArticleFrequency == None:
        ArticleFrequency = {x:{"Article Frequency":0} for x in ArticlesList.keys()}
    values = [value for key in ArticlesList for value in ArticlesList[key]]
    if token.text.lower() in values:
        for key in ArticlesList:
            if token.text.lower() in ArticlesList[key]:
                ArticleFrequency[key]["Article Frequency"] += 1

def Prepositions(token):
    PrepositionList = ["about", "above", "across", "after", "against", "along", "among", "around", "at", 
                       "before", "behind", "below", "beneath", "beside", "between", "beyond", "by", "down", 
                       "during", "except", "for", "from", "in", "inside", "into", "like", "near", "of", "off", "on",
                       "onto", "out", "outside", "over", "past", "since", "through", "throughout", "to", "toward", "under", 
                       "underneath", "until", "up", "upon", "with", "within", "without"]
    
    global PrepositionFrequency
    if PrepositionFrequency == None:
        PrepositionFrequency = {"Preposition Frequency":0}
    if token.text.lower() in PrepositionList:
        PrepositionFrequency["Preposition Frequency"] += 1

def AuxilaryVerbs(token):
    VerbList = ["am", "is", "are", "was", "were", "be", "being", "been", "have", "has", "had", "do", 
                "does", "did", "will", "would", "shall", "should", "can", "could", "may", "might", "must"]
    
    global VerbFrequency
    if VerbFrequency == None:
        VerbFrequency = {"Frequency":0}
    if token.text.lower() in VerbList:
        VerbFrequency["Frequency"] += 1

def conjunctions(token):
    ConjunctionList = {
        "Coordinating":["and","but","or","nor","for","so","yet"],
        "Subordinating":["although","because","if","since","though","unless","until","when","where","while"],

    }

    global conjunctionsFrequency
    if conjunctionsFrequency == None:
        conjunctionsFrequency = {x:{"Conjuction Frequency":0} for x in ConjunctionList.keys()}
    values = [value for key in ConjunctionList for value in ConjunctionList[key]]
    if token.text.lower() in values:
        for key in ConjunctionList:
            if token.text.lower() in ConjunctionList[key]:
                conjunctionsFrequency[key]["Conjunction Frequency"] += 1

def Adverbs(token):
    AdverbList = {
        "Intensifiers":["however","therefore","moreover","consequently","furthermore","very","quite","rather","always","never","just"],
        "Heghing":["almost","often","sometimes","seldom","here","there","now","then","meanwhile","thus"]
    }

    global AdverbFrequency
    if AdverbFrequency == None:
        AdverbFrequency = {x:{"Adverb Frequency":0} for x in AdverbList.keys()}
    values = [value for key in AdverbList for value in AdverbList[key]]
    if token.text.lower() in values:
        for key in AdverbList:
            if token.text.lower() in AdverbList[key]:
                AdverbFrequency[key]["Conjunction Frequency"] += 1

def Quantifiers(token):
    QuantifierList = ["all","some","any","few","many","much","several","each","every","both","either","neither"]

    global QuantifierFrequency
    if QuantifierFrequency == None:
        QuantifierFrequency = {"Frequency":0}
    if token.text.lower() in QuantifierList:
        QuantifierFrequency["Frequency"] += 1

def Negations(token):
    NegationList = ["no","not","none","neither","nor","never"]
    global NegationFrequency
    if NegationFrequency == None:
        NegationFrequency = {"Frequency":0}
    if token.text.lower() in NegationList:
        NegationFrequency["Frequency"] +=1

def Determiners(token):
    DeterminerList = ["my","your","his","her","its","our","their","this","that","these","those","each","every","some","any","no","many","few","much","several","enough"]
    global DeterminerFrequency
    if DeterminerFrequency == None:
        DeterminerFrequency = {"Frequency":0}
    if token.text.lower() in DeterminerList:
        DeterminerFrequency["Frequency"] +=1

def Comparatives(token):
    ComparativeList = ["than","more","less","most","least","as","such"]
    global ComparativeFrequency
    if ComparativeFrequency == None:
        ComparativeFrequency = {"Frequency":0}
    if token.text.lower() in ComparativeList:
        ComparativeFrequency["Frequency"] += 1

def ModalVerbs(token):
    ModalVerbList = ["can","could","may","might","must","shall","should","will","would"]
    global ModalVerbFrequency
    if ModalVerbFrequency == None:
        ModalVerbFrequency = {"Frequency":0}
    if token.text.lower() in ModalVerbList:
        ModalVerbFrequency["Frequency"] += 1

def Possessives(token):
    PossessiveList = {
        "Pronousn":["mine","yours","his","hers","ours","theirs"],
        "Determiners":["my","your","his","her","its","our","their"]
    }
    global PossessiveFrequency
    if PossessiveFrequency == None:
        PossessiveFrequency = {x:{"Possessive Frequency":0} for x in PossessiveList.keys() }
    values = [value for key in PossessiveFrequency for value in PossessiveList[key]]
    if token.text.lower() in values:
        for key in PossessiveList:
            if token.text.lower() in PossessiveList[key]:
                PossessiveFrequency[key]["Possessive Frequency"] += 1

def mainloop():
    wordFrequency()
    partOfSpeechFrequency()
    partOfSpeechClassification()
    for token in doc:
        Articles(token)
        Pronouns(token)
        Prepositions(token)
        AuxilaryVerbs(token)
        conjunctions(token)
        Adverbs(token)
        Quantifiers(token)
        Negations(token)
        Determiners(token)
        Comparatives(token)
        ModalVerbs(token)
        Possessives(token)

if __name__ == "__main__":
    mainloop()