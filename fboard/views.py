from audioop import reverse
from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from fboard.models import Fboard
from fboard.models import Lboard
from django.core.paginator import Paginator
from django.db.models import F
from django.http import JsonResponse


def f_modify(request, nowpage, f_No):
    if request.method == "GET":
        board = Fboard.objects.get(f_No=f_No)
        context = {"board": board, "nowpage": nowpage}
        return render(request, "comment_modify.html", context)

    else:
        board = Fboard.objects.get(f_No=f_No)
        title = request.POST.get("title")
        detail = request.POST.get("detail")
        board.f_Title = title
        board.f_Detail = detail
        board.save()
        return redirect("fboard:f_list", nowpage)


def f_list(request, nowpage):
    qs = Fboard.objects.order_by("-f_group", "f_step")
    paginator = Paginator(qs, 5)
    fList = paginator.get_page(nowpage)
    context = {"fList": fList, "nowpage": nowpage}  # 키값을 html에서 바로 사용가능 {%if fList%}
    return render(request, "comment_list.html", context)


# Create your views here.


def f_write(request, nowpage):
    if request.method == "POST":
        print(request)
        writer = request.session["session_ID"]
        title = request.POST.get("title")
        detail = request.POST.get("detail")
        # qs=Fboard.objects.create(f_Title=title,f_Detail=detail) qs를 이용할수가 없음.
        qs = Fboard(f_Title=title, f_Detail=detail, f_writer=writer)
        qs.save()
        qs.f_group = qs.f_No
        qs.save()
        # context={"nowpage":nowpage}
        return redirect("fboard:f_list", nowpage)

    else:
        context = {"nowpage": nowpage}
        return render(request, "comment_write.html", context)


def f_view(request, nowpage, f_No):
    qs = Fboard.objects.filter(f_No=f_No).update(f_hit=F("f_hit") + 1)
    f_board = Fboard.objects.get(f_No=f_No)
    allboard = Fboard.objects.order_by("-f_group", "f_step")
    print(allboard)
    print("int: ", allboard[0].f_No)
    print(type(allboard))

    if allboard[0].f_No == f_No:
        afterboard = allboard[1]
        context = {"f_board": f_board, "afterboard": afterboard, "nowpage": nowpage}
        return render(request, "comment_view.html", context)

    for i, board in enumerate(allboard):
        if board.f_No == f_No:
            beforeboard = allboard[i - 1]
            try:
                afterboard = allboard[i + 1]
            except:
                afterboard = None

            print(beforeboard)
            print(afterboard)
            print(f_No)
            context = {
                "f_board": f_board,
                "afterboard": afterboard,
                "beforeboard": beforeboard,
                "nowpage": nowpage,
            }
            return render(request, "comment_view.html", context)

        
    context = {"f_board": f_board, "nowpage": nowpage}
    return render(request, "comment_view.html", context)


def f_reply(request, nowpage, f_No):
    if request.method == "GET":
        f_board = Fboard.objects.get(f_No=f_No)
        context = {"nowpage": nowpage, "f_No": f_No, "f_board": f_board}
        return render(request, "comment_reply.html", context)  # render로 뺴낼때 dic타입만 전송가능
    else:
        writer = request.session["session_ID"]
        f_Title = request.POST.get("title")
        f_Detail = request.POST.get("detail")
        f_group = int(request.POST.get("f_group"))
        f_step = int(request.POST.get("f_step"))
        f_indent = int(request.POST.get("f_indent"))
        Fboard.objects.filter(f_group=f_group, f_step__gt=f_step).update(
            f_step=F("f_step") + 1
        )  # f_step =f_step 같은거 말고 더큰거
        qs = Fboard(
            f_writer=writer,
            f_Title=f_Title,
            f_Detail=f_Detail,
            f_group=f_group,
            f_step=f_step + 1,
            f_indent=f_indent + 1,
        )  # F()디비속의 값 가져오기
        qs.save()
        return redirect("fboard:f_list", nowpage)


def f_event(request):
    print("fevent")
    return render(request, "event_view.html")


def f_delete(request, nowpage, f_No):
    qs = Fboard.objects.get(f_No=f_No)
    qs.delete()
    return redirect("fboard:f_list", nowpage)


def low_comment(request):
    print("low")
    low_data = Lboard.objects.order_by("-L_No")
    low_data = list(low_data.values())
    return JsonResponse(low_data, safe=False)


def low_comment_write(request):
    title = request.GET.get("title")
    content = request.GET.get("content")
    qs = Lboard(L_Title=title, L_Detail=content)
    qs.save()
    low_data = Lboard.objects.order_by("-L_No")
    low_data = list(low_data.values())
    return JsonResponse(low_data, safe=False)  # dict만 전달 할래? 아니면 맘대로 보낼래
