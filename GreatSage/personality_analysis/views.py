import csv
from django.shortcuts import redirect, render
from .models import TextAnalysis, HandwritingAnalysis, Chat
import openai
import json
from django.http import JsonResponse
from pathlib import Path
import spacy
from . import wordFrequency2
from .forms import ImageUploadForm
<<<<<<< HEAD

nlp = spacy.load("en_core_web_md")

openai_api_key = "add the API key here"
=======
import markdown

nlp = spacy.load("en_core_web_md")

openai_api_key = "Put your api key here"
>>>>>>> 4fa089f (full)
openai.api_key = openai_api_key


def dashboard(request):
    return render(request, "dashboard.html")

def text(request):
    if request.method == "POST":
<<<<<<< HEAD
        print("okay")
=======

>>>>>>> 4fa089f (full)
        # Get the text input from the request
        wordFrequency2.nlp = nlp
        text = wordFrequency2.process_text(request.POST.get("text"))
        file_path = Path.cwd () / "personality_analysis"/"Great Sage analysis spreadsheet - Qauntifiers.csv"
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
        response = openai.ChatCompletion.create(
            model = "gpt-4",
            messages=[
            {"role": "system", "content": f"You will have to give an insight into the character treats based on the following percentage analogy, please remember that you are answering a 1000 word text directly to the user and do not talk about the word frequency used eg Adverb frequency, Pronoun Frequency.... The user shouldn't know about any of these values . In fact, answer directly in the form of an essay. From these informations:{reader}"},
            {"role": "user", "content": str(text)},
            ]
            )
        answer1 = response.choices[0].message.content.strip()
        response1 = openai.ChatCompletion.create(
            model = "gpt-4",
            messages=[
<<<<<<< HEAD
            {"role": "system", "content": f"I want you to make an essay presenting the person's qualities and flaws in a balanced manner. In the essay, do not make reference to his frequency usage of function words just present the qualities and flaws in a very beautiful and appealing manner. Adress the message in the second person"},
                {"role": "user", "content": str(answer1)},
            ]
            )
        answer = response1.choices[0].message.content.strip()
=======
            {"role": "system", "content": f"I want you to make boulet points(in a markdown syntax) of the person's qualities and flaws in a balanced manner. In the boulet points, do not make reference to his frequency usage of function words just present the qualities and flaws in a very beautiful and appealing manner. Adress the message in the second person"},
                {"role": "user", "content": str(answer1)},
            ]
            )
        answer = markdown.markdown(response1.choices[0].message.content.strip())
>>>>>>> 4fa089f (full)
        text = request.POST.get("text")
        file_path = Path.cwd () / "personality_analysis"/"Sound analysis spreadsheet.csv"
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
        response = openai.ChatCompletion.create(
            model = "gpt-4",
            messages=[
            {"role": "system", "content": f"I want you to analyse the way of writing of this person based on the information present in {reader} and for each classification system, associate a given musical genre to the person based on the his way of writing"},
            {"role": "user", "content": str(text)},
            ]
            )
        song1 = response.choices[0].message.content.strip()
        response1 = openai.ChatCompletion.create(
            model = "gpt-4",
            messages=[
<<<<<<< HEAD
            {"role": "system", "content": f"I want you to make an educated guess on the person's music taste. Based on the information present in {answer1}. After the explanation, you should end in a 'You likely like [here you put the various genres in order]' "},
                {"role": "user", "content": str(song1)},
            ]
            )
        song = response1.choices[0].message.content.strip()
        return render(request, 'result.html', {'answer': answer, 'song': song})
    else:
        print("nope")
=======
            {"role": "system", "content": f"I want you to make an educated guess on the person's music taste in boulet points(in a markdown format). Based on the information present in {answer1}.  Adress the message in the second person"},
                {"role": "user", "content": str(song1)},
            ]
            )
        song = markdown.markdown(response1.choices[0].message.content.strip())
        return render(request, 'result.html', {'answer': answer, 'song': song})
>>>>>>> 4fa089f (full)
    return render(request, 'text_analysis.html')

def result(request):
    return render(request, 'result.html')

# def handwriting(request):   
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             user_image = form.save()
        
#             image_url = user_image.handwriting_image.url

#             response = openai.ChatCompletion.create(
#                 model="gpt-4", 
#                 messages=[
#                     {
#                         "role": "user",
#                         "content": "What's in this image?"
#                     },
#                     {
#                         "role": "user",
#                         "content": f"Here's the image URL: {image_url}"
#                     }
#                 ],
#                 max_tokens=300
#             )

#             answer = response.choices[0].message['content']
#             return render(request, 'result.html', {'answer': answer})
#     else:
#         form = ImageUploadForm()
#     return render(request, 'handwriting.html', {"form":form})

# def sound_analysis(request):
#     if request.method == "POST":
#         # Get the text input from the request
#         text = request.POST.get("text")
#         file_path = Path.cwd () / "personality_analysis"/"Sound analysis spreadsheet.csv"
#         with open(file_path, 'r') as f:
#             reader = csv.reader(f)
#         response = openai.ChatCompletion.create(
#             model = "gpt-4",
#             messages=[
#             {"role": "system", "content": f"I want you to analyse the way of writing of this person based on the information present in {reader} and for each classification system, associate a given musical genre to the person based on the his way of writing"},
#             {"role": "user", "content": str(text)},
#             ]
#             )
#         answer1 = response.choices[0].message.content.strip()
#         response1 = openai.ChatCompletion.create(
#             model = "gpt-4",
#             messages=[
#             {"role": "system", "content": f"I want you to make an educated guess on the person's music taste. Based on the information present in {answer1}. After the explanation, you should end in a 'You likely like [here you put the various genres in order]' "},
#                 {"role": "user", "content": str(answer1)},
#             ]
#             )
#         answer = response1.choices[0].message.content.strip()
#         return render(request, 'result.html', {'answer': answer})
#     return render(request, 'sound_analysis.html')



def ask_openai(message):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Great Sage, an advanced conversational AI specialized in behavioral and psychological concepts. Engage the user in interactive discussions that help them explore their personality traits, thought processes, and behavioral patterns. Provide insightful, engaging, and thought-provoking responses, similar to a modern ChatGPT experience. Ask follow-up questions, suggest psychological theories or frameworks when relevant, and encourage self-reflection."},
            {"role": "user", "content": message},
        ]
    )
    
    answer = response.choices[0].message.content.strip()
    return answer

def conversation(request):
    
    chats = Chat.objects.filter(user = request.user)
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        chat = Chat(user=request.user, message=message, response=response)
        chat.save()
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'conversation.html', {'chats': chats})



