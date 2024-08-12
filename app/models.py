# Create your models here.
from django.db import models
from django.core.validators import EmailValidator
# Create your models here.

#######################################################################
class Room(models.Model):
    name = models.CharField(max_length=10)
    number_of_student=models.IntegerField()##
    lab = models.BooleanField()
    size = models.IntegerField()

    def __str__(self):
        return self.name , self.number_of_student ,self.size


##########################################################################
class Course(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    professor = models.CharField(max_length=100)
    session = models.CharField(max_length=100)
    Mr = models.CharField(max_length=100,default="fade")
    duration = models.IntegerField()

    def __str__(self):
        return self.name




#########################################################################
class Professor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)#
    email = models.EmailField(max_length=254, validators=[EmailValidator()])#
    email_second =models.EmailField(max_length=254, validators=[EmailValidator()])
    password = models.IntegerField()
    p = models.BooleanField()#

    def __str__(self):
        return self.first_name ,self.last_name , self.email , self.p




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
    number_of_day=models.IntegerField()
    number_of_student_of_first_year_first_session = models.IntegerField()##
    number_of_student_of_first_year_second_session= models.IntegerField()##
    number_of_category_of_first_year_first_session=models.IntegerField()##
    number_of_category_of_first_year_second_session= models.IntegerField()##

    number_of_student_of_second_year_first_session = models.IntegerField()##
    number_of_student_of_second_year_second_session= models.IntegerField()##
    number_of_category_of_second_year_first_session=models.IntegerField()##
    number_of_category_of_second_year_second_session= models.IntegerField()##

    number_of_student_of_third_year_first_session = models.IntegerField()##
    number_of_student_of_third_year_second_session= models.IntegerField()##
    number_of_category_of_third_year_first_session=models.IntegerField()##
    number_of_category_of_third_year_second_session= models.IntegerField()##

    number_of_student_of_fourth_year_first_session = models.IntegerField()##
    number_of_student_of_fourth_year_second_session= models.IntegerField()##
    number_of_category_of_fourth_year_first_session=models.IntegerField()##
    number_of_category_of_fourth_year_second_session= models.IntegerField()##

    number_of_student_of_fith_year_first_session = models.IntegerField()##
    number_of_student_of_fith_year_second_session= models.IntegerField()##
    number_of_category_of_fith_year_first_session=models.IntegerField()##
    number_of_category_of_fith_year_second_session= models.IntegerField()##
    number_of_day=models.IntegerField()##    
    holiday = models.CharField(max_length=10, choices=DAYS_OF_WEEK, null=True, blank=True) 
    
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
