from django.urls import path

from . import views

app_name='mysite'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('listing/', views.listing, name='listing'),
    path('postView/', views.postView, name='postView'),
    path('postWrite/', views.postWrite, name='postWrite'),
    path('board_list/', views.board_list, name='board_list'),
    path('postView/<int:pk>', views.postView, name='postView'),
    path('comment_write/<int:board_id>', views.comment_write, name='comment_write'),
]
