from django.urls import path

from accountapp.views import hello_world, AccountCreatView

app_name = "accountapp"

urlpatterns = [
    # 함수형 베이스 중간에 hello world
    path('hello_world/', hello_world, name="hello_world"),

    # 클래스 베이스는 다름
    path('create/', AccountCreatView.as_view(), name='create'),
]