from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreatView, AccountDetailView

app_name = "accountapp"

urlpatterns = [
    # 함수형 베이스 중간에 hello world
    path('hello_world/', hello_world, name="hello_world"),

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # 클래스 베이스는 다름
    path('create/', AccountCreatView.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),

]