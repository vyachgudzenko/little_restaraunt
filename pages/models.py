from django.db import models
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField('Name',max_length=200)
    email = models.EmailField(verbose_name='Email')
    subject = models.CharField('Subject',max_length=200)
    message = models.CharField('Message',max_length=500)
    date_added = models.DateField(verbose_name='Дата создания',
                                  auto_now_add=True)
    status = models.BooleanField(verbose_name='Status',default=False)
    def __str__(self):
        return self.subject
