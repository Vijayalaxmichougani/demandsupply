"""sample1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from two.views import index
from two.views import demand
from two.views import supply
from two.views import ul
from two.views import one
from two.views import two
from two.views import three
from two.views import final
from two.views import final1
from two.views import usersform

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name="index"),
    path("demand/", demand, name="demand"),
    path("supply/", supply, name="supply"),
    path("ul/", ul, name="ul"),
    path("one/", one, name="one"),
    path("two/", two, name="two"),
    path("three/", three, name="three"),
    path("final/", final, name="final"),
    path("final1/", final1, name="final1"),
    path("usersform/", usersform, name="usersform"),

]
