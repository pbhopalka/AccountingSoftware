from django.contrib import admin

# Register your models here.
# For logging in to admin: username:pbhopalka and passwd:NORMAL

from .models import C_Details, Manager, Bill_Record, Payment_Record

# Use admin.StackInline or admin.TabularInline if we have foreign keys and needs
# to be included in one table. Check https://docs.djangoproject.com/en/1.8/intro/tutorial02/#adding-related-objects

class C_Details_Admin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields':['CustName']}),
        ('Address',     {'fields':['AddStreet', 'AddDistrict', 'AddState']}),
        ('Contact Info',{'fields':['Email', 'Phone']}),
        (None,          {'fields':['PendingAmount']}),
    ]
    # See https://docs.djangoproject.com/en/1.8/intro/tutorial02/#customize-the-admin-change-list
    list_display = ('CustID', 'CustName', 'PendingAmount', 'is_safe_state')
    list_filter = ['PendingAmount']
    #for adding search capabilities
    search_fields = ['CustName']

class Manager_Admin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields':['ManaName']}),
        (None,          {'fields':['ManaAuth']}),
        ('Credentials', {'fields':['username', 'password'], 'classes':['collapse']}),
    ]
    list_display = ('ManaID', 'ManaName', 'ManaAuth')

class Bill_Record_Admin(admin.ModelAdmin):
    list_display = ('BillID', 'Date', 'Amount')
    # Add filter on the page
    list_filter = ['Date']

class Payment_Record_Admin(admin.ModelAdmin):
    list_display = ('PaymentID', 'Date', 'Amount')
    list_filter = ['Date']

admin.site.register(C_Details, C_Details_Admin)
admin.site.register(Manager, Manager_Admin)
admin.site.register(Bill_Record, Bill_Record_Admin)
admin.site.register(Payment_Record, Payment_Record_Admin)
