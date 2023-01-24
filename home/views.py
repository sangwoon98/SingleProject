from django.shortcuts import render
from home.models import TopImages

def home(request):
    Tops=TopImages.objects.order_by('T_no')
    print(Tops[0].T_image.url)
    context={'image01':Tops[0].T_image.url,'image02':Tops[1].T_image.url,\
        'image03':Tops[2].T_image.url,'image04':Tops[3].T_image.url,}
    return render(request,'main.html',context)
    
def top(request):
    return render(request,'main.html')
    