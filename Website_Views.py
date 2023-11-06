from django.shortcuts import render,redirect,HttpResponse
from nssps.models import GALLERY,Teacher

def WEB(request):
    #teacher = Teacher.objects.all()


    # context = {
        # 'teacher':teacher,
        
        
        # }

     return render(request,'index.html',)

# Create your views here.
def gallery(request):
    images = GALLERY.objects.all()

    context = {
        'images':images,
     }
    return render(request, 'gallery/image_gallery.html', context)

