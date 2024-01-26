from django.contrib import admin
from django.urls import path, include
from .views import home
# ------------------------------
from django.conf import settings
from django.conf.urls.static import static
#------------------------------------------

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('pets/<slug:category_slug>/', home, name='filterpet'),
    path('user/', include('User.urls')),
    path('user/', include('Pets.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
