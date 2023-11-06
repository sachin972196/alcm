from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required

from nssps.models import Student,Subject,Attendance,Attendance_Report
from django.views.decorators.cache import cache_control


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def HOME(request):

    return render(request,'students/home.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def SUTDENT_VIEW_ATTENDANCE(request):

    student = Student.objects.get(admin = request.user.id )
    subject = Subject.objects.filter(classes = student.classes_id )
    action = request.GET.get('action')

    attendance_report=None
    get_subject =None
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            get_subject = Subject.objects.get(id = subject_id)

            attendance = Attendance.objects.get(subject_id=subject_id)
            attendance_report = Attendance_Report.objects.filter(student_id = student,attendance_id__subject_id = subject_id)


    context ={
        'subject':subject,
        'action':action,
        'get_subject':get_subject,
        'action':action,
        'attendance_report':attendance_report,
    }
    return render(request,'students/view_attendance.html',context)