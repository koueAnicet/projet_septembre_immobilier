from unicodedata import name
from django.urls import path
from authentication import views


urlpatterns = [
    
    path('login/', views.LoginView.as_view(), name="login"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('submit-property/', views.submit_property, name='submit-property'),
    path('user-properties/', views.user_property, name='user-property'),
    path('user-logout/', views.logout_user_auth, name='user-logout'),
    path('active/<uidb64>/<token>/', views.active, name='active'),
    
]
