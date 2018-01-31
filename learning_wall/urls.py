from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^learning_wall/', include('learning_wall_app.urls')),
    url(r'^admin/', admin.site.urls),
]
