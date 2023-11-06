from django.shortcuts import render,redirect,HttpResponse

from django.contrib.auth.decorators import login_required
from nssps.models import Teacher
from nssps.models import Classes,GALLERY
from nssps.models import Session_Year,CustomUser,Student,Subject
from django.contrib import messages

from django.views.decorators.cache import cache_control


@cache_control(no_cache=True, must_revalidate=True, no_store=True)

 





@login_required(login_url='/')
def HOME(request):
    return render(request,'principal/home.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)

@login_required(login_url='/')
def ADD_STUDENT(request):
    classes = Classes.objects.all()
    session_year = Session_Year.objects.all()

    if request.method == "POST":
         profile_pic = request.FILES.get('profile_pic')
         first_name = request.POST.get('first_name')
         last_name = request.POST.get('last_name')
         email = request.POST.get('email')
         username = request.POST.get('username')
         password = request.POST.get('password')
         address = request.POST.get('address')
         gender = request.POST.get('gender')
         dob = request.POST.get('dob')
         religion = request.POST.get('religion')
         mobile = request.POST.get('mobile')
         admission_number = request.POST.get('admission_number')
         classes_id = request.POST.get('classes_id')
         father_name = request.POST.get('father_name')
         father_occuption = request.POST.get('father_occuption')
         father_mobile = request.POST.get('father_mobile')
         mother_name = request.POST.get('mother_name')
         session_year_id = request.POST.get('session_year_id')

        # print(username,profile_pic,father_mobile,father_name,father_occuption,mother_name,session_year_id,first_name,last_name,email,password,gender,dob,classes_id,admission_number,mobile,religion,address)
         if CustomUser.objects.filter(email=email).exists():
             messages.warning(request,'Email is Alredy Register Please Use Another Email')
             return redirect('add_student')
         if CustomUser.objects.filter(username=username).exists():
             messages.warning(request,'username is Alredy Register Please Use Another username')
             return redirect('add_student')
         else:
             user = CustomUser(
                 first_name = first_name,
                 last_name = last_name,
                 username = username,
                 email = email,
                 profile_pic = profile_pic,
                 user_type = 3
             )
             user.set_password(password)
             user.save()
             
             classes = Classes.objects.get(id=classes_id)
             session_year = Session_Year.objects.get(id=session_year_id)

             student = Student(
                 admin = user,
                 address = address,
                 session_year_id = session_year,
                 classes_id = classes,
                 gender = gender,
                 DoB = dob,
                 religion = religion,
                 mobile = mobile,
                 admission_number = admission_number,
                 father_name = father_name,
                 father_mobile = father_mobile,
                 father_occuption = father_occuption,
                 mother_name = mother_name,
                 


             )
             student.save()
             messages.success(request, user.first_name + ' ' + user.last_name + ' ' 'are successfilly added !')
             return redirect('add_student')
              

    
    context = {
        'classes':classes,
        'session_year':session_year,
    }


    return render(request,'principal/add_student.html',context)








@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def VIEW_STUDENT(request):
    student = Student.objects.all()


    context ={
         'student':student,
        
        
     }
    return render(request,'principal/view_student.html',context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def EDIT_STUDENT(request,id):
    student = Student.objects.filter(id = id)
    classes = Classes.objects.all()
    session_year = Session_Year.objects.all()

    context ={
        'student':student,
        'classes':classes,
        'session_year':session_year,
         
    }


    return render(request,'principal/edit_student.html',context)



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def UPDATE_STUDENT(request):

    if request.method == "POST":
         student_id = request.POST.get('student_id')
          
         profile_pic = request.FILES.get('profile_pic')
         first_name = request.POST.get('first_name')
         last_name = request.POST.get('last_name')
         email = request.POST.get('email')
         username = request.POST.get('username')
         password = request.POST.get('password')
         address = request.POST.get('address')
         gender = request.POST.get('gender')
         dob = request.POST.get('dob')
         religion = request.POST.get('religion')
         mobile = request.POST.get('mobile')
         admission_number = request.POST.get('admission_number')
         classes_id = request.POST.get('classes_id')
         father_name = request.POST.get('father_name')
         father_occuption = request.POST.get('father_occuption')
         father_mobile = request.POST.get('father_mobile')
         mother_name = request.POST.get('mother_name')
         session_year_id = request.POST.get('session_year_id')

         user = CustomUser.objects.get(id=student_id)
          
         user.first_name = first_name
         user.last_name = last_name
         user.email = email
         user.username = username
          

         if profile_pic !=None and profile_pic !="":
            user.profile_pic = profile_pic
           
         if password !=None and password !="":
            user.set_password(password)
         user.save()

         student = Student.objects.get(admin=student_id)
         student.address = address
         student.gender = gender
         
          
         if dob!=None and dob !="":
            student.DoB = dob
         student.religion = religion
         student.mobile = mobile
         student.admission_number = admission_number
         student.father_name = father_name
         student.father_occuption = father_occuption
         student.father_mobile = father_mobile
         student.mother_name = mother_name
         


         classes = Classes.objects.get(id = classes_id)
         student.classes_id = classes

         session_year = Session_Year.objects.get(id=session_year_id)
         student.session_year_id = session_year

         student.save()

         messages.success(request,'Student Data Updated Successfilly !')
         return redirect('view_student')


    return render(request,'principal/edit_student.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def DELETE_STUDENT(request,admin):
    student = CustomUser.objects.get(id=admin)
    student.delete()
    messages.success(request,'Student is Successfilly Deleted !')

    return redirect('view_student')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def STUDENT_DETAIL(request,id):

    student = Student.objects.filter(id = id )


    context ={
      'student':student,
        
        
     }


    return render(request,'principal/student_detail.html',context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def ADD_CLASSES(request):

    if request.method == "POST":
        classes_name = request.POST.get('classes_name')
        
        classes = Classes(

            name = classes_name,
        )
        classes.save()
        messages.success(request, 'Class Add Successfully !')
        return redirect('add_classes')
    return render(request,'principal/add_classes.html')



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def VIEW_CLASSES(request):
    classes = Classes.objects.all()
    context = {

        'classes':classes,
    }

    return render(request,'principal/view_classes.html', context)



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def EDIT_CLASSES(request,id):
    classes = Classes.objects.get(id = id)

    context = {
        'classes':classes,
    }

    return render(request, 'principal/edit_classes.html',context) 



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def UPDATE_ClASSES(request):
    if request.method == "POST":
        name = request.POST.get('name')

        classes_id = request.POST.get('classes_id')

        classes = Classes.objects.get(id = classes_id)
        classes.name = name
        classes.save()
        messages.success(request,'Class is Successflly Updated !')
        return redirect('view_classes')

    return render(request, 'principal/edit_classes.html')



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def DELETE_CLASSES(request,id):
    classes = Classes.objects.get(id = id)
    classes.delete()
    messages.success(request,'Class is Successfully Deleted !')
    return redirect('view_classes')



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def ADD_SUBJECT(request):

    classes = Classes.objects.all()
    teacher = Teacher.objects.all()
    if request.method == "POST":
        subject_name = request.POST.get('subject_name')
        classes_id = request.POST.get('classes_id')
        teacher_id = request.POST.get('teacher_id')

        classes = Classes.objects.get(id = classes_id)
        teacher = Teacher.objects.get(id = teacher_id)


        subject = Subject(

          name =  subject_name,
          classes = classes,
          teacher = teacher,


        )

        subject.save()
        messages.success(request,'subject is Successflly Added !')
        return redirect('add_subject')

        

    context = {

        'classes':classes,
        'teacher':teacher,
    }


    return render(request,'principal/add_subject.html', context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def VIEW_SUBJECT(request):
     subject = Subject.objects.all()


     context ={
         'subject':subject,
        
        
      }

     return render(request,'principal/view_subject.html',context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def EDIT_SUBJECT(request,id):
    subject = Subject.objects.get(id = id)
    classes = Classes.objects.all()
    teacher = Teacher.objects.all()
    

    context ={
        'subject':subject,
        'classes':classes,
        'teacher':teacher,
         
         
    }


    return render(request,'principal/edit_subject.html',context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def UPDATE_SUBJECT(request):

    if request.method == "POST":
         subject_id = request.POST.get('subject_id')
         subject_name = request.POST.get('subject_name')
          
         
         teacher_id = request.POST.get('teacher_id')
         
         
         classes_id = request.POST.get('classes_id')
          

          
          

        

        # subject = Subject.objects.get(admin=subject_id)
         
         teacher = Teacher.objects.get(id=teacher_id)
          
         
         


         classes = Classes.objects.get(id = classes_id)
          
         subject = Subject (
             id = subject_id,
             name = subject_name,
             classes = classes,
             teacher = teacher,


         )

          

         subject.save()

         messages.success(request,'Subject Data Updated Successfilly !')
         return redirect('view_subject')


    return render(request,'principal/edit_subject.html')



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def DELETE_SUBJECT(request,id):
    subject = Subject.objects.get(id = id)
    subject.delete()
    messages.success(request,'Subject is Successfully Deleted !')
    return redirect('view_subject')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def ADD_SESSION(request):
    if request.method == 'POST':
     session_year_start = request.POST.get('session_year_start')
     session_year_end = request.POST.get('session_year_end')
     session = Session_Year(
         session_start = session_year_start,
         session_end = session_year_end,

     )
     session.save()
     messages.success(request,'Session Year is Successfully Created !' )
     return redirect('add_session')


    return render(request,'principal/add_session.html')



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def VIEW_SESSION(request):
 
     session = Session_Year.objects.all()


     context ={
         'session':session,
        
        
      }

     return render(request,'principal/view_session.html',context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def EDIT_SESSION(request,id):
    session = Session_Year.objects.filter(id = id)

    context = {
        'session':session,
    }

    return render(request,'principal/edit_session.html',context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def UPDATE_SESSION(request):
    if request.method == 'POST':
        session_id = request.POST.get('session_id')
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')


        session = Session_Year(
            id = session_id,
            session_start = session_year_start,
            session_end =  session_year_end,
        )
        session.save()
        messages.success(request,'Session is Successfully Updated !')
        return redirect('view_session')
    


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def DELETE_SESSION(request,id):
    session = Session_Year.objects.get(id = id)
    session.delete()
    messages.success(request,'Session is Success Deleted !')
    return redirect('view_session')


     




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def ADD_GALLERY(request):    
    if request.method == "POST":
         Gallery_image = request.FILES.get('Gallery_image')
         image_title = request.POST.get('image_title')

         

         gallery = GALLERY(

            image = Gallery_image,
            title = image_title,
         )
         gallery.save()
         messages.success(request, 'Image Add Successfully into Gallery !')
         return redirect('add_gallery')


          
    return render(request,'principal/add_gallery.html')



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def ADD_TEACHER(request):

    if request.method == "POST":
         profile_pic = request.FILES.get('profile_pic')
         first_name = request.POST.get('first_name')
         last_name = request.POST.get('last_name')
         email = request.POST.get('email')
         username = request.POST.get('username')
         password = request.POST.get('password')
         address = request.POST.get('address')
         gender = request.POST.get('gender')



         if CustomUser.objects.filter(email=email).exists():
             messages.warning(request,'Email is Alredy Register Please Use Another Email')
             return redirect('add_teacher')
         if CustomUser.objects.filter(username=username).exists():
             messages.warning(request,'username is Alredy Register Please Use Another username')
             return redirect('add_teacher')
         else:
             user = CustomUser(
                 first_name = first_name,
                 last_name = last_name,
                 username = username,
                 email = email,
                 profile_pic = profile_pic,
                 user_type = 2
             )
             user.set_password(password)
             user.save()
             teacher = Teacher(
                 admin = user,
                 address = address,
                  
                 gender = gender,

             )
             teacher.save()
             messages.success(request,'Teacher Added Successflly !')
             return redirect('add_teacher')

     
    return render(request,'principal/add_teacher.html')



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def VIEW_TEACHER(request):

    
    teacher = Teacher.objects.all()


    context ={
         'teacher':teacher,
        
        
     }
    
    return render(request,'principal/view_teacher.html',context)




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def EDIT_TEACHER(request,id):
    teacher = Teacher.objects.filter(id = id)
    

    context ={
        'teacher':teacher,
         
         
    }


    return render(request,'principal/edit_teacher.html',context)



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def UPDATE_TEACHER(request):

    if request.method == "POST":
         teacher_id = request.POST.get('teacher_id')
          
         profile_pic = request.FILES.get('profile_pic')
         first_name = request.POST.get('first_name')
         last_name = request.POST.get('last_name')
         email = request.POST.get('email')
         username = request.POST.get('username')
         password = request.POST.get('password')
         address = request.POST.get('address')
         gender = request.POST.get('gender')
         

         user = CustomUser.objects.get(id= teacher_id)
          
         user.first_name = first_name
         user.last_name = last_name
         user.email = email
         user.username = username
          

         if profile_pic !=None and profile_pic !="":
            user.profile_pic = profile_pic
           
         if password !=None and password !="":
            user.set_password(password)
         user.save()

         teacher = Teacher.objects.get(admin=teacher_id)
         teacher.address = address
         teacher.gender = gender
         
          
         
         


      
 
         teacher.save()

         messages.success(request,'Teacher Data Updated Successfilly !')
         return redirect('view_teacher')


    return render(request,'principal/edit_teacher.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def DELETE_TEACHER(request,admin):
    teacher = CustomUser.objects.get(id=admin)
    teacher.delete()
    messages.success(request,'Teacher is Successfilly Deleted !')

    return redirect('view_teacher')















 
 