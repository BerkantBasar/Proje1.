from django.contrib import admin
from home.models import Setting, ContactFormMessage,Comment, UserProfileForm, UserProfile,FAQ

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

class UserProfileAdmin(admin.ModelAdmin):
    #list_display =['user','city','country','image_tag']
    list_filter=['user']
admin.site.register(UserProfile,UserProfileAdmin)

class FAQAdmin(admin.ModelAdmin):
    list_display =['question','answer','status']
    list_filter=['status']
admin.site.register(FAQ,FAQAdmin)
