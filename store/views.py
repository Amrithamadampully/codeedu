from django.contrib import messages
from django.shortcuts import render,redirect
from .models import *
from django.http.response import JsonResponse
from django.http import HttpResponse

# Create your views here.
def home(request):
    trending_products=Product.objects.filter(trending=1)
    context={"trending_products":trending_products}
    return render(request,"store/home.html",context)

def collections(request):
    category=Category.objects.filter(status=0)
    context={'category':category}
    return render(request,"store/collections.html",context)

def collectionsview(request,slug):
    if(Category.objects.filter(slug=slug,status=0)):
        products=Product.objects.filter(category__slug=slug)
        category=Category.objects.filter(slug=slug).first()
        context={"products":products,"category":category}
        return render(request, 'store/products/home.html',context)
    else:
        messages.warning(request,"NO such category found")
        return redirect("collections")


def productview(request, cate_slug, prod_slug):
    # Check if the category exists
    if Category.objects.filter(slug=cate_slug, status=0).exists():
        # Check if the product exists
        if Product.objects.filter(slug=prod_slug, status=0).exists():
            # Get the first matching product
            products = Product.objects.filter(slug=prod_slug, status=0).first()
            context = {'products': products}
        else:
            # Product not found
            messages.error(request, "No Such Product Found")
            return redirect("/")
    else:
        # Category not found
        messages.error(request, "No Such Category Found")
        return redirect("collections")

    return render(request, "store/products/view.html", context)

# def product_list(request):
#     products=Product.objects.filter(status=0).values_list('name',flat=True)
#     product_list=list(products)

    return JsonResponse(product_list,safe=False)
def searchproduct(request):
    if request.method=="POST":
        searchterm = request.POST.get('productsearch')
        if searchterm == "":
            return redirect(request.META.get("HTTP_REFERER"))
        else:
            product = Product.objects.filter(name__contains=searchterm).first()
            if product:
                return redirect('collections/'+product.category.slug+'/'+product.slug)
            else:
                messages.info(request,"No Product matched your search")
                return redirect(request.META.get("HTTP_REFERER"))

    return redirect(request.META.get("HTTP_REFERER"))







