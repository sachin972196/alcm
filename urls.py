"""
URL configuration for ns_automation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static  import static
from django.conf import settings

from .import views,Principal_Views,Teacher_Views,Student_Views,Website_Views

urlpatterns = [
    path('admin/', admin.site.urls),


     path('base/', views.BASE,name="BASE"),

    path('login/', views.LOGIN,name="login"),

    path('doLogin/', views.doLogin,name="doLogin"),

    path('doLogout/', views.dologout,name='logout'),

     #profile
    path('profile', views.PROFILE,name='profile'),

    path('profile/update/', views.PROFILE_UPDATE,name='profile_update'),
 







    #this is principal pannel url

    path('principal/Home/', Principal_Views.HOME,name="principal_home"),
    
    path('principal/Student/Add', Principal_Views.ADD_STUDENT,name="add_student"),

    path('principal/Student/View', Principal_Views.VIEW_STUDENT,name="view_student"),

    path('principal/Student/Edit/<str:id>', Principal_Views.EDIT_STUDENT,name="edit_student"),

    path('principal/Student/Update', Principal_Views.UPDATE_STUDENT,name="update_student"),

    path('principal/Student/Delete<str:admin>', Principal_Views.DELETE_STUDENT,name="delete_student"),

    path('principal/Student/View/Detail/<str:id>', Principal_Views.STUDENT_DETAIL,name="student_detail"),



    path('principal/Teacher/Add', Principal_Views.ADD_TEACHER,name="add_teacher"),
    path('principal/Teacher/View', Principal_Views.VIEW_TEACHER,name="view_teacher"),
    path('principal/Teacher/Edit/<str:id>', Principal_Views.EDIT_TEACHER,name="edit_teacher"),
    path('principal/Teacher/Update', Principal_Views.UPDATE_TEACHER,name="update_teacher"),
    path('principal/Teacher/Delete<str:admin>', Principal_Views.DELETE_TEACHER,name="delete_teacher"),
    
    
    path('principal/Classes/Add', Principal_Views.ADD_CLASSES,name="add_classes"),
    path('principal/Classes/View', Principal_Views.VIEW_CLASSES,name="view_classes"),

    path('principal/Classes/Edit/<str:id>', Principal_Views.EDIT_CLASSES,name="edit_classes"),
    path('principal/Classes/Update', Principal_Views.UPDATE_ClASSES,name="update_classes"),
    path('principal/Classes/Delete<str:id>', Principal_Views.DELETE_CLASSES,name="delete_classes"),    
    



    path('principal/Subject/Add', Principal_Views.ADD_SUBJECT,name="add_subject"),
    path('principal/Subject/View', Principal_Views.VIEW_SUBJECT,name="view_subject"),
    path('principal/Subject/Edit/<str:id>', Principal_Views.EDIT_SUBJECT,name="edit_subject"),
    path('principal/Subject/Update', Principal_Views.UPDATE_SUBJECT,name="update_subject"),
    path('principal/Subject/Delete<str:id>', Principal_Views.DELETE_SUBJECT,name="delete_subject"),    
    
    

    path('principal/Session/Add', Principal_Views.ADD_SESSION,name="add_session"),
    path('principal/Session/View', Principal_Views.VIEW_SESSION,name="view_session"),
    path('principal/Session/Edit/<str:id>', Principal_Views.EDIT_SESSION,name="edit_session"),
    path('principal/Session/Update', Principal_Views.UPDATE_SESSION,name="update_session"),
    path('principal/Session/Delete<str:id>', Principal_Views.DELETE_SESSION,name="delete_session"),
 
  #GAllery Path

   path('principal/Gallery/Add', Principal_Views.ADD_GALLERY,name="add_gallery"),
   path('', Website_Views.WEB,name='website'),
   path('gallery/image_gallery', Website_Views.gallery,name='image_gallery'),



   # this Teacher url
    path('teacher/Home', Teacher_Views.HOME,name="teacher_home"),
    path('teacher/Take_Attendance', Teacher_Views.TAKE_ATTENDANCE,name="take_attendance"),
    path('teacher/Save_Attendance', Teacher_Views.SAVE_ATTENDANCE,name="save_attendance"),
    path('teacher/View_Attendance', Teacher_Views.TEACHER_VIEW_ATTENDANCE,name="teacher_view_attendance"),
   




     # this Student url
    path('student/Home', Student_Views.HOME,name="student_home"),

    path('student/View_Attendance', Student_Views.SUTDENT_VIEW_ATTENDANCE,name="student_view_attendace"),
    

     
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
