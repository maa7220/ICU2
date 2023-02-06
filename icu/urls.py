from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
import notifications.urls
from django_rest_passwordreset.views import ResetPasswordConfirmViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/password_reset/',
         include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('inbox/notifications/',
         include(notifications.urls, namespace='notifications')),
    path('api/', include('api.urls')),
    path('api/report/', include('report.urls')),
    path('api/medicine/', include('medicine.urls')),
    path('api/admins/', include('admins.urls')),
    path('api/rays/', include('rays.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
