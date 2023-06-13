from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.conf import settings
from .models import User, Trainer
from .models import Board, Comment, CommentT
from .forms import CommentForm
from django.contrib import messages

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
                if user is not None:
                    request.session['userId'] = user.id
                    request.session['usertype'] = user.usertype
                    context['user'] = request.session['user']
                    context['usertype'] = request.session['usertype']
                return redirect('mysite:board_list')
                #return render(request, 'mysite/listing.html', context)

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
                    if trainer is not None:
                        request.session['userId'] = trainer.id
                        request.session['usertype'] = trainer.usertype
                        context['user'] = request.session['user']
                        context['usertype'] = request.session['usertype']
                    return redirect('mysite:board_list')
                    #return render(request, 'mysite/listing.html', context)

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

            return redirect('mysite:login')
        
        elif request.POST['type'] == "trainer":
            Trainer.objects.create(username = request.POST['username'], useremail = request.POST['useremail'],  password = request.POST['password'])

            return redirect('mysite:login')


def signout(request):
    if request.session.get('user'):
        del(request.session['user'])
    logout(request)
    return redirect('mysite:index')

def listing(request):
    return redirect('mysite:board_list')

def page(request):
    post_list = Board.objects.order_by('-create_date')
    paginator = Paginator(post_list, 10)
    page_obj = paginator.get_page(page)
    context = {'post_list': page_obj}
    return render(request, 'mysite/listing.html', context)


def postView(request, pk):
    try:
        board = get_object_or_404(Board, pk=pk)
        usertype = request.session.get('usertype')
        if(usertype=='user'):
            comments = CommentForm()
        if(usertype=='trainer'):
            comments = CommentTForm()

        comment_view = Comment.objects.filter(post=pk)
        commentT_view = CommentT.objects.filter(post=pk)

    except Board.DoesNotExist:
        raise Http404("Does not exist!")
    return render(request, 'mysite/postView.html', {'board':board, 'comments':comments, 'comment_view':comment_view})

def postWrite(request):
    boards = Board.objects.all()
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        video = request.FILES.get('files',None)

        usertype = request.session.get('usertype')

        if usertype == 'trainer':
            messages.warning(request, "권한이 없습니다.")
            return render(request,'mysite/postWrite.html')

        if usertype == 'user':
            user_id = request.session.get('userId')
            user = User.objects.get(pk=user_id)
            board = Board.objects.create(
                subject=subject,
                message=message,
                writer=user,
                file=video,
            )

            board.save()

        return redirect('mysite:board_list')

    return render(request,'mysite/postWrite.html',{'boards':boards})

def board_list(request):
    boards = Board.objects.all().order_by('-id')
    return render(request,'mysite/listing.html',{"boards":boards})

def comment_write(request, board_id):
    board = get_object_or_404(Board, pk=board_id)

    usertype = request.session.get('usertype')

    if(usertype == 'user'):
        user_id = request.session.get('userId')
        user = User.objects.get(pk=user_id)
    # 댓글 생성하는 로직
        comment_write = CommentForm(request.POST)
        if comment_write.is_valid():
            comments = comment_write.save(commit=False)
            comments.post = board
            comments.author = user
            comments.save()

    if(usertype == 'trainer'):
        user_id = request.session.get('userId')
        user = Trainer.objects.get(pk=user_id)

        comment_write = CommentTForm(request.POST)
        if comment_write.is_valid():
            comments = comment_write.save(commit=False)
            comments.post = board
            comments.author = user
            comments.save()
    return redirect('mysite:postView', board_id)
