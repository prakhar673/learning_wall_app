from django.conf.urls import url
from django.conf.urls import include
from . import views
import notifications.urls

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'post/',views.post,name='post'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^like/$', views.like, name='like'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^approve/$', views.approve, name='approve'),
    url(r'^reject/$', views.reject, name='reject'),
    url(r'^notifications/', include(notifications.urls, namespace='notifications')),
    url(r'^notify/$', views.notifications, name='notify')

]