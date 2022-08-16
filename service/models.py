from django.db import models
from home.models import OverwriteStorage


# Create your models here.
class Service(models.Model):
    title = models.CharField('標題', max_length=50)
    content=models.TextField("內容", max_length=200,blank=True)
    pic_url = models.ImageField("照片",storage=OverwriteStorage(),upload_to='Service/service_image',blank=True)
    def __str__(self):
        return self.title

class Experience(models.Model):
    title = models.CharField('標題', max_length=50)
    content=models.TextField("內容", max_length=200,blank=True)
    pic_url = models.ImageField("照片",storage=OverwriteStorage(),upload_to='Service/experience_image',blank=True)
    def __str__(self):
        return self.title

class Service_Title(models.Model):
    name = models.CharField('公司名稱', max_length=50)
    logo= models.ImageField("公司logo",storage=OverwriteStorage(),upload_to='',blank=True)
    title1 = models.CharField('主題名稱1', max_length=50)
    title2 = models.CharField('主題名稱2', max_length=50)
    bottom_title=models.CharField('底部標題', max_length=20,blank=True)
    bottom_content=models.TextField('底部內容', max_length=300,blank=True)
    bottom_email=models.CharField('底部email', max_length=100,blank=True)
    bottom_phone=models.CharField('底部連絡電話', max_length=50,blank=True)
    def __str__(self):
        return self.name