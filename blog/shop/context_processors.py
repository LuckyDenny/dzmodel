from .models import Category

def categorys_processor(request):
    categories = Category.objects.all()
    return {'categories': categories}