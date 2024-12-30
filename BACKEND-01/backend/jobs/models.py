
import uuid
from django.db import models
from django.contrib.auth.models import User 
from tinymce.models import HTMLField

class Job(models.Model):
    custom_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=200, verbose_name="Job Title")
    company = models.CharField(max_length=200, verbose_name="Company Name")
    location = models.CharField(max_length=200, verbose_name="Location")
    job_type = models.CharField(max_length=50, verbose_name="Job Type", choices=[
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Freelance', 'Freelance'),
        ('Work-From-Home', 'Work-From-Home')
    ])
    short_description = models.TextField(verbose_name="Enter short description")
    
    
    category = models.CharField(max_length=50, choices=[
        ('Software Development', 'Software Development'),
        ('Data Engineering', 'Data Engineering'),
        ('Cloud Architecture', 'Cloud Architecture'),
        ('Cybersecurity', 'Cybersecurity'),
        ('DevOps', 'DevOps'),
        ('Network Engineering', 'Network Engineering'),
        ('AI & Machine Learning', 'AI & Machine Learning'),
        ('System Architecture', 'System Architecture'),
        ('Others', 'Others'),
    ])
    
    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    posted = models.DateTimeField(auto_now_add=True, verbose_name="Date Posted")
    
    # full_description = HTMLField(
    #     help_text="Enter the Full Job Data"
    # )
    content = HTMLField(
        help_text="Enter the Full Job Data"
    )
    

    salary = models.CharField(max_length=50, verbose_name="Salary range")
    qualifications = models.TextField(verbose_name="Enter qualifications")
    
    def __str__(self):
        return self.title
    