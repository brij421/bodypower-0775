from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Homepage after login
    path('', login_required(views.homepage_after_login), name="homepage_after_login"),
    
    # Wallpaper settings
    path('wallpaper/', login_required(views.set_wallpaper), name="set_wallpaper"),
    
    # Change password
    path('change_password/', login_required(views.change_password), name='change_password'),
    
    # Login view, pointing to the correct template location
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
    # Logout view, pointing to the correct template location
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
] + static(settings.WALLPAPER_FILES, document_root=settings.WALLPAPER_URL)
