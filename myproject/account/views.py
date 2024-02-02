# views.py
from django.http import HttpResponse
from django. shortcuts import render
from datetime import datetime

from django.shortcuts import render


#Create your views here.
def money(request):
    context ={"name" : "홍길동", "age" : 40, 'current_time': datetime.now()}
    # render(request,"템플릿 이름", 전달할 데이터(dict 형태))
    return render(request,  'base.html',context)

def test(request):
    context ={"name" : "홍길동", "age" : 40}
    # render(request,"템플릿 이름", 전달할 데이터(dict 형태))
    return render(request,  'base.html',context)

def base(request):
    context ={"name" : "홍길동", "age" : 40}
    # render(request,"템플릿 이름", 전달할 데이터(dict 형태))
    return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")

def index(request):
    context ={"name" : "홍길동", "age" : 40}
    # render(request,"템플릿 이름", 전달할 데이터(dict 형태))
    return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")

def home(request):
    context = {
        "name": "홍길동",
        "age": 30,
        "time" : datetime.now()
    }
    return render(request,  'test.html',context)
#
#
# def ass(request,first,second):
#     context = {
#         "name": "홍길동",
#         "age": 30,
#         "time" : datetime.now(),
#         "hap": first+second
#     }
#     return render(request,  'test1.html',context)
#
# def home1(request,first: int, second=100):
#     context = {
#         "name": "홍길동",
#         "age": 30
#     }
#     date = "짝수" if datetime.datetime.now().day % 2 == 0 else "홀수"
#     context["date"] = date
#     return render(request,  'test1.html',context)


# gugudan = []
# bun = datetime.datetime.now()
# for i in range(2, 10, 1):
#     if bun % (i % 2) == 0:
#         gugudan.append((i, j, i * j))
#     else:
#         gugudan.append((i, j, i * j))
#     print(gugudan)
# "   context["gugudan"] = gugudan
#     return render(request, "index.html", context



# Create your views here.

# def homepage(request):
#     current_time = datetime.datetime.now()  # 현재 날짜 구하기
#     context = {
#         'comma': 50000,
#         'word': 180000000000,
#         'current_time': current_time,
#         "number1": 10,
#         "number2": 1,
#         "yesterday": current_time - datetime.timedelta(days=1),
#         "tomorrow": current_time + datetime.timedelta(days=1),
#     }
#     return render(request, 'human.html', context)