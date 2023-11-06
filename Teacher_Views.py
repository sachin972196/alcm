from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from  nssps.models import Student,Attendance,Attendance_Report
from nssps.models import Subject
from nssps.models import Session_Year, Teacher
from django.views.decorators.cache import cache_control


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
 

 



@login_required(login_url='/')
def HOME(request):

    return render(request,'teachers/home.html')

 
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def TAKE_ATTENDANCE(request):
    teacher_id = Teacher.objects.get(admin = request.user.id)

    subject = Subject.objects.filter( teacher = teacher_id)

    session_year = Session_Year.objects.all()

    action = request.GET.get('action')

    students =None
    get_subject =None
    get_session_year = None
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')

            get_subject = Subject.objects.get(id = subject_id )
            get_session_year = Session_Year.objects.get(id = session_year_id)


            subject = Subject.objects.filter(id = subject_id)
            for i in subject:
                student_id = i.classes.id 
                students = Student.objects.filter(classes_id = student_id)

             



    context = {
        'subject':subject,
        'session_year':session_year,
        'get_subject':get_subject, 
        'get_session_year':get_session_year,
        'action':action,
        'students':students,
    }

    return render(request,'teachers/take_attendance.html',context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def SAVE_ATTENDANCE(request):

    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')

        attendance_date = request.POST.get('attendance_date')
        student_id = request.POST.getlist('student_id')

        get_subject = Subject.objects.get(id = subject_id )
        get_session_year = Session_Year.objects.get(id = session_year_id)

        attendance = Attendance(
            subject_id = get_subject,
            attendance_date = attendance_date,
            session_year_id = get_session_year,
            
        )
        attendance.save()
        for i in student_id:
            stud_id = i
            int_stud = int(stud_id)
            p_students = Student.objects.get(id = int_stud)

            attendance_report = Attendance_Report(
                student_id = p_students,
                attendance_id = attendance,

            )
            attendance_report.save()


    return redirect('take_attendance')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def TEACHER_VIEW_ATTENDANCE(request):

    teacher_id = Teacher.objects.get(admin = request.user.id)

    subject = Subject.objects.filter(teacher_id = teacher_id)

    session_year = Session_Year.objects.all()

    action = request.GET.get('action')
    
    attendance_date= None
    get_session_year = None
    get_subject =None
    attendance_report =None
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            attendance_date = request.POST.get('attendance_date')


            get_subject =Subject.objects.get(id=subject_id)
            get_session_year = Session_Year.objects.get(id = session_year_id)

            attendance = Attendance.objects.filter(subject_id = get_subject, attendance_date =attendance_date)
            for i in attendance:
                attendance_id = i.id
                attendance_report = Attendance_Report.objects.filter(attendance_id = attendance_id)


    context={
        'subject':subject,
        'session_year':session_year,
        'action':action,
       'get_subject':get_subject,
       'get_session_year':get_session_year,
       'attendance_date':attendance_date,
       'attendance_report':attendance_report,
    }
    return render(request,'teachers/view_attendance.html',context)