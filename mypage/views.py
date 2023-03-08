
from email.headerregistry import Address
import json
from tkinter import N
from django.shortcuts import render,redirect
from member.models import Member

def coupon(request):
    return render(request,'coupon.html')

def mypage(request):
    return render(request,'ordercheck.html')

def pw_change(request):
    if request.method=='GET': 
        return render(request,'password_change.html')
    else:
        id=request.session['session_ID']
        qs=Member.objects.get(M_id=id)
        
        M_pw=qs.M_pw
        now_pw=request.POST.get('now_pw')
        new_pw=request.POST.get('new_pw')
        new_pw_re=request.POST.get('new_pw_re')

        if M_pw==now_pw:    # pw 가 일치할떼
            if new_pw==new_pw_re:  
                qs.M_pw=new_pw
                qs.save()
                context={'msg1':'비밀번호가 변경되었습니다.'}
                return render(request,'password_change.html',context)
                #변경 저장후 리턴
            else:
                context={'msg2':'새로운 비밀번호 재입력이 일치하지 않습니다.'}
                return render(request,'password_change.html',context)
                
            
        else:
            context={'msg2':'비밀번호가 존재하지 않습니다.'}
            return render(request,'password_change.html',context)
                
            
            



def change(request):
    
    if request.method=='POST':

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
        name=request.session['session_NAME']
        id=request.session['session_ID']
    
        
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
        
        # 삽입
        qs=Member.objects.get(M_id=id)
        qs.M_email=email
        qs.M_email_check=email_check
        qs.M_address=address
        qs.M_sms=sms
        qs.M_sms_check=sms_check
        qs.M_date_of_birth=date_of_birth
        qs.save()
        
        request.session['session_ID']=qs.M_id
        request.session['session_NAME']=qs.M_name

        return redirect('mypage:mypage')
       
        
    else:
        M_id=request.session['session_ID']
        qs=Member.objects.get(M_id=M_id)
        email_check=(qs.M_email_check)
        sms_check=(qs.M_sms_check)
        
        email=qs.M_email.split('@')
        email0=email[0]
        email1=email[1]
        
        address=qs.M_address.split('/')
        address0=address[0]
        address1=address[1]
        
        sms=qs.M_sms.split('-')
        sms0=sms[0]
        sms1=sms[1]
        sms2=sms[2]
        
        date_of_birth=qs.M_date_of_birth.split('/')
        year=date_of_birth[0]
        
        if date_of_birth[1][0]=='0':
            month=date_of_birth[1][1]
        else:
            month=date_of_birth[1][0:2]
        
        month=date_of_birth[1]
        
        if date_of_birth[2][0]=='0':
            date=date_of_birth[1][1]
        else:
            date=date_of_birth[2][0:2]
        date=date_of_birth[2]
        
        context={'email_check':email_check,'sms_check':sms_check,'email0':email0,'email1':email1,'address0':address0,\
            'address1':address1,'sms0':sms0,'sms1':sms1,'sms2':sms2,'year':year,'month':month,'date':date}
        
        return render(request,'change_info.html',context)

def get_leave(request):
    if request.method=='GET':  
        return render(request,'get_leave.html')
    else:
        re_id=request.session.get('session_ID')
        id=request.POST.get('id')
        pw=request.POST.get('pw')
        
        if re_id!=id:
            context={'msg2':'본인의 계정이 아닙니다. 삭제가 불가능 합니다.'}
            return render(request,'get_leave.html',context)
            
        
        try:
            qs=Member.objects.get(M_id=id,M_pw=pw)
           
        except Member.DoesNotExist:
            qs=None
        
        if qs:
            qs.delete()
            request.session.clear()
            context={'msg':'그동안 저희 서비스를 이용해 주셔서 감사합니다. 안녕히 가십시오.'}
            return render(request,'get_leave.html',context)
        else:
            context={'msg2':'비밀번호가 잘못입력되었습니다. 다시 입력해주세요.','re_id':id}
            return render(request,'get_leave.html',context)

        