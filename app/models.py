# Create your models here.
from django.db import models
from django.core.validators import EmailValidator
# Create your models here.

class Professor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)#
    email = models.EmailField(max_length=254, validators=[EmailValidator()])#
    p = models.BooleanField()#

    def __str__(self):
        return self.first_name ,self.last_name , self.email , self.p



##########################################################################
class Course(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    session = models.CharField(max_length=100)
    Mr = models.CharField(max_length=100)
    duration = models.IntegerField()



    def __str__(self):
        return self.name




##########################################################################
class Year_student(models.Model):

    DAYS_OF_WEEK = [
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
    ]
    name_collage = models.CharField(max_length=10)
    current_year=models.IntegerField()##
    year_of_student=models.IntegerField()
    number_of_days = models.IntegerField()##
    number_of_first_session_student= models.IntegerField()##
    number_of_first_session_category=models.IntegerField()##
    number_of_second_session_student= models.IntegerField()##
    number_of_second_session_category=models.IntegerField()##    
    holiday = models.CharField(max_length=10, choices=DAYS_OF_WEEK, null=True, blank=True) 
    
    def __str__(self):
        return self.name , self.number_of_student ,self.size




#######################################################################
class Room(models.Model):
    name = models.CharField(max_length=10)
    number_of_student=models.IntegerField()##
    lab = models.BooleanField()
    size = models.IntegerField()

    def __str__(self):
        return self.name , self.number_of_student ,self.size


#######################################################################
class Group(models.Model):
    name = models.CharField(max_length=10)
    size = models.IntegerField()

    def __str__(self):
        return self.name , self.size



#########################################################################

class Class(models.Model):
    seesion_on_years= [
        ('first', 'first'),
        ('first', 'first'),
 
    ]
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    duration = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    lab = models.BooleanField(default=False)
    session =models.CharField(max_length=10, choices=seesion_on_years, null=False, blank=True) 
    
    def __str__(self):
        return f"{self.course.name} by {self.professor.name}"
