from django.db import models


 
from django.contrib.auth.models import AbstractUser

# Create your models here.
class GALLERY(models.Model):
    title = models.CharField(max_length=70)
    image= models.ImageField(upload_to='galleray/image')


    def _str_(self):
        return self.title
    
#class Banner(models.Model):
   # title = models.CharField(max_length=70)
    #image= models.ImageField(upload_to='media/image')


  #  def _str_(self):
#        return self.title
    

class CustomUser(AbstractUser):
    USER =(
        (1,'PRINCIPAL'),
        (2,'TEACHER'),
        (3,'STUDENT'),
    )
    user_type = models.CharField(choices=USER,max_length=200,default=1)
    profile_pic=models.ImageField(upload_to='media/profile_pic')


class Classes(models.Model):
    name = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    

class Session_Year(models.Model):
    session_start = models.CharField(max_length=100)
    session_end = models.CharField(max_length=100)
    def __str__(self):
        return self.session_start + " - " + self.session_end



class Student(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)
   
    religion = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    admission_number = models.IntegerField()
    father_name = models.CharField(max_length=100)
    father_occuption = models.CharField(max_length=100)
    father_mobile = models.CharField(max_length=10)
    mother_name = models.CharField(max_length=100)
    DoB = models.DateField(max_length=12)
     
    classes_id = models.ForeignKey(Classes,on_delete=models.DO_NOTHING)
    session_year_id = models.ForeignKey(Session_Year,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name
    


class Teacher(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address = models.TextField()
     
    gender = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    
    

    def __str__(self):
        return self.admin.username
    



class Subject(models.Model):
     
    name = models.CharField(max_length=100)
    classes = models.ForeignKey(Classes,on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    subject_id = models.ForeignKey(Subject,on_delete=models.DO_NOTHING)
    attendance_date = models.DateField()
    session_year_id = models.ForeignKey(Session_Year,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject_id.name
    

class Attendance_Report(models.Model):
    student_id = models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    attendance_id = models.ForeignKey(Attendance,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.student_id.admin.first_name
    

 
    


    


