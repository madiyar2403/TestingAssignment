from django.db import models
from django.core.validators import RegexValidator
import datetime


# Create your models here.


class Person(models.Model):
    iin = models.CharField(
        validators=[RegexValidator(regex='^.{12}$', message='Length of iin must be 12', code='nomatch')], max_length=12)
    age = models.IntegerField(default=0)

    def calculate_age(self):
        def iin_to_age(self):
            today = datetime.date.today()
            return today.year - self.year - ((today.month, today.day) < (self.month, self.day))
        year = self[0:2]
        month = self[2:4]
        day = self[4:6]
        if int(year) > 21:
            year = '19' + year
            iin_convert = year + '-' + month + '-' + day
            iin_convert = datetime.datetime.strptime(iin_convert, '%Y-%m-%d')
            return iin_to_age(iin_convert)
        elif int(year) <= 21:
            year = '20' + year
            iin_convert = year + '-' + month + '-' + day
            iin_convert = datetime.datetime.strptime(iin_convert, '%Y-%m-%d')
            return iin_to_age(iin_convert)

    def __str__(self):
        return self.iin

    def get_age(self):
        return self.age
