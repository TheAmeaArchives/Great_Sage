import spacy  
import re
nlp = spacy.load("en_core_web_md")  

text = str(input("Enter a text: ")) + " "  
doc = nlp(text)
text = re.sub(r'([.,!?])', r' \1 ', text) 
new_word = str()  
text_frequency_classification = {"words":{}, "Part of Speech":{}}

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
    PronounsFrequency = {x:{"Pronoun Frequency":0} for x in PronounsList.keys() }
    values = [value for key in PronounsList for value in PronounsList[key]]
    
    if token.text.lower() in values:
        for key in PronounsList:
            if token.text.lower() in PronounsList[key]:
                PronounsFrequency[key]["Pronoun Frequency"] += 1
    return PronounsFrequency  

def Articles(token):
    ArticlesList ={
        "Definite":["a","an"],
        "Indefinite":["the"]
    }
    ArticleFrequency = {x:{"Article Frequency":0} for x in ArticlesList.keys()}
    values = [value for key in ArticlesList for value in ArticlesList[key]]
    if token.text.lower() in values:
        for key in ArticlesList:
            if token.text.lower() in ArticlesList[key]:
                ArticleFrequency[key]["Article Frequency"] += 1
    return ArticleFrequency

def Prepositions(token):
    PrepositionList = ["about", "above", "across", "after", "against", "along", "among", "around", "at", 
                       "before", "behind", "below", "beneath", "beside", "between", "beyond", "by", "down", 
                       "during", "except", "for", "from", "in", "inside", "into", "like", "near", "of", "off", "on",
                       "onto", "out", "outside", "over", "past", "since", "through", "throughout", "to", "toward", "under", 
                       "underneath", "until", "up", "upon", "with", "within", "without"]
    PrepositionFrequency = {"Preposition Frequency":0}
    if token.text.lower() in PrepositionList:
        PrepositionFrequency["Preposition Frequency"] += 1

def AuxilaryVerbs(token):
    VerbList = ["am", "is", "are", "was", "were", "be", "being", "been", "have", "has", "had", "do", 
                "does", "did", "will", "would", "shall", "should", "can", "could", "may", "might", "must"]
    VerbFrequency = {"Frequency":0}
    if token.text.lower() in VerbList:
        VerbFrequency["Frequency"] += 1

def conjunctions(token):
    ConjunctionList = {
        "Coordinating":["and","but","or","nor","for","so","yet"],
        "Subordinating":["although","because","if","since","though","unless","until","when","where","while"],

    }
    conjunctionsFrequency = {x:{"Conjuction Frequency":0} for x in ConjunctionList.keyx()}
    values = [value for key in ConjunctionList for value in ConjunctionList[key]]
    if token.text.lower() in values:
        for key in ConjunctionList:
            if token.text.lower() in ConjunctionList[key]:
                conjunctionsFrequency[key]["Conjunction Frequency"] += 1
    return conjunctionsFrequency

def Adverbs(token):
    AdverbList = {
        "Intensifiers":["however","therefore","moreover","consequently","furthermore","very","quite","rather","always","never","just"],
        "Heghing":["almost","often","sometimes","seldom","here","there","now","then","meanwhile","thus"]
    }
    AdverbFrequency = {x:{"Adverb Frequency":0} for x in AdverbList.keys()}
    values = [value for key in AdverbList for value in AdverbList[key]]
    if token.text.lower() in values:
        for key in AdverbList:
            if token.text.lower() in AdverbList[key]:
                AdverbFrequency[key]["Conjunction Frequency"] += 1
    return AdverbFrequency
