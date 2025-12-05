
from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf.urls.static import static
from django.conf import settings
from blogs import views as blogViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = "home"),
    path('category/',include('blogs.urls')),
    path('blogs/search/', blogViews.search, name = 'search'),
    path('blogs/<slug:slug>/', blogViews.blogs, name = 'blogs' ),
    path('register/', views.register_view, name = 'register'),
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('dashboard/', include('dashboards.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
