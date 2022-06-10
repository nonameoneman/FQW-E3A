from turtle import end_fill
from urllib import request
from django.http import HttpResponseRedirect
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
    
    def find_stud():
        for s in student:
            if s.user_id == request.user.id:
                return s.pk
    
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
        initaial_data = {
            'student': find_stud,
        }
        
        submitted = False
        
        if request.method == "POST":
            form = DisciplineRegFrom(request.POST, initial=initaial_data)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/disciplines/?submitted=true')
        else:
            form = DisciplineRegFrom(initial=initaial_data)
            if 'submitted' in request.GET:
                submitted = True
        
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
            'submitted': submitted
        }
        
        def disc_filter():
            for s in student:
                if s.user_id == request.user.id:
                    for g in groups:
                        if s.groups_id == g.id:                 
                            for dr in dis_reg:
                                if dis_reg.department_id == g.department_id:
                                    return dis_reg.id
        
        form.fields['student'].widget = forms.HiddenInput()
        form.fields['discipline'].queryset = Discipline_reg.objects.filter(id=[disc_filter(),])
           
        return render(request, 'app_disciplines/reg_s.html', context=context)
