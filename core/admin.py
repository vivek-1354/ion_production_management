from django.contrib import admin
from .models import Line, Product, Shift, ProductionData, LineProduct

admin.site.site_header = "Factory Production Dashboard Admin"
admin.site.site_title = "Production Admin Portal"
admin.site.index_title = "Welcome to the Production Management Panel"


@admin.register(ProductionData)
class ProductionDataAdmin(admin.ModelAdmin):
    """Customize the admin interface for ProductionData."""
    list_display = ('date', 'line', 'product', 'shift', 'line_speed', 'total_production', 'total_energy_consumed','created_by') #show these fields in list view
    readonly_fields = ('created_by',)
    list_filter = ('date', 'line', 'product', 'shift')  # Add filters for easier searching
    date_hierarchy = 'date'  # Add date hierarchy for navigating through dates
    ordering = ('-date', 'line', 'shift')  # Default ordering

    #make some fields editable in the list view
    list_editable = ('line_speed', 'total_production', 'total_energy_consumed')
    # add search
    search_fields = ('line__line_name', 'product__product_name', 'shift__shift_name')
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "product" and request.POST.get('line'):
            line_id = request.POST.get('line')
            allowed_products = Product.objects.filter(line_products__line_id=line_id)
            kwargs["queryset"] = allowed_products
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # This is a new object
            obj.created_by = request.user  # 👈 Set current user
        obj.save()

admin.site.register(Line)
admin.site.register(Product)
admin.site.register(Shift)
admin.site.register(LineProduct)
# admin.site.register(ProductionData,ProductionDataAdmin)

