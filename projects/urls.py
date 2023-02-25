from django.urls import path

from .views import HomePageView, ProjectDetailPageView, AddProjectPageView, UpdateProjectPageView, \
    DeleteProjectPageView, EditReviewView,DeleteReviewView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('add-project/', AddProjectPageView.as_view(), name='add_project'),
    path('update/<int:pk>/', UpdateProjectPageView.as_view(), name='update_project'),
    path('delete/<int:pk>/', DeleteProjectPageView.as_view(), name='delete_project'),
    path('<int:pk>/', ProjectDetailPageView.as_view(), name='detail'),
    path('<int:project_id>/update/<int:review_id>', EditReviewView.as_view(), name='update_review'),
    path('<int:project_id>/delte/<int:review_id>', DeleteReviewView.as_view(), name='delete_review')
]
