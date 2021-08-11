from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.
from .forms import SignUpForm
from .models import CustomUser
from django.core.files.storage import FileSystemStorage

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration.html'

class UserProfileView(generic.TemplateView):
    template_name = 'profile/index.html'

class ProfileView(generic.TemplateView):
    template_name = 'profile/profile.html'


def UpdateProfieleView(request, id):
    records = CustomUser.objects.get(id=id)
    records.username = request.POST['username']
    records.first_name = request.POST[ 'first_name']
    records.last_name = request.POST['last_name']
    records.email = request.POST['email']

    img_file = request.FILES['image']

    fs = FileSystemStorage('media/media/avatar/')
    filename = fs.save(img_file.name, img_file)
    uploaded_file_path = fs.path(filename)

    records.image = uploaded_file_path
    records.save()
    return redirect("/profile")

def EditProfieleView(request, user_id):
    user = get_object_or_404(CustomUser,pk=user_id)
    return render(request, 'profile/update.html', {'user': user})