from django.urls import path
from .views import SignUpView, UserProfileView, ProfileView, EditProfieleView, UpdateProfieleView
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('adminprofile/', UserProfileView.as_view(), name='adminprofile'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('edit/<int:user_id>', EditProfieleView, name='edit'),
    path('update/<int:id>',UpdateProfieleView, name='update'),


]