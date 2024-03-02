from django.contrib import admin
from django.urls import include, path,re_path

from polls.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('polls.urls',namespace="home") ),
    re_path(r'^categories/',include('polls.urls',namespace="categories")), 
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
