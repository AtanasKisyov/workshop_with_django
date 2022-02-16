from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('workshop.main.urls')),
    path('pet/', include('workshop.pet.urls')),
    path('photo/', include('workshop.photo.urls')),
    path('profile/', include('workshop.user_profile.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
