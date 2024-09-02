from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/properties/', include('property.urls')),
    path('api/properties/<uuid:property_id>/', include('review.urls')),  # Include review URLs under properties
    path('api/auth/', include('useraccount.urls')),
    path('api/chat/', include('chat.urls')),
    path('api/community/', include('community.urls')),  # Include community URLs
    path('api/payments/', include('payments.urls')),  # Include payment URLs here
]

# Serve media files using the configured MEDIA_URL
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
