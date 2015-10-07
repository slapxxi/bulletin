from .models import Category

def categories(_request):
    categories = Category.objects.all()
    return {'categories': categories}
