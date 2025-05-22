# blog/models.py
from django.db import models
from django.conf import settings
from accounts.models import CustomUser


CATEGORY_CHOICES = [
    ('mental_health', 'Mental Health'),
    ('heart_disease', 'Heart Disease'),
    ('covid19', 'Covid19'),
    ('immunization', 'Immunization'),
]

class BlogPost(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    summary = models.TextField()
    content = models.TextField()
    is_draft = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def truncated_summary(self):
        words = self.summary.split()
        return ' '.join(words[:15]) + ('...' if len(words) > 15 else '')
