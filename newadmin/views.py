from http.client import HTTPResponse
from multiprocessing import context
from event.models import E_board
from home.models import TopImages
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.db.models import F
from event.views import event
from member.models import Member
from fboard.models import Fboard

#-------------------임시 페이지 이동 관리------------------------------#

def tabels(request):
    return render(request,'tables.html')

def admin(request):
    return render(request,'index.html')

def form(request):
    return render(request,'form.html')

#----------------main-----------------------------------_#

def main_list(request):
    board=TopImages.objects.order_by('T_no')
    context={'board':board}
    return render(request,'main_list.html',context)

def main_write(request):
    if request.method=="GET":
        return render(request,'main_write.html')
    else:
        main_no=int(request.POST.get('main_no'))
        main_title=request.POST.get('main_title')
        image=request.FILES.get('image')
        TopImages.objects.filter(T_no__gt=main_no-1).update(T_no=F('T_no')+1)
        qs = TopImages(T_no=main_no,T_image=image,T_title=main_title)
        qs.save()
        allno=TopImages.objects.order_by('T_no')
        for i,no in enumerate(allno):
            no.T_no = i + 1
            no.save()
        return redirect('newadmin:main_list')
    
def main_top_view(request,no):
    if request.method=="GET":
        board=TopImages.objects.get(T_no=no)
        context={'board':board,'no':no}
        return render(request,'main_top_view.html',context)
    else: #save
        main_no=int(request.POST.get('main_no')) #변경될 수도 있는 넘버
        main_title=request.POST.get('main_title')
        image=request.FILES.get('image',None)
        sub_image=request.POST.get('sub_image') 
        if image==None:
            image=sub_image
            
        qs=TopImages.objects.get(T_no=no) #db가져오기
        if no!=main_no: #변동 사항이 있다면?
            if no<main_no:
                TopImages.objects.filter(T_no__lte=main_no).update(T_no=F('T_no')-1)
            else:
                TopImages.objects.filter(T_no__gte=main_no).update(T_no=F('T_no')+1)
        qs.T_no=main_no
        qs.T_title=main_title
        qs.T_image=image
        qs.save()
        allno=TopImages.objects.order_by('T_no')
        for i,no in enumerate(allno):
            no.T_no=i+1
            no.save()
        return redirect('newadmin:main_list')
    
@csrf_exempt 
def main_multi_delete(request):
    
    no = request.GET['numbers']
    num_list=no.split(' ')
    if no:
        for i in num_list:
            qs=TopImages.objects.get(T_no=i)
            qs.delete()
        allno=TopImages.objects.order_by('T_no')
        for i,no in enumerate(allno):
            no.T_no=i+1
            no.save()
        return JsonResponse(safe=False)
    
def main_top_delete(request,no):
    
    return render(request,'main_top_view.html')
   
    
#----------------main끝-----------------------------------_#


#----------------------event 관리------------------------------#


def event_write(request):
    if request.method=='GET':
        return render(request,'event_write.html')
    else:
        #이미지는 테이블 속성 값으로 이미지 자체로 저장되어있는 것이 아닌 
        # '/media/이미지이름.png' 처럼 path가 저장된다.               
        event_no=int(request.POST.get('event_no'))
        progress=request.POST.get('progress')
        event_title=request.POST.get('event_title')
        event_content=request.POST.get('event_content')
        event_srart=request.POST.get('event_srart')
        event_end=request.POST.get('event_end')
        image=request.FILES.get('image')
        image02=request.FILES.get('image02')
        nowpage=1
        event_no=event_no
        
        #----------------------numbering--------------------------------
 
        if E_board.objects.exists():
            max_no=E_board.objects.latest('E_event_no').E_event_no
            if max_no<event_no:
                event_no=max_no+1
            else:
                E_board.objects.filter(E_event_no__gt=event_no-1).update(E_event_no=F('E_event_no')+1)
            qs = E_board(E_event_no=event_no,E_progress=progress,E_title=event_title,\
            E_content=event_content,E_start_day=event_srart,\
            E_end_day=event_end,E_image=image,E_image02=image02)
            qs.save()
            
        else:
            qs = E_board(E_event_no=event_no,E_progress=progress,E_title=event_title,\
            E_content=event_content,E_start_day=event_srart,\
            E_end_day=event_end,E_image=image,E_image02=image02)
            qs.save()
        
        #----------------------numbering end--------------------------------
      
        return redirect('newadmin:event_list',nowpage)
    

def event_list(request,nowpage):
    allno=E_board.objects.order_by('E_event_no')
    for i,no in enumerate(allno):
        no.E_event_no=i+1
        no.save()
    
    qs = E_board.objects.order_by('E_event_no')
    # 페이징 처리 - request:str타입
    # page = int(request.GET.get('nowpage',1)) # page변수 전달, 없으면 1
    paginator = Paginator(qs,100)     # 1페이지 나타낼수 있는 게시글 수 설정.  
    event_list = paginator.get_page(nowpage) # 요청한 페이지의 게시글 10개를 전달
    context={'event_list':event_list,'nowpage':nowpage}
    return render(request,'event_list.html',context)


def event_delete(request,nowpage,no):
    qs = E_board.objects.get(E_no=no)
    qs.delete()
    allno=E_board.objects.order_by('E_event_no')
    return redirect('newadmin:event_list',nowpage)

@csrf_exempt 
def event_multi_delete(request):

    no = request.GET['numbers']
    num_list=no.split(' ')
    if no:
        for i in num_list:
            qs=E_board.objects.get(E_no=i)
            qs.delete()
        return JsonResponse(safe=False)
    
def event_list_view(request,nowpage,event_no):
    if request.method=='GET':
        board=E_board.objects.get(E_no=event_no) #원래 넘버에서 보드 들고오기
        context={'nowpage':nowpage,'no':event_no,'board':board} 
        return render(request,'event_list_view.html',context)
    else:
        qs=E_board.objects.get(E_no=event_no) #고유 넘버에서 정보 가져오기
        event_progress=request.POST.get('event_progress')
        event_title=request.POST.get('event_title')
        event_content=request.POST.get('event_content')
        event_srart=request.POST.get('event_srart')
        event_end=request.POST.get('event_end')
        image=request.FILES.get('image',None)
        image02=request.FILES.get('image02',None)
        sub_image=request.POST.get('sub_image') 
        sub_image02=request.POST.get('sub_image02') 
        event_change_no=int(request.POST.get('event_no'))  #변경 됐을수도 있는 넘버

        if image==None:
            image=sub_image
        if image02==None:
            image02=sub_image02

        if event_change_no!=qs.E_event_no: #변경이 되었는가?
            if qs.E_event_no<event_change_no:
                E_board.objects.filter(E_event_no__lte=event_change_no).update(E_event_no=F('E_event_no')-1)
            else:
                E_board.objects.filter(E_event_no__gte=event_change_no).update(E_event_no=F('E_event_no')+1)

        qs.E_event_no=event_change_no
        qs.E_progress=event_progress
        qs.E_title=event_title
        qs.E_content=event_content
        qs.E_start_day=event_srart
        qs.E_end_day=event_end
        qs.E_image=image
        qs.E_image02=image02
        qs.save()
        
        allno=E_board.objects.order_by('E_event_no')
        for i,no in enumerate(allno):
            no.E_event_no=i+1
            no.save()       
        return redirect('newadmin:event_list',nowpage)
    

    #----------------------member 관리------------------------------#


def member_list(request,nowpage):
    qs = Member.objects.all()
    # 페이징 처리 - request:str타입
    # page = int(request.GET.get('nowpage',1)) # page변수 전달, 없으면 1
    paginator = Paginator(qs,100)     # 1페이지 나타낼수 있는 게시글 수 설정.  
    member_list = paginator.get_page(nowpage) # 요청한 페이지의 게시글 10개를 전달
    context={'member_list':member_list,'nowpage':nowpage}
    return render(request,'member_list.html',context)

@csrf_exempt 
def member_multi_delete(request):
    
    ids = request.GET['ids']
    id_list=ids.split(' ')
    if ids:
        for id in id_list:
            qs=Member.objects.get(M_id=id)
            qs.delete()
        return JsonResponse(safe=False)

def community_list(request,nowpage):
    qs = Fboard.objects.all()
    # 페이징 처리 - request:str타입
    # page = int(request.GET.get('nowpage',1)) # page변수 전달, 없으면 1
    paginator = Paginator(qs,100)     # 1페이지 나타낼수 있는 게시글 수 설정.  
    community_list = paginator.get_page(nowpage) # 요청한 페이지의 게시글 10개를 전달
    context={'community_list':community_list,'nowpage':nowpage}
    return render(request,'community_list.html',context)

@csrf_exempt 
def community_multi_delete(request):
    ids = request.GET['ids']
    id_list=ids.split(' ')
    if ids:
        for no in id_list:
            qs=Fboard.objects.get(f_No=no)
            qs.delete()
        return JsonResponse(safe=False)



