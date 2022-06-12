from unicodedata import name
from django.db import models

# Create your models here.

OCCUPATION_CHOICES = (
    ('Student', 'Student'),
    ('Employee', 'Employed'),
    ('Freelancer', 'Freelancer'),
    ('Unemployed', 'Unemployed'),
    ('others', 'others')
)
STATE_CHOICES = (
    ('Assam', 'Assam'),
    ('Delhi', 'Delhi'),
    ('Kolkata',' Kolkata'),
    ('Hyderabad', 'Hyderabad'),
)
PLAN_CHOICES = (
    ('Silver(1 month)', 'Silver(1 month)'),
    ('Gold(6 Months)', 'Gold(6 Months)'),
    ('Diamond(1 year)', 'Diamond(1 year)'),
)
SHIFT_CHOICES = (
    ('Morning(5:00 am - 8:00 am)', 'Morning(5:00 am - 8:00 am)'),
    ('Evening(4:00 am - 7:00 pm)', 'Evening(4:00 am - 7:00 pm)'),
)

EQUIP_CATEGORY = (
    ('Free weights','Free weights'),
    ('Machines', 'Machines'),
    ('Racks', 'Racks')
)

class Member(models.Model):
    member_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    dob = models.DateField(default='dd/mm/yyyy')
    occupation = models.CharField(max_length=20, choices=OCCUPATION_CHOICES, default='choose')
    phone = models.IntegerField()
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=15, choices=STATE_CHOICES, default='choose')
    zip = models.IntegerField()
    plan = models.CharField(max_length=40, choices=PLAN_CHOICES, default='choose')
    shift = models.CharField(max_length=30, choices=SHIFT_CHOICES, default='choose')

class Equipments(models.Model):
    equi_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30, choices=EQUIP_CATEGORY, default='choose')
    quantity = models.IntegerField()