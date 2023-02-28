from .models import Product, ProductAttribute
def get_filters(request):
    cats = Product.objects.distinct().values('category__title','category__id')
    brands = Product.objects.distinct().values('brand__title','brand__id')
    sizes = ProductAttribute.objects.distinct().values('size__title','size__id')
    colors = ProductAttribute.objects.distinct().values('color__title','color__id','color__color_code')
    data = {
        'cats':cats,
        'brands':brands,
        'sizes':sizes,
        'colors':colors,
    }
    return data