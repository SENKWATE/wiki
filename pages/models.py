from django.db import models
from django.urls import reverse
# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    last_update = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        #return "/page/%i/" % self.id
        return reverse('page-detail', kwargs={'page_id':self.id})
        #return reverse('page-detail', args=[str(self.id)])

    def __str__(self):
        return self.title
