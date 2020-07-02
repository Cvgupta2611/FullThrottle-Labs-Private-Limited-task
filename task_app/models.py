from django.db import models

class Activity(models.Model):
    start_date = models.TextField(blank=True, null=True)
    end_date = models.TextField(blank=True, null=True)
    user_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity'


class UserTable(models.Model):
    id = models.IntegerField(primary_key=True)
    real_name = models.TextField()
    location = models.TextField()

    class Meta:
        managed = False
        db_table = 'user_table'



