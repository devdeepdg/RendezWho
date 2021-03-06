from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    userID = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=50)
    requests = models.CharField(max_length=1000)
    email = models.CharField(max_length=50)

class Schedule_Entry(models.Model):
    entryID = models.BigAutoField(primary_key=True)
    activity = models.CharField(max_length=50)
    time = models.TimeField(auto_now_add=True,blank=True)
    date = models.DateField(auto_now_add=True, blank=True)

class Location(models.Model):
    coordinate = models.CharField(primary_key=True,max_length=50)
    name = models.CharField(max_length=50)

class Meeting(models.Model):
    privacy = models.BooleanField()
    meetingID = models.BigAutoField(primary_key=True)
    time = models.TimeField(auto_now_add=True, blank=True)
    date = models.DateField(auto_now_add=True, blank=True)
"""
class ParticipantOf(models.Model):
    userID = models.ForeignKey('User.userID')
    meetingID = models.ForeignKey('Meeting.meetingID')

class Connection(models.Model):
    userID1 = models.ForeignKey('User.userID')
    userID2 = models.ForeignKey('User.userID')

class Has (models.Model):
    userID = models.ForeignKey('User.userID')
    entryID = models.ForeignKey('User.entryID')

class LocatedAt (models.Model):
    entryID = models.ForeignKey('User.entryID')
    coordinate = models.ForeignKey('Location.coordinate')

class isAt (models.Model):
    meetingID = models.ForeignKey('Meeting.meetingID')
    coordinate = models.ForeignKey('Location.coordinate')

"""