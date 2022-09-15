from django.urls import path
from authentication import views


urlpatterns = [
    path('/', views.HomeView.as_view()),
    path('login/', views.RegisterView.as_view(), name="login"),
    path('register/', views.RegisterView.as_view(), name="register"),
]
