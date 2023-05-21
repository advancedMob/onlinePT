from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import User, Trainer
from .models import Post, Reply

# Create your views here.


def index(request):

    return render(request, 'mysite/index.html')

def login(request):
    return render(request, 'mysite/login.html')


def signin(request):
    if request.method == "POST":
        # 비정상적인 제출
        useremail = request.POST.get('useremail', '')
        password = request.POST.get('password', '')
        if not useremail or not password:
            context = {
                'error': '공란 없이 입력해주십시오!',
            }
            return render(request, 'mysite/login.html', context)
        
        #  user 진위여부 확인
        try:
            user = User.objects.get(useremail=useremail)
            if user.password != password:
                context = {
                    'error': '비밀번호를 다시 확인해주세요!',
                }
                return render(request, 'mysite/login.html', context)
            else:
                context = {
                    'user': user,
                }
                print("hi user")
                return render(request, 'mysite/listing.html', context)

        except User.DoesNotExist:
            try:
                trainer = Trainer.objects.get(useremail=useremail)
                if trainer.password != password:
                    context = {
                        'error': '비밀번호를 다시 확인해주세요!',
                    }
                    return render(request, 'mysite/login.html', context)
                else:
                    context = {
                        'user': trainer,
                    }
                    print("hi trainer")
                    return render(request, 'mysite/listing.html', context)

            except Trainer.DoesNotExist:
                # JavaScript로 경고창을 표시하기 위해 HttpResponse 객체를 반환
                context = {
                    'error': "해당 아이디 미존재!"
                }
                return render(request, 'mysite/login.html', context)

        

def signup(request):
    # 중복 이메일 검사 -> 이메일이 중복되는걸 허용하면 signin에서 user과 trainer 신분이 중복될 수 있어서 사전에 방지한다.
    print(User.objects.filter(useremail=request.POST['useremail']).exists())
    print(Trainer.objects.filter(useremail=request.POST['useremail']).exists())
    if User.objects.filter(useremail=request.POST['useremail']).exists() or Trainer.objects.filter(useremail=request.POST['useremail']).exists():
        print("해당 이메일로 가입된 아이디가 존재합니다!")
        context = {
            'error': "해당 이메일로 가입된 아이디가 존재합니다!"
        }
        return render(request, 'mysite/login.html', context)

    if request.method == "POST":
        if request.POST['type'] == "user":
            User.objects.create(username = request.POST['username'], useremail = request.POST['useremail'],  password = request.POST['password'])
            
            return redirect('mysite:listing')
        
        elif request.POST['type'] == "trainer":
            Trainer.objects.create(username = request.POST['username'], useremail = request.POST['useremail'],  password = request.POST['password'])
            
            return redirect('mysite:listing')


def signout(request):
    logout(request)
    return redirect('mysite:index')

def listing(request):
    return render(request, 'mysite/listing.html')

def page(request):
    post_list = Post.objects.order_by('-create_date')
    paginator = Paginator(post_list, 10)
    page_obj = paginator.get_page(page)
    context = {'post_list': page_obj}
    return render(request, 'mysite/listing.html', context)


def postView(request):
    return render(request, 'mysite/postView.html')

def postWrite(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']

        user = User.objects.first()

        post = Post.objects.create(
            subject=subject,
            message=message,
            writer=user
        )

        post = Reply.objects.create(
            message=message,
            created_by=user
        )

        return redirect('mysite:listing')

    return render(request,'mysite/postWrite.html',{'posts':posts})

def post_list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request,'mysite/listing.html',{"posts":posts})