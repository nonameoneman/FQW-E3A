from wsgiref.util import request_uri
from django.shortcuts import redirect, render
from app_users.models import User, Advisor, Groups, Student, Teacher
from app_calendars.models import Ac_years
from app_disciplines.models import Disciplines, Discipline_reg
    
def my_redirect(request):
    if request.user.is_authenticated == False:
        return redirect('login/')
    
    elif request.user.is_advisor == True:
        user = User.objects.all()
        groups = Groups.objects.all()
        student = Student.objects.all()
        advisor = Advisor.objects.all()
        teacher = Teacher.objects.all()
        discipline = Disciplines.objects.all()
        dis_reg = Discipline_reg.objects.all()
        years = Ac_years.objects.all()
        
        context = {
            'users': user,
            'advisor': advisor,
            'groups': groups,
            'student': student,
            'teacher': teacher,
            'discipline': discipline,
            'dis_reg': dis_reg,
            'years': years,
            'title': 'Ассистент Советника',
        }
            
        return render(request, 'app_assistant/assistant_a.html', context=context)
    
    elif request.user.is_teacher == True:
        user = User.objects.all()
        teacher = Teacher.objects.all()
        groups = Groups.objects.all()
        student = Student.objects.all()
        advisor = Advisor.objects.all()
        discipline = Disciplines.objects.all()
        dis_reg = Discipline_reg.objects.all()
        years = Ac_years.objects.all()
        
        context = {
            'teacher': teacher,
            'users': user,
            'advisor': advisor,
            'groups': groups,
            'student': student,
            'discipline': discipline,
            'dis_reg': dis_reg,
            'years': years,
            'title':'Ассистент Преподавателя',
        }
        
        return render(request, 'app_assistant/assistant_t.html', context=context)
    
    elif request.user.is_staff == True:
        return render(request, 'admin_redirect.html', {'title':'Администратор'})
    
    else:
        user = User.objects.all()
        groups = Groups.objects.all()
        student = Student.objects.all()
        advisor = Advisor.objects.all()
        discipline = Disciplines.objects.all()
        dis_reg = Discipline_reg.objects.all()
        years = Ac_years.objects.all()
        
        context = {
            'users': user,
            'advisor': advisor,
            'groups': groups,
            'student': student,
            'discipline': discipline,
            'dis_reg': dis_reg,
            'years': years,
            'title': 'Ассистент Студента',
        }
        
        return render(request, 'app_assistant/assistant_s.html', context=context)
    endif