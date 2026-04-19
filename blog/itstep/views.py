from django.shortcuts import render, get_object_or_404
from .models import Course

def get_course():
    all = Course.objects.all()
    count = all.count()
    return {'cat1': all[:count // 2], 'cat2': all[count // 2:]}

# Create your views here.
def index(request):
    courses = Course.objects.all().order_by('-start')
    context = {'courses': courses}
    context.update(get_course())
    return render(request, "itstep/index.html", context)