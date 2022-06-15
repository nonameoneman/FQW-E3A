from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from app_users.models import *
from app_news.forms import *

def news(request):
    
    user = User.objects.all()
    groups = Groups.objects.all()
    student = Student.objects.all()
    advisor = Advisor.objects.all()
    news = News.objects.all()
    
    def find_advisor():
        for a in advisor:
            if a.user_id == request.user.id:
                return a.pk
    
    if request.user.is_advisor == True:    
        
        initaial_data = {
            'advisor': find_advisor,
        }
        
        submitted = False
        
        if request.method == "POST":
            form = NewsForm(request.POST, initial=initaial_data)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/news/?submitted=true')
        else:
            form = NewsForm(initial=initaial_data)
            if 'submitted' in request.GET:
                submitted = True
        
        form.fields['advisor'].widget = forms.HiddenInput()
        
        context = {
            'form': form,
            'users': user,
            'advisor': advisor,
            'groups': groups,
            'student': student,
            'news': news,
            'title':'Управление новостями',
        }
        
        return render(request, 'app_news/news_a.html', context=context)

    elif request.user.is_teacher == True or request.user.is_staff:
        return redirect('my_redirect')
    
    else:        
        context = {
            'users': user,
            'advisor': advisor,
            'groups': groups,
            'student': student,
            'news': news,
            'title':'Новости',
        }
        
        return render(request, 'app_news/news_s.html', context=context)