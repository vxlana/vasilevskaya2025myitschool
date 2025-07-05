from django.contrib import admin
from .models import Size, Category, ClothingItem, ClothingItemSize

# можем добавлять размеры неограниченно
class ClothingItemSizeInline(admin.TabularInline):
    model = ClothingItemSize
    extra = 4

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(ClothingItem)
class ClothingItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'discount')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ClothingItemSizeInline]
    list_filter = ('category',)
    search_fields = ('name', 'description')




