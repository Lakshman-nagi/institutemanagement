from django.db import models

# Create your models here.
class City(models.Model):
    City_Name=models.CharField(max_length=50)

    def __str__(self):
        return f'{self.City_Name}'
class Course(models.Model):
    Course_Name=models.CharField(max_length=50)

    def __str__(self):
        return  f'{self.Course_Name}'
class Student(models.Model):
    Std_Name=models.CharField(max_length=50)
    Std_Age=models.IntegerField()
    Std_Phno=models.BigIntegerField()
    Std_City=models.ForeignKey(City,on_delete=models.CASCADE)
    Std_Course=models.ForeignKey(Course,on_delete=models.CASCADE)


