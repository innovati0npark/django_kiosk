from django.db import models
# Create your models here.

class Menu(models.Model):
    menu_name = models.CharField(max_length=100)  # 메뉴 이름
    menu_price = models.IntegerField(default=0)  # 메뉴 가격
    description = models.TextField(blank=True)  # 메뉴 설명
    category = models.CharField(max_length=50)  # 카테고리
    
    def __str__(self):
        return self.menu_name
    

class Order(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    order_time = models.DateTimeField(auto_now_add=True)  # 주문 시간
    total_price = models.IntegerField()  # 총 금액


class Customer(models.Model):
    contact = models.CharField(max_length=50)
    nickname = models.CharField(max_length=100)
    order_num = models.ForeignKey(Order, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nickname