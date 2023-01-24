from http.client import HTTPResponse
import json
from django.http import JsonResponse
from multiprocessing import context
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt

from member.models import Member

def logout(request):
    request.session.clear()
    return redirect('/')
    



def login(request):
    if request.method=='GET':
        print('get')
        return render(request,'login.html')
    else:
        id=request.POST.get('id')
        pw=request.POST.get('pw')
        print(id,pw)
        
        try: #등록된 아이디 인가? 확인
            qs=Member.objects.get(M_id=id,M_pw=pw)
            
        except Member.DoesNotExist:
            qs=None
            
        if qs: #qs의 값이 존재하면
            request.session['session_ID']=qs.M_id
            request.session['session_NAME']=qs.M_name
            return redirect('/')
        
        else:
    
            try: #등록된 아이디라도 있나? 확인
                qs=Member.objects.get(M_id=id)
                
            except Member.DoesNotExist:
                qs=None
            
            if qs:
                msg='패스워드가 일치하지 않습니다. 비밀번호를 다시 입력해주세요.'
                context={'msg':msg,'id':id}
                return render(request,'login.html',context)
            else:
                msg='아이디가 존재하지 않습니다. 아이디를 다시 입력해주세요.'
                context={'msg':msg}
                return render(request,'login.html',context)
                

        






def register(request):
    return render(request,'step01.html')

def register02(request):
    return render(request,'step02.html')

@csrf_exempt 
def check_id(request):
    print('hi')
    id = request.GET['id']
    print(id)
    # 데이터 프레임 -> json으로 보내야함
    # body = df.to_json() #컬럼을 기준으로 변환
    # body_json = {}
    # body_json['json_data'] = json.loads(id) # 한번더 가져와야함
    # print(body_json)
    try: #등록된 아이디라도 있나? 확인
        qs=Member.objects.get(M_id=id)
            
    except Member.DoesNotExist:
        qs=None
    
    if qs:
        msg='이미 존재하는 아이디 입니다. 다른 아이디를 입력해주세요.'
        context={'msg':msg}
        return JsonResponse(context,safe=False)
    else:
        msg='사용 가능한 아이디 입니다.'
        context={'msg':msg}
        return JsonResponse(context,safe=False)


     
    # json_data = json.loads(request) 
    # print('view post : ',json_data.get('name')) 
    # context = {'name': json_data.get('name'),'age':json_data.get('age')}
    

   
 
def register03(request):
    return render(request,'step03.html')
    #     try: #등록된 아이디가 있나? 확인
    #         qs=Member.objects.get(M_id=id)   
    #     except Member.DoesNotExist:
    #         qs=None
            
    #     if qs:
    #         msg='패스워드가 일치하지 않습니다. 비밀번호를 다시 입력해주세요.'
    #         context={'msg':msg,'id':id}
    #         return render(request,'login.html',context)
    #     else:
    #         msg='아이디가 존재하지 않습니다. 아이디를 다시 입력해주세요.'
    #         context={'msg':msg}
    #         return render(request,'login.html',context)
        
   
    
def register04(request):
    name=request.POST.get('name')
    id=request.POST.get('id')
    password=request.POST.get('password')
    email=request.POST.get('email')
    email02=request.POST.get('email02')
    email_tail=request.POST.get('email_tail')
    email_check=request.POST.get('email_check')
    address=request.POST.get('address')
    address02=request.POST.get('address02')
    sms=request.POST.get('sms')
    sms02=request.POST.get('sms02')
    sms03=request.POST.get('sms03')
    sms_check=request.POST.get('sms_check')
    year=request.POST.get('year')
    month=request.POST.get('month')
    date=request.POST.get('date')
    # print('name: ',name)
    # print('id: ',id)
    # print('password: ',password)
    # print('email: ',email)
    # print('email02: ',email02)
    # print('email_tail: ',email_tail)
    # print('address: ',address)
    # print('address02: ',address02)
    # print('email_check: ',email_check)
    # print('sms_check: ',sms_check)
    # print('sms: ',sms)
    # print('sms02: ',sms02)
    # print('sms03: ',sms03)
    # print('year: ',year)
    # print('month: ',month)
    # print('date: ',date)
    
    
    #email 재조합
    if email_tail=='#':
        email=email+'@'+email02
    else:
        email=email+'@'+email_tail
    
    #주소 재조합
    address=address+'/'+address02
    
    #전화번호 재조합
    sms=sms+'-'+sms02+'-'+sms03
    
    #생년월일 재조합
    # 포스트 데이터는 무조건 str형태로 들어오나 봄
    if (year!='#') and (month!='#')and (date!='#'):
        month=int(month)
        date=int(date)
        if month<10:
            month='0'+str(month)
        if date<10:
            date='0'+str(date)
        date_of_birth=str(year)+'/'+str(month)+'/'+str(date)
    else:
        date_of_birth='#/#/#'
        
        
    # print(email)
    # print(address)
    # print(sms)
    # print(date_of_birth)
    
    qs=Member(M_name=name, M_id=id, M_pw=password, M_email=email, M_address=address,\
        M_email_check=email_check, M_sms_check=sms_check, M_sms=sms, M_date_of_birth=date_of_birth)
    qs.save()
    
    return render(request,'step04.html')
    