from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse

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
            redirect_url = request.build_absolute_uri(reverse("question", kwargs={"level": 2, "question": 1}))
            print(redirect_url)
            return JsonResponse({"redirect":redirect_url}, safe=False)  # Send as JSON
        return JsonResponse({"error": "Invalid request"}, status=400)  
    except Exception as e:
        print(f"Error occured: {e}")