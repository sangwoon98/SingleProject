from http.client import HTTPResponse
import json
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from event.models import E_board, R_board
from django.core import serializers
from django.http import HttpResponse

def event(request,nowpage):
    qs = E_board.objects.order_by('-E_no')
    # 페이징 처리 - request:str타입
    # page = int(request.GET.get('nowpage',1)) # page변수 전달, 없으면 1
    paginator = Paginator(qs,100)     # 1페이지 나타낼수 있는 게시글 수 설정.  
    event_list = paginator.get_page(nowpage) # 요청한 페이지의 게시글 10개를 전달
    context={'event_list':event_list,'nowpage':nowpage}
    return render(request,'event.html',context)


   
# def event_view_previous(request,nowpage,no):
#     board=E_board.objects.get(E_no=no)
#     event_no=board.E_event_no
#     try:
#         qs=E_board.objects.get(E_no=event_no-1)
#     except E_board.DoesNotExist:
#         qs=None
#     if qs:
#         board=E_board.objects.get(E_event_no=event_no-1)
#         context={'nowpage':nowpage,'no':no,'board':board}
#         return render(request,'event_view.html',context)
#     else:
#         redirect('/')

# def event_view_next(request,nowpage,no):
#     board=E_board.objects.get(E_event_no=event_no)
#     event_no=board.E_event_no
#     try:
#         qs=E_board.objects.get(E_no=event_no+1)
#     except E_board.DoesNotExist:
#         qs=None
#     if qs:
#         board=E_board.objects.get(E_event_no=event_no+1)
#         context={'nowpage':nowpage,'no':no,'board':board}
#         return render(request,'event_view.html',context)
#     else:
#         redirect('/')
    
def event_view(request,nowpage,no):
    # if request.method=='GET':
    board=E_board.objects.get(E_event_no=no)
    if no==1:
        prevboard=None
        try:
            nextboard=E_board.objects.get(E_event_no=no+1)
        except E_board.DoesNotExist:
            nextboard=None
    
    else:
        prevboard=E_board.objects.get(E_event_no=no-1)
        try:
            nextboard=E_board.objects.get(E_event_no=no+1)
        except E_board.DoesNotExist:
            nextboard=None
            
    context={'nowpage':nowpage,'no':no,'board':board,'nextboard':nextboard,'prevboard':prevboard}
        
    return render(request,'event_view.html',context)

    # else:
    #     qs=E_board.objects.get(E_no=no)
    #     event_progress=request.POST.get('event_progress')
    #     event_title=request.POST.get('event_title')
    #     event_content=request.POST.get('event_content')
    #     event_srart=request.POST.get('event_srart')
    #     event_end=request.POST.get('event_end')
    #     image=request.FILES.get('image',None)
        
    #     print('progress: ',event_progress)
    #     print('event_content: ',event_content)
    #     print('event_title: ',event_title)
    #     print('event_srart: ',event_srart)
    #     print('event_end: ',event_end)
    #     print('image: ',image)
        
        
    #     # qs.E_progress=event_progress
    #     # qs.E_title=event_title
    #     # qs.E_content=event_content
    #     # qs.E_start_day=event_srart
    #     # qs.E_end_day=event_end
    #     # qs.E_image=image
    #     # qs.save()
    #     context={'nowpage':nowpage,'no':no,'board':board}
       
    #     return redirect('newadmin:event_list',context)
    
    
    



@csrf_exempt 
def event_reply_write(request,no):
    lowcontent = request.GET['lowcontent']
    
    if lowcontent:
        r_writer=request.session['session_ID']
        qs=R_board(R_writer=r_writer,R_content=lowcontent,R_e_no=no)
        qs.save()
        
    reply_list=R_board.objects.filter(R_e_no=no).order_by('-R_no')
    reply_list = json.loads(serializers.serialize("json",reply_list))  # serializers.serialize== queary셋을 list로 변경                  # json형태로 선언한뒤 conte
    context={'reply_list':reply_list}
    
    return JsonResponse(context)  

#수정
@csrf_exempt 
def event_reply_repair(request,no):
    lowcontent = request.GET['lowcontent']
    num = request.GET['num']
    text = request.GET['text']
    r_writer=request.session['session_ID']
    
    # 가져온 댓글의 원래 번호 가져오기
    
    qs=R_board.objects.order_by('-R_no')
    array=[]
    for i,q in enumerate(qs):
        array.append(int(q.R_no))
    num=array[int(num)]
    
    # 넘어올떄 계속 
    qs=R_board.objects.get(R_no=num)
    qs.R_e_no=no
    qs.R_content=text
    qs.R_writer=r_writer
    qs.save()
        
    reply_list=R_board.objects.filter(R_e_no=no).order_by('-R_no')
    reply_list = json.loads(serializers.serialize("json",reply_list))  # serializers.serialize== queary셋을 list로 변경                  # json형태로 선언한뒤 conte
    context={'reply_list':reply_list}
    
    return JsonResponse(context)  




def event_reply_delete(request,no):
    lowcontent = request.GET['lowcontent']
    num = request.GET['num']
    r_writer=request.session['session_ID']

    # 가져온 댓글의 원래 번호 가져오기
    qs=R_board.objects.order_by('-R_no')
    array=[]
    for i,q in enumerate(qs):
        array.append(int(q.R_no))
    num=array[int(num)]
    # 번호가져오기 끝
    
    # 넘어올떄 계속 
    qs=R_board.objects.get(R_no=num)
    qs.delete()
    # qs=R_board(R_writer=r_writer,R_content=lowcontent,R_e_no=no)
        
    reply_list=R_board.objects.filter(R_e_no=no).order_by('-R_no')
    reply_list = json.loads(serializers.serialize("json",reply_list))  # serializers.serialize== queary셋을 list로 변경                  # json형태로 선언한뒤 conte
    context={'reply_list':reply_list}
    
    return JsonResponse(context)  
    
    
    
#     R_no=models.AutoField(primary_key=True)
#     R_writer=models.CharField(max_length=100)
#     R_content=models.CharField(max_length=1000)
#     R_createdate =models.DateTimeField(default=datetime.now(),blank=True)
    
    