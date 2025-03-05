from django.shortcuts import render
from django.http import JsonResponse
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
    if request.method == "POST":
        print("Button clicked !!!!")
        return JsonResponse({"message": "button_clicked"})
    return JsonResponse({"error": "Invalid request"}, status=400)