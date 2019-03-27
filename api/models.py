from django.db import models


# Create your models here.
class Story(models.Model):
    sid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=256, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    # pid = models.ForeignKey(to="Person", to_field="pid", on_delete=None)
    # pub_time = models.DateTimeField(null=True, blans11k=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'cs_story'
        managed = False


class Person(models.Model):
    pid = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cs_person'
        managed = False
