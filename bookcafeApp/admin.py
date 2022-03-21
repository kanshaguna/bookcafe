from django.contrib import admin
from bookcafeApp.models import Enquiry
from bookcafeApp.models import Menu

# Register your models here.
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'contact', 'message']

admin.site.register(Enquiry, EnquiryAdmin)

class MenuAdmin(admin.ModelAdmin):
    list_display = ['itemName', 'itemCategory', 'itemPrice']

admin.site.register(Menu, MenuAdmin)