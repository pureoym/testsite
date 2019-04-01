from django.db import models


#########################
####### METHOD 1 ########
#########################
class Story(models.Model):
    sid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=256, null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'cs_story'
        managed = False


class Person(models.Model):
    pid = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=256)
    story = models.ForeignKey(Story, related_name='person', on_delete=None)

    def __str__(self):
        # return str(self.pid)
        return str(self.pname)

    class Meta:
        db_table = 'cs_person'
        managed = False


#########################
####### METHOD 2 ########
#########################