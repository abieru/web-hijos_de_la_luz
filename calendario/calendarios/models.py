from django.db import models

# Create your models here.
class Category(models.Model):
    name    = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de edición")

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = "Categorias"
        ordering = ["-created"]

    def __str__(self):
        return self.name 

class Image(models.Model):
	name = models.CharField(max_length=100, verbose_name="Nombre")
	image = models.ImageField(upload_to='gallery', verbose_name="Imagen")
	categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_posts")
    	