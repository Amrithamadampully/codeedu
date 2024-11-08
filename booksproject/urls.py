"""
URL configuration for booksproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from store import  views
from django.conf.urls.static import static
from django.conf import settings
from store.controller import authview,cart,order



urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/',include('store.urls')),# Include your store app's URLs
    path('',views.home),# Handle the root URL by pointing it to a view (home page)
    path('collections',views.collections,name='collections'),
    path('collections/<str:slug>',views.collectionsview,name='collectionsview'),
    path('collections/<str:cate_slug>/<str:prod_slug>',views.productview,name='productview'),
    path('register/', authview.register, name='register'),  # Register URL at root level
    path('login/', authview.loginpage, name='loginpage'),
    path('logout/',authview.logoutpage,name="logout"),
    path('add-to-cart',cart.addtocart,name='/add-to-cart'),
    path('store/order/',order.order_view, name='order'),
    path('view-order/<str:t_no>/', order.view_order, name='orderview'),
    # path('product-list/', views.product_list, name='product_list'),
    path('searchproduct/', views.searchproduct, name='searchproduct'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
