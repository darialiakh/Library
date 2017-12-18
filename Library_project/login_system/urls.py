from django.conf.urls import url, include
from . import views


urlpatterns = [
            url(r'^register/$', views.RegisterFormView.as_view(), name='register'),
            url(r'^login/$', views.LoginFormView.as_view(), name='login'),
            url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
            url(r'^password/$', views.ChangePasswordView, name='change_password'),
            url('social-auth/', include('social_django.urls', namespace='social')),
]