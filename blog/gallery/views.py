from django.shortcuts import render,redirect
from .models import GalleryImages
from .forms import GalleryImagesForm

# Create your views here.
def gallery(request):
    images = GalleryImages.objects.all()
    return render(request,'gallery/index.html', {"images":images})

def uploads(request):
    if request.method == 'POST':
        form = GalleryImagesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = GalleryImagesForm()
    return render(request,'gallery/uploads.html', {"form":form})