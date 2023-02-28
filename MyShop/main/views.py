from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Banner,Category,Brand,Product,ProductAttribute
# Create your views here.

# Home (index) view
def index(request):
    banners = Banner.objects.all().order_by('-id')
    data = Product.objects.filter(is_featured=True).order_by('-id')
    return render(request,'index.html',{
        'data':data,
        'banners':banners,
        })

# Category List view
def category_list(request):
    data = Category.objects.all().order_by('-id')

    return render(request,'category_list.html',{'data':data})
# Brand List View
def brand_list(request):
    data = Brand.objects.all().order_by('-id')

    return render(request,'brand.html',{'data':data})
# Product List View
def product_list(request):
    data = Product.objects.all().order_by('-id')
    return render(request,'product_list.html',{
        'data':data,
        })


# Product List According to Category
def category_product_list(request,cat_id):
    category = Category.objects.get(id=cat_id)
    data = Product.objects.filter(category=category).order_by('-id')
    return render(request, 'category_product_list.html',{
        'data':data,
        })

# Brand List According to Category
def brand_product_list(request,brand_id):
    brand = Brand.objects.get(id=brand_id)
    data = Product.objects.filter(brand=brand).order_by('-id')
    return render(request, 'brand_product_list.html',{
        'data':data,
        })

# Product Detail
def product_detail(request,slug,id):
    product = Product.objects.get(id=id)
    related_products = Product.objects.filter(category=product.category).exclude(id=id)[:4]
    return render(request, 'product_detail.html',{
        'data':product,
        'related':related_products
        })

def search(request):
    q = request.GET['q']
    data = Product.objects.filter(title__icontains=q).order_by('-id')
    return render(request,'search.html',{'data':data})

# Filter data
def filter_data(request):
    colors = request.GET.getlist('color[]')
    categories = request.GET.getlist('category[]')
    brands = request.GET.getlist('brand[]')
    sizes = request.GET.getlist('size[]')
    allProducts = Product.objects.all().order_by('-id').distinct()
    if len(colors)>0:
        allProducts = allProducts.filter(productattribute__color__id__in=colors).distinct()
    if len(categories)>0:
        allProducts = allProducts.filter(category__id__in=categories).distinct()
    if len(brands)>0:
        allProducts = allProducts.filter(brand__id__in=brands).distinct()
    if len(sizes)>0:
        allProducts = allProducts.filter(productattribute__size__id__in=sizes).distinct()
    t = render_to_string('ajax/product-list.html',{'data':allProducts})
    return JsonResponse({'data':t}) 