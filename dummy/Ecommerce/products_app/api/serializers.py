from rest_framework import serializers
from products_app.models import Product, Brand



class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    brands = BrandSerializer(many=True)  # Include nested serialization of brands

    class Meta:
        model = Product
        fields = '__all__'













# class BrandSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Brand
#         fields = '__all__'


# class ProductSerializer(serializers.ModelSerializer):
#     brand = BrandSerializer(read_only=True)
    
#     class Meta:
#         model = Product
#         fields = '__all__'
    
    # def get_brand(self, obj):
    #     return {
    #         'name': obj.brand.name,
    #         'id': obj.brand.id,
    #         'price' : obj.brand.price 
    #     }
   













# class ProductSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     description = serializers.CharField(max_length=400)
#     price = serializers.DecimalField(max_digits=10, decimal_places=2)
#     discount_percentage = serializers.DecimalField(
#         max_digits=5, decimal_places=2)
#     rating = serializers.FloatField()
#     stock = serializers.IntegerField(min_value=1)
#     brand = serializers.CharField(max_length=255)
#     category = serializers.CharField(max_length=255)
#     thumbnail = serializers.URLField()
