from django.db import models
from django.utils.html import mark_safe
# Create your models here.

# Banner Model
class Banner(models.Model):
    image = models.ImageField(upload_to="banner_imgs/")
    alt_text = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural='1. Banners'

    def image_tag(self):
        return mark_safe('<img src="%s" width="100" />' % (self.image.url))

    def __str__(self):
        return self.alt_text

# Category Model
class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="cat_imgs/")

    class Meta:
        verbose_name_plural='2. Categories'
    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title

# Brand Model
class Brand(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="brand_imgs/")

    class Meta:
        verbose_name_plural='3. Brands'
        
    def __str__(self):
        return self.title

# Color Model
class Color(models.Model):
    title = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='4. Colors'
    
    def color_bg(self):
        return mark_safe('<div style="width:30px; height:30px; background-color:%s"></div>' % (self.color_code))

    def __str__(self):
        return self.title

# Size Model
class Size(models.Model):
    title = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural='5. Sizes'
        
    def __str__(self):
        return self.title
# Product Model
class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    detail = models.TextField()
    specs = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural='6. Products'
        
    def __str__(self):
        return self.title

# Product attribute Model
class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to="product_imgs/",default='')

    
    class Meta:
        verbose_name_plural='7. ProductAttribute'
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
        
    def __str__(self):
        return self.product.title
