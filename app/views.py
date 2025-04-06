from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai
from django.contrib import auth
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Chat
from decouple import config

openai.api_key = config("OPENAI_API_KEY")

def ask_openai(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message},
            ]
        )
        return response.choices[0].message['content'].strip()
    except openai.error.OpenAIError as e:
        print("OpenAI Error:", e)
        return "Something went wrong. Please try again."

def chatbot(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Unauthorized'}, status=401)

        message = request.POST.get('message')
        if not message:
            return JsonResponse({'error': 'Empty message'}, status=400)

        response = ask_openai(message)

        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()
        return JsonResponse({'message': message, 'response': response})

    chats = Chat.objects.filter(user=request.user) if request.user.is_authenticated else []
    return render(request, 'chatbot.html', {'chats': chats})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('chatbot')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return render(request, 'register.html', {'error_message': 'Passwords do not match'})

        try:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            auth.login(request, user)
            return redirect('chatbot')
        except:
            return render(request, 'register.html', {'error_message': 'Username or email already exists'})
    
    return render(request, 'register.html')

def logout_view(request):
    auth.logout(request)
    return redirect('login')
