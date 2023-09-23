from django.contrib import admin
from products_app.models import Product, Brand



from django.contrib import admin
from products_app.models import Product, Brand

class ProductAdmin(admin.ModelAdmin):
    #list_display = ('id', 'title', 'category', 'thumbnail', 'get_price', 'get_discount_percentage', 'get_rating', 'get_stock')

    # Define methods to display the desired fields
    def get_price(self, obj):
        return obj.brands.first().price if obj.brands.exists() else None
    get_price.short_description = 'Price'  # Set the column header name

    def get_discount_percentage(self, obj):
        return obj.brands.first().discount_percentage if obj.brands.exists() else None
    get_discount_percentage.short_description = 'Discount Percentage'

    def get_rating(self, obj):
        return obj.brands.first().rating if obj.brands.exists() else None
    get_rating.short_description = 'Rating'

    def get_stock(self, obj):
        return obj.brands.first().stock if obj.brands.exists() else None
    get_stock.short_description = 'Stock'

    # Other admin customizations as needed

admin.site.register(Product, ProductAdmin)
admin.site.register(Brand)



# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 
#                     'category', 'thumbnail', 'get_description', 
#                     'get_price', 'get_discount_percentage', 'get_rating', 'get_stock')

#     def get_description(self, obj):
#         return obj.description

#     def get_price(self, obj):
#         return obj.price

#     def get_discount_percentage(self, obj):
#         return obj.discount_percentage

#     def get_rating(self, obj):
#         return obj.rating

#     def get_stock(self, obj):
#         return obj.stock

#     get_description.short_description = 'Description'
#     get_price.short_description = 'Price'
#     get_discount_percentage.short_description = 'Discount Percentage'
#     get_rating.short_description = 'Rating'
#     get_stock.short_description = 'Stock'

#     # Other admin customization as needed

# admin.site.register(Product, ProductAdmin)
# admin.site.register(Brand)





# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'brand_name', 'description', 'price', 'discount_percentage', 'rating', 'stock', 'category', 'thumbnail')

#     def brand_name(self, obj):
#         return obj.brand.name  # Display the brand's name

#     brand_name.short_description = 'Brand'  # Set the column header name

#     def save_model(self, request, obj, form, change):
#         # Extract the brand name and model from the form data
#         brand_name = form.cleaned_data.get('brand_name')
#         brand_model = form.cleaned_data.get('brand_model')

#         # Check if both brand_name and brand_model are provided
#         if brand_name and brand_model:
#             # Create or retrieve the Brand object based on the provided name and model
#             brand, created = Brand.objects.get_or_create(name=brand_name, model=brand_model)

#             # Associate the product with the brand
#             obj.brand = brand
#         else:
#             # Handle the case where brand_name or brand_model is missing
#             # You can add appropriate error handling here
#             pass

#         super().save_model(request, obj, form, change)

#     # Define the fields to include in the product creation form
#     # These fields should match the names used in the form.cleaned_data above
#     fields = ('title', 'description', 'price', 'discount_percentage', 'rating', 'stock', 'category', 'thumbnail', 'brand_name', 'brand_model')

# admin.site.register(Product, ProductAdmin)
# admin.site.register(Brand)






























# admin.site.register(Product, ProductAdmin)
# admin.site.register(Brand)







# class BrandInline(admin.StackedInline):
#     model = Brand
#     extra = 2  # Number of Brand forms to display when adding a Product

# class ProductAdmin(admin.ModelAdmin):
#     inlines = [BrandInline]

# admin.site.register(Product, ProductAdmin)
# admin.site.register(Brand)



# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'brand_name', 'description', 'price', 'discount_percentage', 'rating', 'stock', 'category', 'thumbnail')

#     def brand_name(self, obj):
#         return obj.brand

#     brand_name.short_description = 'Brand'  # Set the column header name

# admin.site.register(Product, ProductAdmin)
