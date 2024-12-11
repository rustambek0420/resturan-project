"""
URL configuration for resturan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
    path('home/',home, name='home'),
    path('index/',index, name='index'),
    path('categoryhtml/',categoryhtml, name='categoryhtml'),
    path('productshtml/',productshtml, name='productshtml'),
    path('boshmenuhtml', boshmenuhtml, name='boshmenuhtml'),
    path('getintouchhtml', getintouchhtml, name='getintouchhtml'),
    path('teacherhtml', teacherhtml, name='teacherhtml'),
    path('bookatablehtml', bookatablehtml, name='bookatablehtml'),
    path('details', detailshtml, name='detailshtml'),
    path('rs', rshtml, name='rshtml'),
    path('giveagifthtml', giveagifthtml, name='giveagifthtml'),
    path('latestnewshtml', latestnewshtml, name='latestnewshtml'),
    path('newrestuaranthtml', newrestuaranthtml, name='newrestuaranthtml'),

    path('BoshMenuViewset', BoshMenuSerializer, name='BoshMenuViewset'),
    path('CategoryViewset', CategorySerializer, name='CategoryViewset'),
    path('ProductViewset', ProductSerializer, name='ProductViewset'),
    path('CategorySerializer/<int:pk>', CategorySerializer, name='CategorySerializer'),
    path("ProductSerializer/<int:pk>", ProductSerializer, name="ProductSerializer"),
    path("BookATableViewSet", BookATableSerializer, name="BookATableViewSet"),
    path("GetInTouchViewSet", GetInTouchSerializer, name="GetInTouchViewSet"),
    path("TeacherViewSet/<int:pk>", TeacherSerializer, name="TeacherViewSet"),
    path("DatailsViewsSet/<int:pk>", DetailsSerializer, name="DatailViewsSet"),
    path("ReserveYourSpotDetailsMenuTeacherVie/<int:pk>", ReserveYourSpotDetailsMenuTeacherSerializer, name="ReserveYourSpotDetailsMenuTeacherViewSet"),
    path("GiveAGiftViewSet", GiveAGiftSerializer, name="GiveAGiftViewSet"),
    path("LatestNewsViewSet", LatestNewsSerializer, name="LatestNewsViewSet"),
    path("NewRestaurantViewSet",NewRestaurantSerializer, name="NewRestaurantViewSet"),


    path('boshmenu/', boshmenu_view, name='boshmenu_view'), 
    path('boshmenu/add/', add_boshmenu, name='add_boshmenu'), 
    path('boshmenu/<int:id>/update/', update_boshmenu, name='update_boshmenu'),
    path('boshmenu/<int:id>/delete/', delete_boshmenu, name='delete_boshmenu'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'), 
    path('bookatable/', bookatable_view, name='bookatable_view'), 
    path('bookatable/add/', add_bookatable, name='add_bookatable'), 
    path('bookatable/<int:id>/update/', update_bookatable, name='update_bookatable'),
    path('bookatable/<int:id>/delete/', delete_bookatable, name='delete_bookatable'),
    path('getintouch/', getintouch_view, name='getintouch_view'), 
    path('getintouch/add/', add_getintouch, name='add_getintouch'), 
    path('getintouch/<int:id>/update/', update_getintouch, name='update_getintouch'),
    path('getintouch/<int:id>/delete/', delete_getintouch, name='delete_getintouch'),
    path('teacher/', teacher_view, name='teacher_view'), 
    path('teacher/add/', add_teacher, name='add_teacher'), 
    path('teacher/<int:id>/update/', update_teacher, name='update_teacher'),
    path('teacher/<int:id>/delete/', delete_teacher, name='delete_teacher'),
    path('details/', details_view, name='details_view'), 
    path('details/add/', add_details, name='add_details'), 
    path('details/<int:id>/update/', update_details, name='update_details'),
    path('details/<int:id>/delete/', delete_details, name='delete_details'),
    path('rs/', rs_view, name='rs_view'), 
    path('rs/add/', add_rs, name='add_rs'), 
    path('rs/<int:id>/update/', update_rs, name='update_rs'),
    path('rs/<int:id>/delete/', delete_rs, name='delete_rs'),
    path('giveagift/', giveagift_view, name='giveagift_view'), 
    path('giveagift/add/', add_giveagift, name='add_giveagift'), 
    path('giveagift/<int:id>/update/', update_giveagift, name='update_giveagift'),
    path('giveagift/<int:id>/delete/', delete_giveagift, name='delete_giveagift'),
    path('latestnews/', latestnews_view, name='latestnews_view'), 
    path('latestnews/add/', add_latestnews, name='add_latestnews'), 
    path('latestnews/<int:id>/update/', update_latestnews, name='update_latestnews'),
    path('latestnews/<int:id>/delete/', delete_latestnews, name='delete_latestnews'),
    path('newrestuarant/', newrestuarant_view, name='newrestuarant_view'), 
    path('newrestuarant/add/', add_newrestuarant, name='add_newrestuarant'), 
    path('newrestuarant/<int:id>/update/', update_newrestuarant, name='update_newrestuarant'),
    path('newrestuarant/<int:id>/delete/', delete_newrestuarant, name='delete_newrestuarant'),

    path('category/', category_view, name='category_view'),
    path('category/add/', add_category, name='add_category'),
    path('category/<int:id>/update/', update_category, name='update_category'),
    path('category/<int:id>/delete/', delete_category, name='delete_category'),
    path('product/', product_view, name='product_view'),
    path('product/add/', add_product, name='add_product'),
    path('product/<int:id>/update/', update_product, name='update_product'),
    path('product/<int:id>/delete/', delete_product, name='delete_product'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
