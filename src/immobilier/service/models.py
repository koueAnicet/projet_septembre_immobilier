from django.contrib.auth import get_user_model
from django.db import models

from immobilier.authentication.views import user_property


class Status(models.Model):
    name = models.CharField()
    def __str__(self) -> str:
        return self.name

class City(models.Model):
    name = models.CharField()
    def __str__(self) -> str:
        return self.name

class State(models.Model):
    name = models.CharField()
    def __str__(self) -> str:
        return self.name


class SubmitProperty(models.Model):
    user_property_submit = get_auth_model()
    image_first = models.FieldFile(upload_to='image_first')
    name=models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    description =HTMLField()
    state = models.ForeignKey(
        'service.state',
        on_delete=models.SET_DEFAULT,
        related_name='properti_state',
    )
    city = models.ForeignKey(
        'service.city',
        on_delete=models.SET_DEFAULT,
        related_name='property_city',
    )
    status = models.ForeignKey(
     'service.status',
        on_delete=models.SET_DEFAULT,
        related_name='property_status',
    )
    bed_numbers=models.PositiveBigIntegerField()
    bath_numbers=models.PositiveBigIntegerField()
    area_numbers=models.PositiveBigIntegerField()
    image1 = models.FileField(upload_to='img1',blank=True, null=True)
    image2 = models.FileField(upload_to='img2',blank=True, null=True)
    image3 = models.FileField(upload_to='img3',blank=True, null=True)
    image4 = models.FileField(upload_to='img4',blank=True, null=True)
    videos = models.URLField(blank=True, null=True)
    videos2 = models.FieldFile(upload_to='videos2', blank=True, null=True)
    accept_condition = models.BooleanField(default=False)
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'SubmitProperty'
        managed = True
        verbose_name = 'SubmitProperty'
        verbose_name_plural = 'SubmitProperties'
