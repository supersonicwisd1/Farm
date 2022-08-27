from django.shortcuts import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .models import Crop, Category
from .serializers import CropSerializer, CategorySerializer


class CropsList(APIView):
    def get(self, request, format=None):
        crops = Crop.objects.all()
        serializer = CropSerializer(crops, many=True)
        return Response(serializer.data)
    
class CropDetail(APIView):
    def get_object(self, category_slug, crop_slug):
        try:
            return Crop.objects.filter(category__slug=category_slug).get(slug=crop_slug)
        except Crop.DoesNotExist:
            raise Http404
        
    def get(self, request, category_slug, crop_slug, format=None):
        crop = self.get_object(category_slug, crop_slug)
        serializer = CropSerializer(crop)
        return Response(serializer.data)
    
class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Crop.DoesNotExist:
            raise Http404
        
    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')
    
    if query:
        crops = Crop.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = CropSerializer(crops, many=True)
        return Response(serializer.data)
    else:
        return Response({"crops": []})