from rest_framework import serializers
from .models import *

class BoshMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boshmenu
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class BookATableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookatable
        fields = '__all__'

class GetInTouchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Getintouch
        fields = '__all__'



class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = '__all__'

class ReserveYourSpotDetailsMenuTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserveyourspotdetailsmenutecher
        fields = '__all__'

class GiveAGiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Giveagift
        fields = '__all__'

class LatestNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Latestnews
        fields = '__all__'

class NewRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newrestuarant
        fields = '__all__'
