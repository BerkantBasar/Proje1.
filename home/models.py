from django.db import models
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import  RichTextUploadingField
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.models import User
from product.models import Course
from django.urls import reverse
from django.contrib.auth.decorators import login_required



class Setting(models.Model): 
    STATUS=(
        ('True','Evet'),
        ('False','Hayir'),
    ) 
    title=models.CharField(max_length=150) 
    description=models.CharField(blank=True,max_length=255)
    keywords=models.CharField(blank=True,max_length=255)
    company=models.CharField(max_length=50)
    icon=models.ImageField(blank=True,upload_to='images/')
    logo=models.ImageField(blank=True,upload_to='images/')

    adress=models.CharField(blank=True,max_length=255)
    phone=models.CharField(blank=True,max_length=15)
    fax=models.CharField(blank=True,max_length=15)
    email=models.CharField(blank=True,max_length=50)

    smtpserver=models.CharField(max_length=20)
    smtpemail=models.CharField(max_length=20)
    smtppassword=models.CharField(max_length=10)
    smtpport=models.CharField(max_length=5)

    facebook=models.CharField(blank=True,max_length=150)
    pinterest=models.CharField(blank=True,max_length=150)
    instagram=models.CharField(blank=True,max_length=50)
    twitter=models.CharField(blank=True,max_length=50)
    linkedin=models.CharField(blank=True,max_length=50)

    aboutus=RichTextUploadingField(blank=True,)
    contact=RichTextUploadingField(blank=True,)
    references=RichTextUploadingField(blank=True,)
    
    status=models.CharField(max_length=10,choices=STATUS)
    crate_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title  


class ContactFormMessage(models.Model): 
    STATUS=(
        ('Okundu','Okundu'),
        ('Okunmadı','Okunmadı'),
        ('Çözüldü','Çözüldü'),
    ) 
    name=models.CharField(max_length=150) 
    email=models.CharField(blank=True,max_length=50)
    phone=models.CharField(blank=True,max_length=15)
    subject=models.CharField(blank=True,max_length=50)
    message=models.CharField(blank=True,max_length=255)
    status=models.CharField(max_length=10,choices=STATUS,default='New')
    ip=models.CharField(blank=True,max_length=20)
    note=models.CharField(blank=True,max_length=100)
    crate_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 

class ContactFormu(ModelForm): 
   class Meta:
    model=ContactFormMessage
    fields=['name','email','phone','subject','message',]
    widgets={
        'name':TextInput(attrs={'class': 'stext-111 cl2 plh3 size-116 p-l-62 p-r-30','placeholder':'Adınız & Soyadınız'}),
        'subject': TextInput(attrs={'class':'stext-111 cl2 plh3 size-116 p-l-62 p-r-30','placeholder':'Konu'}),
        'email':TextInput(attrs={'class': 'stext-111 cl2 plh3 size-116 p-l-62 p-r-30','placeholder':'Email Adresiniz'}),
        'phone':TextInput(attrs={'class': 'stext-111 cl2 plh3 size-116 p-l-62 p-r-30','placeholder':'Telefonunuz'}),
        'message':TextInput(attrs={'class': 'stext-111 cl2 plh3 size-116 p-l-62 p-r-30','placeholder':'Mesajınız','rows':'5'}),
    }

class Comment(models.Model): 
    STATUS=(
        ('New','Yeni'),
        ('True','Evet'),
        ('False','Hayır'),
    ) 
    product=models.ForeignKey(Course,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(blank=True,max_length=50)
    comment=models.CharField(blank=True,max_length=255)
    status=models.CharField(max_length=10,choices=STATUS,default='New',blank=True)
    ip=models.CharField(blank=True,max_length=20)
    crate_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.subject 
      
class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields=['subject','comment']


class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(blank=True,max_length=15)
    adress=models.CharField(blank=True,max_length=150)
    city=models.CharField(blank=True,max_length=50)
    country=models.CharField(blank=True,max_length=50)
    image=models.ImageField(blank=True,upload_to='images/userProfile')
    

    def __str__(self):
        return self.user.first_name+' '+self.user.last_name
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image' 

class UserProfileForm(ModelForm):
    class Meta:
        model=UserProfile
        fields=['phone','adress','city','country','image']

class FAQ(models.Model): 
    STATUS=(
        ('True','Evet'),
        ('False','Hayir'),
    ) 
    
    question=models.CharField(blank=True,max_length=255)
    answer=models.CharField(blank=True,max_length=1000)
    status=models.CharField(max_length=10,choices=STATUS)
    crate_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.question