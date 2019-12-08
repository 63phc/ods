from django.urls import path

from src.apps.panel.views import ClaimListView, ClaimDetailView, ClaimCreateView

urlpatterns = [
    path('list/', ClaimListView.as_view(), name='claim-list'),
    path('add/', ClaimCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', ClaimDetailView.as_view(), name='detail'),
]
