from django.urls import path

from src.apps.account.views import SignInPageView

urlpatterns = [
    path('', SignInPageView.as_view(), name='sign-in'),
]
