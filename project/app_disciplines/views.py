from django.shortcuts import redirect, render
from app_users.models import *
from .models import *
from .forms import *

def dis(request):
    user = User.objects.all()
    groups = Groups.objects.all()
    student = Student.objects.all()
    advisor = Advisor.objects.all()
    teacher = Teacher.objects.all()
    dis = Disciplines.objects.all()
    dis_reg = Discipline_reg.objects.all()
    
    if request.user.is_authenticated == False:
        return redirect('login/')
    
    if request.user.is_advisor == True:
        context = {
            'users': user,
            'advisor': advisor,
            'groups': groups,
            'student': student,
            'teacher': teacher,
            'dis': dis,
            'dis_reg': dis_reg,
            'title': 'Запросы на регистрацию',
        }   
        return render(request, 'app_disciplines/reg_a.html', context=context)
    
    elif request.user.is_teacher == True:
        context = {
            'users': user,
            'advisor': advisor,
            'groups': groups,
            'student': student,
            'teacher': teacher,
            'dis': dis,
            'dis_reg': dis_reg,
            'title': 'Запросы на регистрацию',
        }   
        return render(request, 'app_disciplines/reg_t.html', context=context)
    
    elif request.user.is_staff == True:
        return redirect('my_redirect')
    
    else:
        form = DisciplineRegFrom
        context = {
            'users': user,
            'advisor': advisor,
            'groups': groups,
            'student': student,
            'teacher': teacher,
            'dis': dis,
            'dis_reg': dis_reg,
            'form': form,
            'title': 'Регистрация на предметы',
        }   
        return render(request, 'app_disciplines/reg_s.html', context=context)
