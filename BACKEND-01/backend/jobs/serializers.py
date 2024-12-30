from rest_framework import serializers
from .models import Job


class JobCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = [
            'custom_id', 'title', 'company', 'location', 'category', 'qualifications',
            'job_type', 'short_description', 'salary', 'posted', 'content'
        ]
        
class JobDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job 
        fields = [
            'custom_id', 'content', 'qualifications'
        ]
        
class CategorySerializer(serializers.Serializer):
    category = serializers.CharField()
    job_count = serializers.SerializerMethodField()

    def get_job_count(self, obj):
        return Job.objects.filter(category=obj['category']).count()