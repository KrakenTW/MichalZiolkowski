from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.views import serve
from django.urls import include, path
from django.conf import settings

admin.autodiscover()

urlpatterns = [
    path("admin/", admin.site.urls),
    path("services/", include("services.urls")),
    path("accounts/", include("accounts.urls")),
    path("", include("providers.urls")),
    path("reservation/", include("reservation.urls")),

    # Heroku
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
