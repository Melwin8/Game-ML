from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='user-registration'),
    path('user-login/', views.UserloginView.as_view(), name='user-token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('quiz/', views.QuizAPIView.as_view(), name='quiz'),
    path('api/boggle/', views.BoggleGameView.as_view(), name='boggle_game'),
]
