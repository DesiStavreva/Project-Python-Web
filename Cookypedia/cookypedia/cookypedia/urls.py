from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('cookypedia.core.urls')),
                  path('profile/', include('cookypedia.profiles.urls')),
                  path('', include('cookypedia.recipe.urls')),
                  path('', include('cookypedia.cocktail.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
