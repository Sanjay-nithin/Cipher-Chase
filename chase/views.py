from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Team
import requests
import json

# Create your views here.
def redirect_to_login(request):
    return redirect("login_team")

def login(request):
    return render(request, "login.html")

def home(request):
    return render(request, "firstpage.html")

def play(request):
    return render(request, "gamepage.html")

def open_level(request, level):
    return render(request, f'level{level}.html')

def done(request):
    return render(request, "price.html")

def question_page(request, level, question):
    total = 4

    qlinks = [{"number":i, 'url':f'level/{level}/question/{i}'} for i in range(1, total+1)]

    return render(request, f'level_{level}/question{question}.html', {
        'level': level,
        'question': question,
        'qlinks': qlinks,
    })

@csrf_exempt
def track_tab_switch(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Parse incoming JSON request
            count = data.get("count", 0)  # Extract count of tab switches

            # Here, you can log the count, store it in a database, or trigger an action
            print(f"Tab switched {count} times")  # Debugging (check server logs)

            return JsonResponse({"message": "Tab switch recorded", "count": count})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)


def open_morse(request, level):
    return render(request, f"morse-code{level}.html")

@csrf_exempt
def register_team(request):
    if request.method == "POST":
        data = json.loads(request.body)
        team_name = data.get("team_name")

        if Team.objects.filter(name=team_name).exists():
            return JsonResponse({"success": False, "message": "Team name already exists!"})
        
        Team.objects.create(name=team_name)
        return JsonResponse({"success": True, "message": "Team registered successfully! Please login."})

@csrf_exempt
def login_team(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            team_name = data.get("team_name", "").strip()

            if not team_name:
                return JsonResponse({"success": False, "message": "Enter a valid team name."})

            if Team.objects.filter(name=team_name).exists():
                return JsonResponse({"success": True, "message": "Login successful!"})
            else:
                return JsonResponse({"success": False, "message": "Team not found. Please register."})

        except json.JSONDecodeError:
            return JsonResponse({"success": False, "message": "Invalid request format."})

    # **Render the login page when accessed via GET**
    return render(request, "login.html")

def decypher(request):
    return render(request, "morse_code.html")

@csrf_exempt
def execute_code(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            # Validate required fields
            if "language" not in data or "files" not in data:
                return JsonResponse({"error": "Invalid request format"}, status=400)

            # Forward request to Piston API
            piston_url = "http://13.234.239.94:2000/api/v2/execute"
            response = requests.post(piston_url, json=data)

            return JsonResponse(response.json())

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
        except requests.RequestException as e:
            return JsonResponse({"error": f"API request failed: {str(e)}"}, status=500)
        except Exception as e:
            return JsonResponse({"error": f"Internal server error: {str(e)}"}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)