from django.contrib import admin
from .models import GstRegistration


# admin.site.register(GstRegistration)
@admin.register(GstRegistration)
class GstAdmin(admin.ModelAdmin):
    list_display = ['Invoice_Number', 'Date', 'Customer_Name', 'Customer_Address', 'Customer_Mobile_Number', 'Product',
                    'Product_Price', 'GST', 'Total']
