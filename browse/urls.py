from django.urls import path
from .views import browse_view, reverse_browse_view

urlpatterns = [
    path('user/<str:username>/', browse_view, name='skills_by_user'),
    path('user/<str:username>/<str:skill_name>/', browse_view, name='skill_detail_from_user'),
    path('skill/<str:skill_name>/', reverse_browse_view, name='users_by_skill'),
    path('skill/<str:skill_name>/<str:username>/', reverse_browse_view, name='skill_detail_from_skill'),
]