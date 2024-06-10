from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    # string representation for tasks in admin
    def __str__(self):
        return self.name

