from django.urls import path, include

from .views import GenerateRandomUserView, UsersListView

urlpatterns = [
    path('', UsersListView.as_view(), name='users_list'),
    path('generate', GenerateRandomUserView.as_view(), name='generate'),
]