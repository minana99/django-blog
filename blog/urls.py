from django.urls import path
from .views import index,IndexView,BlogListView

urlpatterns = [
    path('', index, name="index"),
    path('asview', IndexView.as_view(), name="indexview"),
    path('blog_list', BlogListView.as_view(), name="blog_list"),
]