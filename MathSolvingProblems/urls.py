from django.contrib import admin
from django.urls import path , include
# include - we can access other apps urls

from django.conf.urls.static import static
from MathSolvingProblems import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('', include('users.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)