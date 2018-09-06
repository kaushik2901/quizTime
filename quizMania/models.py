from django.db import models
from django.contrib.gis.db import models as geomodels


class Users(models.Model):
    rollNumber = models.CharField(max_length=16)
    key = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(self.id) + " -> " + str(self.rollNumber) + " -> " + str(self.key)
    def __unicode__(self):
        return str(self.id)

class UserStatus(models.Model):
    user = models.ForeignKey('Users', on_delete=models.CASCADE)
    ruleDisplay = models.BooleanField(default=True)
    completed = models.BooleanField(default=False)
    answeredQuestions = models.CharField(max_length=2000, null=True, blank=True)
    points = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user.rollNumber) + " -> " + "completed : " + str(self.completed) + " -> " + "points : " + str(self.points)
    def __unicode__(self):
        return str(self.id)

class Questions(models.Model):
    MAX_ANS = 20

    questionString = models.CharField(max_length=2000)
    questionType = models.CharField(max_length=20)
    questionImage = models.ImageField(upload_to='.', null=True, blank=True)
    option1 = models.CharField(max_length=MAX_ANS, null=True, blank=True)
    option2 = models.CharField(max_length=MAX_ANS, null=True, blank=True)
    option3 = models.CharField(max_length=MAX_ANS, null=True, blank=True)
    option4 = models.CharField(max_length=MAX_ANS, null=True, blank=True)
    answer = models.CharField(max_length=MAX_ANS)
    points = models.IntegerField()


    def __str__(self):
        return str(self.id) + " -> " + str(self.questionType) + " -> " + str(self.questionString[:10])
    def __unicode__(self):
        return str(self.id)

class Rules(models.Model):
    ruleString = models.CharField(max_length=2000)

    def __str__(self):
        return str(self.id) + " -> " + str(self.ruleString)
    def __unicode__(self):
        return str(self.id)
    
    
class RoadMapping(models.Model):
    road_code = models.CharField(max_length=50)
    road_name = models.CharField(max_length=2000, null=True, blank=True)
    officer_id = models.IntegerField(default=0)
    lat1 = models.FloatField(default=0)
    lon1 = models.FloatField(default=0)
    lat2 = models.FloatField(default=0)
    lon2 = models.FloatField(default=0)

    def __str__(self):
        return str(self.road_code)
    def __unicode__(self):
        return str(self.id)
    
class Roads(geomodels.Model):
    name = geomodels.CharField(max_length=50)
    discription = geomodels.CharField(max_length=200, blank=True, null=True)
    road = geomodels.LineStringField(dim=3)
    
    def __str__(self):
        return str(self.name)
    def __unicode__(self):
        return str(self.id)
    
class Image(models.Model):
    image = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
