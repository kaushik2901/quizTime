"""quizMania URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index),
    path('questions/', views.Question),
    path('requestQuestion/', csrf_exempt(views.requestQuestion)),
    path('validateAnswer/', csrf_exempt(views.ValidateAnswer)),
    path('HideRules/', csrf_exempt(views.HideRules)),
    path('login/', views.login),
    path('distance/', views.Distance),
    path('road_api/', views.RoadApi),
    path('tables/', views.RoadTable),
    path('upload_image/', csrf_exempt(views.Image_Upload)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
