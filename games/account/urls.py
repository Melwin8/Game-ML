from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='user-registration'),
    path('user-login/', views.UserloginView.as_view(), name='user-token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('TenseQuiz/', views.QuizAPIView.as_view(), name='quiz_api'),
    path('boggle/',views.BoggleGameAPIView.as_view(), name='boggle_game'),
    path('word-shuffle/', views.WordShuffleChallengeAPIView.as_view(), name='word-shuffle-challenge'),
]
