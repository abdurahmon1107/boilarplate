# from django.shortcuts import render
from rest_framework.generics import *
from .serializers import *

class ProfileUpdateAPIView(UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# __________________________________________________________________________________

class CategoryRetrieveAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# __________________________________________________________________________________

class SubcategoryRetrieveAPIView(RetrieveAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

# __________________________________________________________________________________

class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# __________________________________________________________________________________

class Give_offerCreateAPIView(CreateAPIView):
    queryset = Give_offer.objects.all()
    serializer_class = Give_offerSerializer

# __________________________________________________________________________________

class LocationCreateAPIView(CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

# __________________________________________________________________________________

class CenterCreateAPIView(CreateAPIView):
    queryset = Center.objects.all()
    serializer_class = CenterSerializer

class CenterRetrieveAPIVeiw(RetrieveAPIView):
    queryset = Center.objects.all()
    serializer_class = CenterSerializer

# __________________________________________________________________________________

class ProductClearanceSerializer(CreateAPIView):
    queryset = ProductClearance.objects.all()
    serializer_class = ProductClearance


# __________________________________________________________________________________
    
class ProductAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'