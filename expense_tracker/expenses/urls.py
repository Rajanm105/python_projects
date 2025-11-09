from django.urls import path
from .views import ExpenseListCreateAPIView, ExpenseDetailAPIView

urlpatterns = [
    path('expenses/', ExpenseListCreateAPIView.as_view(), name="expense-list-create"),
    path('expenses/<int:pk>/', ExpenseDetailAPIView.as_view(), name='expense-detail'),
]