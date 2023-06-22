from django.urls import path
from .views import index,IndexView

urlpatterns = [
    path('', index, name="index"),
    path('asview', IndexView.as_view(), name="indexview"),
]