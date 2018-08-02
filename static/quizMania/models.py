from django.db import models


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
