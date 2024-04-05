#kiosk_cafe 폴더에 urls.py가 없어서 새로 생성

from django.urls import path

from . import views

app_name = "kiosk_cafe"

urlpatterns =[
    path("", views.IndexView.as_view(), name='index'),
    path("<int:pk>/", views.DetailView.as_view(), name="detail")
]