from django.shortcuts import render, redirect
from .models import Comment
from .form import CommentForm
from django.core.paginator import Paginator
from .filters import ClothingItemFilter
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .form import RegisterForm
from django.http import JsonResponse
from .models import Category, ClothingItem

def product_index(request):
    filterset = ClothingItemFilter(request.GET, queryset=ClothingItem.objects.all().order_by('created_on'))
    paginator = Paginator(filterset.qs, 8)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "filterset": filterset,
        "page_obj": page_obj,
        "posts": page_obj.object_list,
    }
    return render(request, "main/products/list.html", context)

def product_detail(request, pk):
    post = ClothingItem.objects.get(pk=pk)

    # Получаем все размеры с доступностью для этого товара
    sizes_availability = []
    for size in post.sizes.all():
        # Получаем связь ClothingItemSize для этого размера и товара
        cis = post.clothingitemsize_set.filter(size=size).first()
        available = cis.available if cis else False
        sizes_availability.append({'size': size.name, 'available': available})

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                autor=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
        "sizes_availability": sizes_availability,
    }

    return render(request, "main/products/detail.html", context)


# ======================== для бота ==============================

def category_list_api(request):
    categories = Category.objects.all()
    data = [{'id': cat.id, 'name': cat.name} for cat in categories]
    return JsonResponse(data, safe=False)

def clothing_items_by_category_api(request, category_id):
    items = ClothingItem.objects.filter(category_id=category_id)
    data = []
    for item in items:
        data.append({
            'id': item.id,
            'name': item.name,
            'price': float(item.price),
            'discount': float(item.discount),
            'price_with_discount': float(item.get_price_with_discount()),
            'image': request.build_absolute_uri(item.image.url) if item.image else None,
            'description': item.description
        })
    return JsonResponse(data, safe=False)

