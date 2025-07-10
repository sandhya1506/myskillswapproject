from django.conf.urls import url
from user_authentication import views

app_name = 'user_authentication'

urlpatterns = [
    url(r'^register/$', views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]