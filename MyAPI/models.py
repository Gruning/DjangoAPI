from django.db import models
from django.db.models.enums import Choices

class aprovals(models.Model):
    GENDER_CHOICES = (
        ('Female','Female'),
        ('Male','Male')   
    )
    MARRIED_CHOICES = (
        ('Yes','Yes'),
        ('No','No')   
    )
    GRADUATED_CHOICES = (
        ('Graduated','Graduated'),
        ('Not_Graduated','Not_Graduated')   
    )
    SELFEMPLOYED_CHOICES = (
        ('Yes','Yes'),
        ('No','No')   
    )
    PROPERTY_CHOICES = (
        ('Rural','Rural'),
        ('SemiUrban','SemiUrban'),
        ('Urban','Urban') 
    )

    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    dependants = models.IntegerField()
    applicantincome = models.IntegerField()
    coapplicantincome = models.IntegerField()
    loanamt = models.IntegerField()
    loantern = models.IntegerField()
    credithistory = models.IntegerField()
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    married = models.CharField(max_length=15, choices=MARRIED_CHOICES)
    graduatededucation = models.CharField(max_length=15, choices=GRADUATED_CHOICES)
    selfemployed = models.CharField(max_length=15, choices=SELFEMPLOYED_CHOICES)
    area = models.CharField(max_length=15, choices=PROPERTY_CHOICES)

def __str__(self):
    return self.firstname