from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, ListAPIView
from .models import Job
from django.db.models import Count
from .serializers import JobCardSerializer, JobDetailSerializer, CategorySerializer


class JobCardView(ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobCardSerializer
    
    
class JobDetailView(RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobDetailSerializer
    
    lookup_field = 'custom_id'
    
class CategoryJobCountView(ListAPIView):
    serializer_class = CategorySerializer
    
    def get_queryset(self):
        return Job.objects.values('category').annotate(job_count=Count('id')).order_by('category')