from django.db import models

# Create your models here.
class Sprajo(models.Model):
    Name = models.CharField(blank=True , max_length=70)
    Image= models.ImageField(blank=True,upload_to='uploads/')
    description = models.CharField(blank=True,max_length=400)
    capacity = models.IntegerField(null=False)
    unit = models.CharField(blank=True,max_length=5)
    price = models.IntegerField(blank=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural="product"

