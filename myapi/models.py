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
        century = self[6:7]
        if int(century) == 3 or int(century) == 4:
            year = '19' + year
            iin_convert = year + '-' + month + '-' + day # 1999-03-29
            iin_convert = datetime.datetime.strptime(iin_convert, '%Y-%m-%d')
            return iin_to_age(iin_convert)
        elif int(century) == 5 or int(century) == 6:
            year = '20' + year
            iin_convert = year + '-' + month + '-' + day
            iin_convert = datetime.datetime.strptime(iin_convert, '%Y-%m-%d')
            return iin_to_age(iin_convert)

    def __str__(self):
        return self.iin

    def get_age(self):
        return self.age
