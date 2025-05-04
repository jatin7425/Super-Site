from django.db import models
from django.contrib.auth.models import User

class LearningEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    shared_with = models.ManyToManyField(User, related_name='shared_learnings', blank=True)
    is_completed = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    def soft_delete(self):
        from django.utils import timezone
        self.deleted_at = timezone.now()
        self.save()