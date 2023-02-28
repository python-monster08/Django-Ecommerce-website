from django.contrib import admin
from .models import Banner, Category, Brand,Color,Size,Product,ProductAttribute
# Register your models here.
# admin.site.register(Banner)
# admin.site.register(Category)
admin.site.register(Brand)
# admin.site.register(Color)
admin.site.register(Size)

# BannerAdmin
class BannerAdmin(admin.ModelAdmin):
    list_display = ['alt_text','image_tag']
admin.site.register(Banner,BannerAdmin)

# CategoryAdmin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','image_tag']
admin.site.register(Category,CategoryAdmin)

# ColorAdmin
class ColorAdmin(admin.ModelAdmin):
    list_display = ['title','color_bg']
admin.site.register(Color,ColorAdmin)


# ProductAdmin
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','category','brand','color','size','status','is_featured']
    list_editable = ('status','is_featured')
admin.site.register(Product,ProductAdmin)

# ProductAttributeAdmin
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ['id','image_tag','product','price','color','size']
admin.site.register(ProductAttribute,ProductAttributeAdmin)