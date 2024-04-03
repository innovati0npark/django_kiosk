#kiosk_cafe 폴더에 urls.py가 없어서 새로 생성

from django.urls import path

from . import views

app_name = "kiosk_cafe"

urlpatterns =[
    path("", views.main, name='kiosk_cafe')
]