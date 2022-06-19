from itertools import count
from turtle import end_fill
from urllib import request, response
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from app_users.models import *
from app_calendars.models import *
from .models import *
from .forms import *
import datetime
      
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
            if 'academ' in request.POST:
                academ_list = request.POST.getlist('send')
                for snd in academ_list:
                    dis_reg.filter(pk=int(snd)).update(send=True)
            elif 'create' in request.POST:
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
                        if dr.student_id == s.id and dr.academ_c == True:
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
            count_r = 128 - count_r
            return count_r
        
        calend = Ac_years.objects.all()
        today = datetime.date.today()
        
        for c in calend:
            def m1():
                if c.pk == 2:
                    if today > c.m1_s and today < c.m1_e:
                        return True
                    else:
                        return False
            def m2():
                if c.pk == 2:
                    if today > c.m2_s and today < c.m2_e:
                        return True
                    else:
                        return False
            def m3():
                if c.pk == 2:
                    if today > c.m3_s and today < c.m3_e:
                        return True
                    else:
                        return False
            def m4():
                if c.pk == 2:
                    if today > c.m4_s and today < c.m4_e:
                        return True
                    else:
                        return False
                    
            def is_i():
                    if c.pk == 2:
                        if today > c.i1_s and today < c.i1_e:
                            return True
                        elif today > c.i2_s and today < c.i2_e:
                            return True
                        else:
                            return False
        
        context = {
            'users': user,
            'advisor': advisor,
            'groups': groups,
            'student': student,
            'teacher': teacher,
            'dis': dis,
            'dis_reg': dis_reg,
            'title': 'Регистрация на предметы',
            'submitted': submitted,
            'cf': credit_counting_conf(),
            'cr': credit_counting_req(),
            'co': credit_ost(),
            'form': form,
            'm1': m1(),
            'm2': m2(),
            'm3': m3(),
            'm4': m4(),
            'is_i': is_i(),
            'calend': calend,
            'today': today
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

def academ_conf(request):
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
        
        if request.method == "POST":
            conf_list = request.POST.getlist('cnf')
            for c in conf_list:
                dis_reg.filter(pk=int(c)).update(academ_c=True)
            
            abon_list = request.POST.getlist('abn')
            for a in abon_list:
                dis_reg.filter(pk=int(a)).update(academ_b=True)    
                
            return redirect('ac_conf')  
        
        return render(request, 'app_disciplines/ac_a.html', context=context)
    
    elif request.user.is_teacher == True:
        return redirect('my_redirect')
    
    elif request.user.is_staff == True:
        return redirect('my_redirect')
    
    else:       
        if request.method == "POST":
            if 'academ' in request.POST:
                academ_list = request.POST.getlist('send')
                for snd in academ_list:
                    dis_reg.filter(pk=int(snd)).update(send=True)
            elif 'clear' in request.POST:
                clear_list = request.POST.getlist('hide')
                for clr in clear_list:
                    dis_reg.filter(pk=int(clr)).update(hide=True)
        
        context = {
            'users': user,
            'advisor': advisor,
            'groups': groups,
            'student': student,
            'teacher': teacher,
            'dis': dis,
            'dis_reg': dis_reg,
            'title': 'Регистрация на предметы',
        }
           
        return render(request, 'app_disciplines/ac_s.html', context=context)
    
def reg_list(request):
    
    user = User.objects.all()
    groups = Groups.objects.all()
    student = Student.objects.all()
    advisor = Advisor.objects.all()
    teacher = Teacher.objects.all()
    dis = Disciplines.objects.all()
    dis_reg = Discipline_reg.objects.all()

    if request.user.is_advisor == True:
        return redirect('my_redirect')
    elif request.user.is_teacher == True: 
        return redirect('my_redirect')
    elif request.user.is_staff == True: 
        return redirect('my_redirect')   
    else:                  
        date = datetime.date.today()
        
        context = {
            'date' : date,
            'users': user,
            'advisor': advisor,
            'groups': groups,
            'student': student,
            'teacher': teacher,
            'dis': dis,
            'dis_reg': dis_reg,
            'date': date,
            'title': 'Регистрация на предметы',
        }

        return render(request, 'app_disciplines/reg_list.html', context=context)