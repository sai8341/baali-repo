from django.urls import path
from .views import JobCardView, JobDetailView, CategoryJobCountView


urlpatterns = [
    path('job-listings/', JobCardView.as_view(), name="job-card-view"),
    path('job-details/<uuid:custom_id>/', JobDetailView.as_view(), name="job-details"),
    path('job-categories/', CategoryJobCountView.as_view(), name='category-job-count-view')
]
