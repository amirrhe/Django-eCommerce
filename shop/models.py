from django.db import models
class products(models.Model):
    title =  models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300) # using charfield instead of image field becuse to put link of image in this field 
    def __str__(self) -> str:
        return self.title