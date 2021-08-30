"""learn_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from my_application.views import hello

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',hello,name='hello') # Empty url path that ensures that first page opened is the hello function http response. "Acts as homepage"
    path('my_application/',include('my_application.urls')), # the urlpattern list can add the route created in the my_application directory. This links the urlpatterns list to the main urlpatterns list. This prevents cluttering of the main urlpattern list. Routes from my_application.url list all have a base route "my_application/"
]



