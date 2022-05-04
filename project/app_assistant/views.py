from django.shortcuts import render

def assistant_a(request):
    return render(request, 'app_assistant/assistant_a.html', {'title':'Ассистент Академического Советника'})

def assistant_s(request):
    return render(request, 'app_assistant/assistant_s.html', {'title':'Ассистент Студента'})