"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from django.contrib import admin
from django.urls import path
from db.views import generate_pdf

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    #path('generate-pdf', views.generate_pdf, name='generate-pdf')
=======
    path('generate-pdf', generate_pdf, name='generate-pdf')
>>>>>>> 048447c324303eed5b03bcd6aba9bf04cb553522
]


urlpatterns += [
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]


