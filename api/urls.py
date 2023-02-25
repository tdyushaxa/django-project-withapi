from django.urls import path

from api.views import ProjectsPageApiView,ProjectsDetailPageApiView

urlpatterns=[
    path('',ProjectsPageApiView.as_view(),name='project_api'),
    path('detail/<int:pk>',ProjectsDetailPageApiView.as_view(),name='project_detail-api')
]