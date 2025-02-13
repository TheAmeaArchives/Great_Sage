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

nlp = spacy.load("en_core_web_md")

openai_api_key = "put api key here"
openai.api_key = openai_api_key

def landing(request):
    if request.user.is_authenticated:
        return render(request, "dashboard.html")
    else:
        return render(request, "landing_page.html")
    
def dashboard(request):
    return render(request, "dashboard.html")

def text(request):
    if request.method == "POST":
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
            {"role": "system", "content": f"I want you to make an essay presenting the person's qualities and flaws in a balanced manner. In the essay, do not make reference to his frequency usage of function words just present the qualities and flaws in a very beautiful and appealing manner. Adress the message in the second person"},
                {"role": "user", "content": str(answer1)},
            ]
            )
        answer = response1.choices[0].message.content.strip()
        return render(request, 'result.html', {'answer': answer})
    return render(request, 'text_analysis.html')
    """if request.method == 'POST':
        user = request.user
        text = request.POST['writing']
        TextAnalysis.objects.create(
            user = user,
            text = text,
        )
        return redirect('result')
    return render(request, 'text_analysis.html')"""

def result(request):
    return render(request, 'result.html')

def handwriting(request):   
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            user_image = form.save()
        
            image_url = user_image.handwriting_image.url

            response = openai.ChatCompletion.create(
                model="gpt-4", 
                messages=[
                    {
                        "role": "user",
                        "content": "What's in this image?"
                    },
                    {
                        "role": "user",
                        "content": f"Here's the image URL: {image_url}"
                    }
                ],
                max_tokens=300
            )

            answer = response.choices[0].message['content']
            return render(request, 'result.html', {'answer': answer})
    else:
        form = ImageUploadForm()
    return render(request, 'handwriting.html', {"form":form})



def ask_openai(message):
    #This function gives us the answer from the openai API
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are engage in conversations relating behavioural concepts."},
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



