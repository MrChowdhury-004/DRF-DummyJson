from rest_framework.response import Response
from rest_framework.views import APIView

from products_app.api.serializers import ProductSerializer, BrandSerializer
from products_app.models import Product
from rest_framework import status


class GroupedProducts(APIView):
    def get(self, request):
        # Retrieve all products
        products = Product.objects.all()

        # Serialize the products with nested brands
        serialized_products = ProductSerializer(products, many=True).data

        return Response(serialized_products)


class ProductsList(APIView):
    
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        
        # Return only the list of products as an array
        return Response(serializer.data)
 
    
class ProductDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class ProductsList(APIView):
    
#     def get(self, request, format=None):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
        
#         # Customize the response format|
#         response_data = {
#             "products": serializer.data,
#             "total": products.count(),
#             "skip": 0,  #  can customize these values as needed
#             "limit": 30
#         }
        
#         return Response(response_data)
    

    


# class GroupedProducts(APIView):
#     def get(self, request):
#         # Retrieve all products
#         products = Product.objects.all()

#         # Create a dictionary to group products by title
#         grouped_products = {}
#         for product in products:
#             title = product.title
#             if title not in grouped_products:
#                 grouped_products[title] = []

#             # Create a list of brand serializers for each product
#             brand_serializers = [BrandSerializer(brand).data for brand in product.brands.all()]

#             # Serialize the product with multiple brands
#             product_data = ProductSerializer(product).data
#             product_data["brands"] = brand_serializers

#             grouped_products[title].append(product_data)

#         return Response(grouped_products)
