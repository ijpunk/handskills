from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

COUNTRIES = (
    ("NIGERIA", "Nigeria"),

)


OCCUPATIONS = (
    ("PLUMBER", "Plumber"),
    ("ELECTRICIAN", "Electrician"),
    ("CARPENTER", "Carpenter"),
    ("AC_REPAIRER", "AC repairer"),
    ("FASHION_DESIGNER", "Fashion designer"),
    ("HAIR_STYLIST", "Hair stylist"),
    ("BRICKLAYER", "Bricklayer"),
    ("PAINTER", "Painter"),
    ("WELDER", "Welder"),
    ("POP", "Pop"),
    ("FURNITURE", "Furniture"),
    ("Tiler", "Tiler"),
    ("INTERIOR DECORATOR", "Interior decorator"),
    ("GENERATOR REPAIRER", "Generator repairer"),
    ("TAILOR", "Tailor"),
    ("REFRIGERATOR REPAIRER", "Refrigerator repairer"),
    ("CLEANER", "Cleaner"),
    ("PEST TERMINATOR", "Pest terminator"),

)

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(default='default.png', upload_to='users/', 
                              blank=True, null=True)
    occupation = models.CharField(max_length=150, blank=True, choices=OCCUPATIONS)
    experience = models.IntegerField(blank=True, default=0)

    address = models.CharField(max_length=150, blank=True, null=True )
    phone = models.IntegerField(blank= True, null=True  )
    country = models.CharField(max_length=150, blank=True, null=True, choices=COUNTRIES )
    state = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True )
    artisan = models.BooleanField(default=False)
    client = models.BooleanField(default=False)


class Portfolio(models.Model):
    description = models.TextField( blank=True, null=True)
    mywork1  = models.CharField(max_length=50, blank=True)
    mywork2  = models.CharField(max_length=50, blank=True)
    mywork3  = models.CharField(max_length=50, blank=True)
    mywork4  = models.CharField(max_length=50, blank=False)
    portfolio1 = models.ImageField(default='default.png', upload_to='users/', 
                              blank=True, null=True)
    portfolio2 = models.ImageField(default='default.png', upload_to='users/', 
                              blank=True, null=True)
    portfolio3 = models.ImageField(default='default.png', upload_to='users/', 
                              blank=False, null=True)
    portfolio4 = models.ImageField(default='default.png', upload_to='users/', 
                              blank=False, null=True)



    def __str__(self):
        return f' {self.user.username} Profile'


