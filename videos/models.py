from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name

class Video(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    thumbnail = models.FileField(blank=False, null=False)
    file = models.FileField(upload_to=('videos'), blank=False, null=False)
    fileName = models.CharField(max_length=150, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']

