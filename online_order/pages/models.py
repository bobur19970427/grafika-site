from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=250)
    description = models.TextField()

    class Meta:
        ordering = ('name',)
        verbose_name ='category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.name

class Product(models.Model):
	name = models.CharField(max_length=250, unique=True)
	slug = models.CharField(max_length=250, unique=True)
	description = models.TextField(blank=True)
	category=models.ForeignKey(Category, on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	image = models.ImageField(upload_to='product', blank=True)
	stock = models.IntegerField()
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name', )
		verbose_name = 'product'
		verbose_name_plural = 'products'

	def get_url(self):
		return reverse('product_details', args=[self.category.slug, self.slug])

	def __str__(self):
		return self.name