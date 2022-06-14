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
            count_r = 41 - count_r
            return count_r
        
        context = {
            'users': user,
            'advisor': advisor,
            'groups': groups,
            'student': student,
            'discipline': discipline,
            'dis_reg': dis_reg,
            'years': years,
            'title': 'Ассистент Студента',
            'cf': credit_counting_conf(),
            'cr': credit_counting_req(),
            'co': credit_ost(),
        }
        
        return render(request, 'app_assistant/assistant_s.html', context=context)
    endif