from django.contrib import admin
from order.models import ShopCart, OrderProduct,Order

class ShopCartAdmin(admin.ModelAdmin):
    list_display=['user','product','price','quantity','amount']
    list_filter=['user']
admin.site.register(ShopCart,ShopCartAdmin)

class OrderProductInline(admin.TabularInline):
    model=OrderProduct
    readonly_fields=('user','product','price','quantity','amount')
    can_delete=False
    extra=0

class OrderAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','phone','city','total','status']
    list_filter=['status']
    readonly_fields=('user','adress','city','country','phone','first_name','ip','last_name','total')
    inlines=[OrderProductInline]
admin.site.register(Order,OrderAdmin)

class OrderProductAdmin(admin.ModelAdmin):
    list_display=['user','product','price','quantity','amount']
    list_filter=['user']
admin.site.register(OrderProduct,OrderProductAdmin)