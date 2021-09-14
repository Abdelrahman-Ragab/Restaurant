from django.db import models

# Create your models here.


class Table(models.Model):

    select_day = [
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
    ]

    select_hour = [
        ('10:00','10:00'),
        ('12:00','12:00'),
        ('14:00','14:00'),
        ('16:00','16:00'),
        ('18:00','18:00'),
        ('20:00','20:00'),
        ('22:00','22:00'),
    ]

    person_number = [
        ('1-Person','1-Person'),
        ('2-Persons','2-Persons'),
        ('3-Persons','3-Persons'),
        ('4-Persons','4-Persons'),
        ('5-Persons','5-Persons'),
        ('6-Persons','6-Persons'),
        ('7-Persons','7-Persons'),
    ]

    Select_Day = models.CharField(max_length = 50 , choices = select_day , null=True , blank = True)
    Select_Hour = models.CharField(max_length = 50 , choices = select_hour , null=True , blank = True)
    Full_Name = models.CharField(max_length = 100)
    Phone_Number = models.CharField(max_length = 11)
    How_Many_Persons = models.CharField(max_length = 50 , choices = person_number , null=True , blank = True)

    def __str__(self):
        return self.Full_Name




class Email(models.Model):
    email = models.EmailField(max_length = 100)

    def __str__(self):
        return self.email




class Contact(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    phone = models.CharField(max_length = 11)
    message = models.TextField(max_length = 500)

    def __str__(self):
        return self.name
    



class Break(models.Model):
    image = models.ImageField(upload_to='photos' , null=True , blank = True)
    price = models.DecimalField(max_digits=5 , decimal_places=2)
    name = models.CharField(max_length=100)
    details = models.TextField(max_length=1000)

    def __str__(self):
        return self.name




class Lunch(models.Model):
    image = models.ImageField(upload_to='photos' , null=True , blank = True)
    price = models.DecimalField(max_digits=5 , decimal_places=2)
    name = models.CharField(max_length=100)
    details = models.TextField(max_length=1000)

    def __str__(self):
        return self.name



class Dinner(models.Model):
    image = models.ImageField(upload_to='photos' , null=True , blank = True)
    price = models.DecimalField(max_digits=5 , decimal_places=2)
    name = models.CharField(max_length=100)
    details = models.TextField(max_length=1000)

    def __str__(self):
        return self.name



class Dessert(models.Model):
    image = models.ImageField(upload_to='photos' , null=True , blank = True)
    price = models.DecimalField(max_digits=5 , decimal_places=2 , null=True , blank = True)
    name = models.CharField(max_length=100 , null=True , blank = True)
    details = models.TextField(max_length=1000 , null=True , blank = True)

    def __str__(self):
        return self.name




class Food(models.Model):
    meal = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos' , null=True , blank = True)
    price = models.DecimalField(max_digits=5 , decimal_places=2)
    name = models.CharField(max_length=100)
    details = models.TextField(max_length=1000)

    def __str__(self):
        return self.meal






class Post(models.Model):
    date = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos' , null=True , blank = True)
    name = models.CharField(max_length=100)
    admin = models.CharField(max_length=100)
    details = models.TextField(max_length=1000)


    def __str__(self):
        return self.name



class Blog(models.Model):
    date = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos' , null=True , blank = True)
    name = models.CharField(max_length=100)
    admin = models.CharField(max_length=100)
    details = models.TextField(max_length=1000)


    def __str__(self):
        return self.name





class Service(models.Model):
    image = models.ImageField(upload_to='photos' , null=True , blank = True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

