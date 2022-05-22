from rest_framework.urls import urlpatterns, path
from .views import LoginView, Protected, UserCreateView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('protected/', Protected.as_view()),
    path('create/', UserCreateView.as_view())
]