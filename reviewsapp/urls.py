from django.urls import path
from . import views

urlpatterns = [
    path('add-review/<int:reviewee_id>/<int:skill_id>/', views.add_review, name='add_review'),
    path('', views.review_list, name='review_list')

]
