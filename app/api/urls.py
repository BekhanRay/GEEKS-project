
from django.urls import path, include
from .views import ItemList, FilteredList

urlpatterns = [
    path('item/', ItemList.as_view()),
    path('item/get/', FilteredList.as_view()),
]