
from django.urls import path

from .import views

urlpatterns = [
   path('', views.home, name="home"),
   path('about/', views.about, name="about"),
   path('propertygrid/', views.propertygrid, name="propertygrid"),
   path('propertysingle/', views.propertysingle, name="propertysingle"),
   path('contact/', views.contact, name="contact"),
   path('blog/', views.blog, name="blog"),
   path('agentsgrid/', views.agentsgrid, name="agentsgrid"),
   path('agentsingle/', views.agentsingle, name="agentsingle"),

]
