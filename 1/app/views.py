from django.shortcuts import render,redirect,get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from .forms import *
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, CustomLoginForm
from django.contrib import messages
from django.http import HttpResponseNotFound


def home(request):
    return render(request,'index.html')

def index(request):
    context = {
        'categoryes': Category.objects.all(),
        'productes' : Product.objects.all(),
        'boshmenus': Boshmenu.objects.all(),
        'bookatablees': Bookatable.objects.all(),
        'getintouches':Getintouch.objects.all(),
        'teachers':Teacher.objects.all(),
        'detailes':Details.objects.all(),
        'rses' : Reserveyourspotdetailsmenutecher.objects.all(),
        'giveagiftes':Giveagift.objects.all(),
        'latestnewses' : Latestnews.objects.all(),
        'newrestuarantes': Newrestuarant.objects.all(),
    }
    return render(request,'home.html', context=context)

def categoryhtml(request):
    return render(request,'category.html')

def productshtml(request):
    return render(request,'products.html')


def boshmenuhtml(request):
    return render(request,'boshmenu.html')

def bookatablehtml(request):
    return render(request,'bookatable.html')

def getintouchhtml(request):
    return render(request,'getintouch.html')

def teacherhtml(request):
    return render(request,'teacher.html')


def detailshtml(request):
    return render(request,'details.html')

def rshtml(request):
    return render(request,'rs.html')

def giveagifthtml(request):
    return render(request,'giveagife.html')

def latestnewshtml(request):
    return render(request,'latestnews.html')

def newrestuaranthtml(request):
    return render(request,'newrestuarant.html')

class BoshMenuViewSet(ModelViewSet):
    queryset = Boshmenu.objects.all()
    serializer_class = BoshMenuSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class BookATableViewSet(ModelViewSet):
    queryset = Bookatable.objects.all()
    serializer_class = BookATableSerializer

class GetInTouchViewSet(ModelViewSet):
    queryset = Getintouch.objects.all()
    serializer_class = GetInTouchSerializer



class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class DetailsViewSet(ModelViewSet):
    queryset = Details.objects.all()
    serializer_class = DetailsSerializer

class ReserveYourSpotDetailsMenuTeacherViewSet(ModelViewSet):
    queryset = Reserveyourspotdetailsmenutecher.objects.all()
    serializer_class = ReserveYourSpotDetailsMenuTeacherSerializer

class GiveAGiftViewSet(ModelViewSet):
    queryset = Giveagift.objects.all()
    serializer_class = GiveAGiftSerializer

class LatestNewsViewSet(ModelViewSet):
    queryset = Latestnews.objects.all()
    serializer_class = LatestNewsSerializer

class NewRestaurantViewSet(ModelViewSet):
    queryset = Newrestuarant.objects.all()
    serializer_class = NewRestaurantSerializer





def boshmenu_view(request):
    boshmenus = Boshmenu.objects.all()  
    return render(request, 'boshmenu.html', {'boshmenus': boshmenus})


def delete_boshmenu(request, id):
    boshmenu = Boshmenu.objects.get(id=id)
    boshmenu.delete()
    return redirect('boshmenu_view')

def add_boshmenu(request):
    if request.method == 'POST':
        form = BoshmenuForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('boshmenu_view')
    else:
        form = BoshmenuForm()
    return render(request, 'boshmenu.html', {'form': form})

def update_boshmenu(request, id):
    boshmenu = get_object_or_404(Boshmenu, id=id)  
    if request.method == "POST":
        form = BoshmenuForm(request.POST, instance=boshmenu)  
        if form.is_valid():
            form.save()  
            return redirect('boshmenu_view')  
    else:
        form = BoshmenuForm(instance=boshmenu) 

    return render(request, 'update_boshmenu.html', {'form': form})


# Ro'yxatdan o'tish
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            messages.success(request, "Registration successful!")
            return redirect('home')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

#tizimga kirish
def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Welcome, you are logged in!")
                return redirect('home') 
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')






def category_view(request):
    categoryes = Category.objects.all()  
    return render(request, 'category.html', {'categoryes': categoryes})


def delete_category(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('category_view')

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_view')
    else:
        form = CategoryForm()
    return render(request, 'category.html', {'form': form})

def update_category(request, id):
    category = get_object_or_404(Category, id=id)  
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)  
        if form.is_valid():
            form.save()  
            return redirect('category_view')  
    else:
        form = CategoryForm(instance=category) 

    return render(request, 'update_category.html', {'form': form})

def bookatable_view(request):
    bookatables = Bookatable.objects.all()  
    return render(request, 'Bookatable.html', {'bookatables': bookatables})


def delete_bookatable(request, id):
    bookatable = Bookatable.objects.get(id=id)
    bookatable.delete()
    return redirect('bookatable_view')

def add_bookatable(request):
    if request.method == 'POST':
        form = BookatableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookatable_view')
    else:
        form = BookatableForm()
    return render(request, 'Bookatable.html', {'form': form})

def update_bookatable(request, id):
    bookatable = get_object_or_404(Bookatable, id=id)  
    if request.method == "POST":
        form = BookatableForm(request.POST, instance=bookatable)  
        if form.is_valid():
            form.save()  
            return redirect('bookatable_view')  
    else:
        form = BookatableForm(instance=bookatable) 

    return render(request, 'updatebookatable.html', {'form': form})







def getintouch_view(request):
    getintouchs = Getintouch.objects.all()  
    return render(request, 'getintouch.html', {'getintouchs': getintouchs})


def delete_getintouch(request, id):
    bookatable = Getintouch.objects.get(id=id)
    bookatable.delete()
    return redirect('getintoch_view')

def add_getintouch(request):
    if request.method == 'POST':
        form = GetintouchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('getintouch_view')
    else:
        form = GetintouchForm()
    return render(request, 'getintouch.html', {'form': form})

def update_getintouch(request, id):
    getintouch = get_object_or_404(Getintouch, id=id)  
    if request.method == "POST":
        form = GetintouchForm(request.POST, instance=getintouch)  
        if form.is_valid():
            form.save()  
            return redirect('getintouch_view')  
    else:
        form = GetintouchForm(instance=getintouch) 

    return render(request, 'update_getintouch.html', {'form': form})



def teacher_view(request):
    teachers = Teacher.objects.all()  
    return render(request, 'teacher.html', {'teachers': teachers})


def delete_teacher(request, id):
    teacher = Teacher.objects.get(id=id)
    teacher.delete()
    return redirect('teacher_view')

def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_view')
    else:
        form = TeacherForm()
    return render(request, 'teacher.html', {'form': form})

def update_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)  
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)  
        if form.is_valid():
            form.save()  
            return redirect('teacher_view')  
    else:
        form = TeacherForm(instance=teacher) 

    return render(request, 'update_teacher.html', {'form': form})



def details_view(request):
    detailes = Details.objects.all()  
    return render(request, 'details.html', {'details': detailes})


def delete_details(request, id):
    details = Details.objects.get(id=id)
    details.delete()
    return redirect('details_view')

def add_details(request):
    if request.method == 'POST':
        form = DetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details_view')
    else:
        form = DetailsForm()
    return render(request, 'details.html', {'form': form})

def update_details(request, id):
    details = get_object_or_404(Details, id=id)  
    if request.method == "POST":
        form = DetailsForm(request.POST, instance=details)  
        if form.is_valid():
            form.save()  
            return redirect('details_view')  
    else:
        form = DetailsForm(instance=details) 

    return render(request, 'update_details.html', {'form': form})




def rs_view(request):
    rses = Reserveyourspotdetailsmenutecher.objects.all()  
    return render(request, 'rs.html', {'rses': rses})


def delete_rs(request, id):
    rs = Reserveyourspotdetailsmenutecher.objects.get(id=id)
    rs.delete()
    return redirect('rs_view')

def add_rs(request):
    if request.method == 'POST':
        form = RsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rs_view')
    else:
        form = RsForm()
    return render(request, 'rs.html', {'form': form})

def update_rs(request, id):
    rs = get_object_or_404(rs, id=id)  
    if request.method == "POST":
        form = RsForm(request.POST, instance=rs)  
        if form.is_valid():
            form.save()  
            return redirect('rs_view')  
    else:
        form = RsForm(instance=rs) 

    return render(request, 'update_rs.html', {'form': form})


def giveagift_view(request):
    giveagiftes = Giveagift.objects.all()  
    return render(request, 'giveagife.html', {'giveagiftes': giveagiftes})


def delete_giveagift(request, id):
    giveagift = Giveagift.objects.get(id=id)
    giveagift.delete()
    return redirect('giveagift_view')

def add_giveagift(request):
    if request.method == 'POST':
        form = GiveagifeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('giveagift_view')
    else:
        form = GiveagifeForm()
    return render(request, 'giveagife.html', {'form': form})

def update_giveagift(request, id):
    giveagift = get_object_or_404(Giveagift, id=id)  
    if request.method == "POST":
        form = GiveagifeForm(request.POST, instance=giveagift)  
        if form.is_valid():
            form.save()  
            return redirect('giveagife_view')  
    else:
        form = GiveagifeForm(instance=giveagift) 

    return render(request, 'update_giveagife.html', {'form': form})



def latestnews_view(request):
    latestnewses = Latestnews.objects.all()  
    return render(request, 'latestnews.html', {'latestnewses': latestnewses})


def delete_latestnews(request, id):
    latestnews = Latestnews.objects.get(id=id)
    latestnews.delete()
    return redirect('latestnews_view')

def add_latestnews(request):
    if request.method == 'POST':
        form = LatestnewsrForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('latestnews_view')
    else:
        form = LatestnewsrForm()
    return render(request, 'latestnews.html', {'form': form})

def update_latestnews(request, id):
    latestnews = get_object_or_404(Latestnews, id=id)  
    if request.method == "POST":
        form = LatestnewsrForm(request.POST, instance=latestnews)  
        if form.is_valid():
            form.save()  
            return redirect('latestnews_view')  
    else:
        form = LatestnewsrForm(instance=latestnews) 

    return render(request, 'update_latestnews.html', {'form': form})


def newrestuarant_view(request):
    newrestuarantes = Newrestuarant.objects.all()  
    return render(request, 'newrestuarant.html', {'newrestuarantes': newrestuarantes})


def delete_newrestuarant(request, id):
    newrestuarant = Newrestuarant.objects.get(id=id)
    newrestuarant.delete()
    return redirect('newrestuarant_view')

def add_newrestuarant(request):
    if request.method == 'POST':
        form = NewrestuarantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('newrestuarant_view')
    else:
        form = NewrestuarantForm()
    return render(request, 'newrestuarant.html', {'form': form})

def update_newrestuarant(request, id):
    newrestuarant = get_object_or_404(Newrestuarant, id=id)  
    if request.method == "POST":
        form = NewrestuarantForm(request.POST, instance=newrestuarant)  
        if form.is_valid():
            form.save()  
            return redirect('newrestuarant_view')  
    else:
        form = NewrestuarantForm(instance=newrestuarant) 

    return render(request, 'update_newrestuarant.html', {'form': form})


def product_view(request):
    productes = Product.objects.all()  
    return render(request, 'products.html', {'productes': productes})


def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('product_view')

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save
            return redirect('product_view')
    else:
        form = ProductForm()
    return render(request, 'products.html', {'form': form})

def update_product(request, id):
    product = get_object_or_404(product, id=id)  
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)  
        if form.is_valid():
            form.save()  
            return redirect('product_view')  
    else:
        form = ProductForm(instance=product) 

    return render(request, 'update_products.html', {'form': form})
