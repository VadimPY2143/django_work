from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),
    path('product/', include('products.urls')),
    path('review/', include('reviews.urls')),
    path('order/', include('orders.urls')),
    path('cart/', include('carts.urls')),
    path('payment/', include('payments.urls')),
    path('address/', include('addresses.urls')),
    path('auth/', include('Auth.urls')),
    path('library/', include('library.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
