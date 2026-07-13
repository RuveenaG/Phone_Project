from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
path('', views.storehome, name='storehome'),
path('aboutus', views.aboutus, name='aboutus'),
path('reviews', views.reviews, name='reviews'),
path('campaign', views.campaign, name='campaign'),
]
# Add static files support
