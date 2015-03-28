from django.contrib.gis.db import models

# Create your models here.


class GeoDataLog(models.Model):
    latlng = models.GeometryField(spatial_index=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.GeoManager()
