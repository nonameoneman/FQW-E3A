from itertools import count
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
        
        if request.method == "POST":
            conf_list = request.POST.getlist('cnf')
            for c in conf_list:
                dis_reg.filter(pk=int(c)).update(conf=True)
            
            abon_list = request.POST.getlist('abn')
            for a in abon_list:
                dis_reg.filter(pk=int(a)).update(abon=True)    
                
            return redirect('dis')   
        
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
        
        if request.method == "POST":
            conf_list = request.POST.getlist('cnf')
            for c in conf_list:
                dis_reg.filter(pk=int(c)).update(conf=True)
            
            abon_list = request.POST.getlist('abn')
            for a in abon_list:
                dis_reg.filter(pk=int(a)).update(abon=True)    
                
            return redirect('dis')
           
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
        
        def credit_counting_conf():
            all_data = []
            for dr in dis_reg:
                for s in student:
                    if s.user_id == request.user.id:
                        if dr.student_id == s.id and dr.conf == True:
                            all_data.append(dr.discipline.credits)
            count = 0
            for a in all_data:
                count = count + a
            return count
        
        def credit_counting_req():
            all_data_r = []
            for dr in dis_reg:
                for s in student:
                    if s.user_id == request.user.id:
                        if dr.student_id == s.id and dr.abon != True:
                            all_data_r.append(dr.discipline.credits)
            count_r = 0
            for a in all_data_r:
                count_r = count_r + a
            return count_r
        
        def credit_ost():
            all_data_r = []
            for dr in dis_reg:
                for s in student:
                    if s.user_id == request.user.id:
                        if dr.student_id == s.id:
                            all_data_r.append(dr.discipline.credits)
            count_r = 0
            for a in all_data_r:
                count_r = count_r + a
            count_r = 41 - count_r
            return count_r
        
        
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
            'submitted': submitted,
            'cf': credit_counting_conf(),
            'cr': credit_counting_req(),
            'co': credit_ost(),
        }
        
        def disc_filter():
            list = []
            for s in student:
                if s.user_id == request.user.id:
                    for g in groups:
                        if s.groups_id == g.id:                 
                            for d in dis:
                                if d.department_id == g.department_id:
                                    return d.department_id
        
        form.fields['student'].widget = forms.HiddenInput()
        form.fields['discipline'].queryset = Disciplines.objects.filter(department_id=disc_filter())
           
        return render(request, 'app_disciplines/reg_s.html', context=context)
