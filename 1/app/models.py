from django.db import models
from django.db import models


class Boshmenu(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    ishvaqti = models.CharField(max_length=100)  

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    
class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_food_of_day = models.BooleanField(default=False)

    def __str__(self):
        return self.name




    
class Bookatable(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    people = models.IntegerField()

    def __str__(self):
        return self.name
    

class Getintouch(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    


    
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    malumoti = models.TextField(default=False)

    def __str__(self):
        return self.name
    

class Details(models.Model):
    date = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    language = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    
class Reserveyourspotdetailsmenutecher(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    details = models.ForeignKey(Details, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Giveagift(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    price = models.CharField(max_length=100)
    text = models.TextField()


    def __str__(self):
        return self.name
    
class Latestnews(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    text = models.TextField()
    date = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Newrestuarant(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    text = models.TextField()

    def __str__(self):
        return self.name