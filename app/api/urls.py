
from django.urls import path, include
from .views import ItemList

urlpatterns = [
    path('item/', ItemList.as_view())
]