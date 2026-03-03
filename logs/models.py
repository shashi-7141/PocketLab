from django.db import models
from django.urls import reverse


class ExperimentLog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    details = models.TextField()
    observations = models.TextField()
    results = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.title} ({self.date})"

    def get_absolute_url(self):
        return reverse('logs:detail', kwargs={'pk': self.pk})