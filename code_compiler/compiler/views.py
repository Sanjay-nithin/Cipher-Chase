from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.urls import reverse
import json
from django.shortcuts import get_object_or_404
from .models import User
import bcrypt

# Create your views here.
def question_page(request, level, question):
    total = 3

    qlinks = [{"number":i, 'url':f'level/{level}/question/{i}'} for i in range(1, total+1)]

    return render(request, f'level_{level}/question{question}.html', {
        'level': level,
        'question': question,
        'qlinks': qlinks,
    })

def unity_game(request):
    return render(request, "unitygame.html")

def unity_button(request):
    try:
        if request.method == "POST":
            print("Unity Button Clicked!") 
            data = json.loads(request.body.decode("utf-8"))  # Parse JSON body
            level = int(data.get("level")) + 1
            redirect_url = request.build_absolute_uri(reverse("question", kwargs={"level": level, "question": 1}))
            print(redirect_url)
            return JsonResponse({"redirect":redirect_url}, safe=False)  # Send as JSON
        return JsonResponse({"error": "Invalid request"}, status=400)  
    except Exception as e:
        print(f"Error occured: {e}")
        
def track_tab_switch(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        print(f"Tab switched {data['count']} times.")
        return JsonResponse({"status": "success"})
    return JsonResponse({"error": "Invalid request"}, status=400)

# @csrf_exempt
# def get_progress(request):
#     """Handles both GET (fetch progress) and POST (update progress)."""
    
#     player_id = "default_player"  # You can modify this to get from request

#     if request.method == "GET":
#         # Get the player's progress or default to level 1
#         progress, created = PlayerProgress.objects.get_or_create(player_id=player_id)
#         return JsonResponse({"unlockedLevels": progress.unlocked_levels})

#     elif request.method == "POST":
#         try:
#             data = json.loads(request.body)
#             new_level = data.get("unlockedLevels", 1)

#             progress, created = PlayerProgress.objects.get_or_create(player_id=player_id)
#             progress.unlocked_levels = max(progress.unlocked_levels, new_level)
#             progress.save()

#             return JsonResponse({"message": "Progress saved successfully."}, status=200)
#         except json.JSONDecodeError:
#             return JsonResponse({"error": "Invalid JSON"}, status=400)


@csrf_exempt
def auth(request):
    if request.method == "POST":
        data = json.loads(request.body)
        action = data.get("action")  # "login" or "register"
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return JsonResponse({"error": "Username and password required"}, status=400)

        if action == "register":
            # Check if user exists
            if User.objects.filter(username=username).exists():
                return JsonResponse({"error": "Username already exists"}, status=400)

            # Hash password
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            # Save user
            User.objects.create(username=username, password=hashed_password)
            return JsonResponse({"message": "Registration successful!"}, status=201)

        elif action == "login":
            # Fetch user
            user = get_object_or_404(User, username=username)

            # Verify password
            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({"message": "Login successful!"}, status=200)
            return JsonResponse({"error": "Invalid credentials"}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)