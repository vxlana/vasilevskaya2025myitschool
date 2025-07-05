from django.contrib import admin
from .models import Order, OrderItem
from .utils import generate_tracking_number


@admin.action(description="Отправить заказ (присвоить трек-номер)")
def mark_as_shipped(modeladmin, request, queryset):
    for order in queryset:
        if order.tracking_number in [None, "", "В ожидании", "Pending",]:
            order.tracking_number = generate_tracking_number()
        order.status = "shipped"
        order.save()

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "created_at", "tracking_number")
    search_fields = ("first_name", "last_name", "city", "street", "postal_code", "tracking_number")
    inlines = [OrderItemInline]
    actions = [mark_as_shipped]

    fieldsets = (
        (None, {
            'fields': ('user', 'first_name', 'last_name',
                       'middle_name', 'city', 'street',
                       'house_number', 'apartment_number',
                       'postal_code', 'tracking_number')
        }),
    )

admin.site.register(Order, OrderAdmin)


