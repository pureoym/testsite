from django.db import models


class Person(models.Model):
    pid = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=256)

    def __str__(self):
        return self.pname

    class Meta:
        db_table = 'cs_person'
        managed = False


class Story(models.Model):
    sid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=256, null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    person = models.ForeignKey(Person, on_delete=None)
    # person = models.ManyToManyField(Person, related_name='person_id', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'cs_story'
        managed = False
