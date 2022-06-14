from django.shortcuts import render, redirect
from app_users.models import *
from app_news.forms import *

def news(request):
    if request.user.is_advisor == True:    
        user = User.objects.all()
        groups = Groups.objects.all()
        student = Student.objects.all()
        advisor = Advisor.objects.all()
        
        def find_advisor():
            for a in advisor:
                if a.user_id == request.user.id:
                    return a.pk
        
        initaial_data = {
            'advisor': find_advisor,
        }
        
        if request.method == "POST":
            form = NewsForm(request.POST, initial=initaial_data)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/news/?submitted=true')
        else:
            form = NewsForm(initial=initaial_data)
            if 'submitted' in request.GET:
                submitted = True
        
        context = {
            form: form,
            'users': user,
            'advisor': advisor,
            'groups': groups,
            'student': student,
            'title':'Управление новостями',
        }
        
        return render(request, 'app_news/news_a.html', context=context)

    elif request.user.is_teacher == True or request.user.is_staff:
        return redirect('my_redirect')
    
    else:
        user = User.objects.all()
        groups = Groups.objects.all()
        student = Student.objects.all()
        advisor = Advisor.objects.all()
        
        context = {
            'users': user,
            'advisor': advisor,
            'groups': groups,
            'student': student,
            'title':'Новости',
        }
        
        return render(request, 'app_news/news_s.html', context=context)