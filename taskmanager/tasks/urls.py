from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('tasks/', views.TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', views.TaskRetrieveUpdateDeleteView.as_view(), name='task-detail'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
