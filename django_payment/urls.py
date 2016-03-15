
from django.conf.urls import url
from django.contrib import admin
from payments import views
from django.conf import settings
from django.conf.urls.static import static
from profiles import views as profile_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.provider_list),
    url(r'^$', profile_views.profile_list),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
