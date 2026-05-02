from django.db import models
from PIL import Image
import os
from django.utils.text import slugify
from io import BytesIO
from django.core.files.base import ContentFile

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='shop/categories/')
    thumbnail = models.ImageField(upload_to='shop/categories/thumbnails/', blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=120, unique=False, blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        if self.image and not self.thumbnail:
            self.create_thumbnail()

    def create_thumbnail(self):
        img = Image.open(self.image.path)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        img.thumbnail((200, 200))
        temp_thumb = BytesIO()
        img.save(temp_thumb, format='JPEG', quality=85)
        temp_thumb.seek(0)
        file_name = os.path.basename(self.image.name)
        self.thumbnail.save(
            file_name,
            ContentFile(temp_thumb.read()),
            save=False
        )
        super().save(update_fields=['thumbnail'])

class Product(models.Model):
    title = models.TextField()
    images = models.ImageField(upload_to='shop/products/')
    thumbnail = models.ImageField(upload_to='shop/products/thumbnails/', blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    about = models.TextField()
    slug = models.SlugField(max_length=120, unique=False, blank=True, null=True)

    def create_thumbnail(self):
        img_path = self.image.path
        thumb_path = os.path.join(os.path.dirname(img_path), 'thumbnails', os.path.basename(img_path))
        os.path.basename(img_path)
        img = Image.open(img_path)
        img.thumbnail((200, 200))
        os.makedirs(os.path.dirname(thumb_path), exist_ok=True)
        img.save(thumb_path)
        self.thumbnail = f"shop/products/thumbnails/{os.path.basename(img_path)}"
        super().save(update_fields=['thumbnail'])

class ProductImeges(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shop/products/')
