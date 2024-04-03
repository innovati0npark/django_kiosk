from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=100)  # 메뉴 이름
    price = models.IntegerField(default=0)  # 메뉴 가격
    description = models.TextField(blank=True)  # 설명
    category = models.CharField(max_length=50)  # 카테고리
    

    def __str__(self):
        return self.name
    

class Order(models.Model):
    order_number = models.CharField(max_length=20)  # 주문 번호
    menus = models.ManyToManyField(Menu)  # 주문한 메뉴 목록
    order_time = models.DateTimeField(auto_now_add=True)  # 주문 시간
    total_price = models.IntegerField()  # 총 금액

    def __str__(self):
        return self.order_number


class Manage(models.Model):
    date = models.DateField()  # 날짜
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)  # 메뉴 (Menu 모델과 연결)
    sales = models.IntegerField()  # 해당 메뉴의 매출액

    def __str__(self):
        return f"{self.date} - {self.menu.name}"