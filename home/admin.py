from django.contrib import admin
from home.models import Setting, ContactFormMessage,Comment

class SettingAdmin(admin.ModelAdmin):
    list_display=['title', 'status']
    list_filter=['status']      #filtreleme ypar
admin.site.register(Setting,SettingAdmin)

class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display=['name','subject','note','status', 'message',]
    list_filter=['status']      #filtreleme ypar
admin.site.register(ContactFormMessage,ContactFormMessageAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display =['subject','comment','product','user','status',]
    list_filter=['status']
admin.site.register(Comment,CommentAdmin)

