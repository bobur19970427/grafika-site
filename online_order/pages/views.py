from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import Post, Product, Category


# Create your views here.
# class HomePageView(TemplateView):
#     template_name = 'index.html'

# class NewsPageView(ListView):
#     model = Post
#     template_name = 'news.html'


def home(request, category_slug=None):
	category_page = None
	products = None
	if category_slug != None:
		category_page = get_object_or_404(Category, slug=category_slug)
		products = Product.objects.filter(category=category_page, available=True)
	else:
		products = Product.objects.all().filter(available=True)
	return render(request, 'index.html', {'category':category_page, 'products': products})

def product(request, category_slug, product_slug):
	try:
		product = Product.objects.get(category__slug=category_slug, slug=product_slug)
	except Exception as e:
		raise e
	return render(request, 'product.html', {'product': product})


def NewsPageView(request):
    posts = Post.objects
    return render(request, 'news.html', {'posts': posts})

