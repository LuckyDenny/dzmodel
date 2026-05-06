from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ('id', 'first_name', 'last_name', 'email', 'total_coast', 'created_at')
    list_filter = ('last_name', 'first_name', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')

    def get_total_coast(self):
        return sum(item.total_coast() for item in self.items.all())

    get_total_coast.short_description = "Total coast"