from django.db import models
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your models here.
class OverwriteStorage(FileSystemStorage):
    #overwrite same filename image 
    # need to change storage.py: 
    # name = self.get_available_name(name, max_length=max_length) --> name = self.get_available_name(name)
    def get_available_name(self, name):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


class HomePage(models.Model):
    name = models.CharField('公司名稱', max_length=20)
    logo= models.ImageField("公司logo",storage=OverwriteStorage(),upload_to='',blank=True)
    big_pic_url1 = models.ImageField("圖片1 URL",storage=OverwriteStorage(),upload_to='home_image/',blank=True)
    big_pic_url2 = models.ImageField("圖片2 URL",storage=OverwriteStorage(),upload_to='home_image/',blank=True)
    big_pic_url3 = models.ImageField("圖片3 URL",storage=OverwriteStorage(),upload_to='home_image/',blank=True)
    title = models.CharField('標題', max_length=20)
    title_content=models.TextField('標題內容', max_length=200)
    sub_title1=models.CharField('子標題1', max_length=50,blank=True)
    sub_title2=models.CharField('子標題2', max_length=50,blank=True)
    sub_title3=models.CharField('子標題3', max_length=50,blank=True)
    sub_title4=models.CharField('子標題4', max_length=50,blank=True)
    pic_url1 = models.ImageField("子標題圖片1 URL",storage=OverwriteStorage(),upload_to='home_image/',blank=True)
    pic_url2 = models.ImageField("子標題圖片2 URL",storage=OverwriteStorage(),upload_to='home_image/',blank=True)
    pic_url3 = models.ImageField("子標題圖片3 URL",storage=OverwriteStorage(),upload_to='home_image/',blank=True)
    pic_url4 = models.ImageField("子標題圖片4 URL",storage=OverwriteStorage(),upload_to='home_image/',blank=True)
    bottom_title=models.CharField('底部標題', max_length=20,blank=True)
    bottom_content=models.TextField('底部內容', max_length=300,blank=True)
    bottom_email=models.CharField('底部email', max_length=100,blank=True)
    bottom_phone=models.CharField('底部連絡電話', max_length=50,blank=True)
    def __str__(self):
        return self.name

class HomePage_EN(models.Model):
    name = models.CharField('公司名稱', max_length=50)
    title = models.CharField('標題', max_length=50)
    title_content=models.TextField('標題內容', max_length=400)
    sub_title1=models.CharField('子標題1', max_length=50,blank=True)
    sub_title2=models.CharField('子標題2', max_length=50,blank=True)
    sub_title3=models.CharField('子標題3', max_length=50,blank=True)
    sub_title4=models.CharField('子標題4', max_length=50,blank=True)
    bottom_title=models.CharField('底部標題', max_length=20,blank=True)
    bottom_content=models.TextField('底部內容', max_length=400,blank=True)
    bottom_email=models.CharField('底部email', max_length=100,blank=True)
    bottom_phone=models.CharField('底部連絡電話', max_length=50,blank=True)
    def __str__(self):
        return self.name
