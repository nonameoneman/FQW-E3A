from wsgiref.util import request_uri
from django.shortcuts import render
from app_users.models import User, Advisor, Groups, Student
    
def my_redirect(request):
    if request.user.is_advisor == True:
        user = User.objects.all()
        groups = Groups.objects.all()
        student = Student.objects.all()
        advisor = Advisor.objects.all()
        
        context = {
            'users': user,
            'advisor': advisor,
            'groups': groups,
            'student': student,
            'title': 'Ассистент академического советника',
        }
            
        return render(request, 'app_assistant/assistant_a.html', context=context)
    
    elif request.user.is_staff == True:
        return render(request, 'admin_redirect.html', {'title':'Администратор'})
    
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
            'title': 'Ассистент Студентаа',
        }
        
        return render(request, 'app_assistant/assistant_s.html', context=context)
    endif