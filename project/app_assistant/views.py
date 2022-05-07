from django.shortcuts import render

  
def my_redirect(request):
    if request.user.is_advisor == True:
        return render(request, 'app_assistant/assistant_a.html', {'title':'Ассистент Академического Советника'})
    else:
        return render(request, 'app_assistant/assistant_s.html', {'title':'Ассистент Студента'})