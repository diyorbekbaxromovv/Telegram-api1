from django.urls import path
from .views import SignUpView,VerifyView

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('verify/', VerifyView.as_view()),
    
]
