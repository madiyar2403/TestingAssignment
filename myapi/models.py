from dateutil.relativedelta import relativedelta
from django.db import models
from django.core.validators import RegexValidator
from freezegun import freeze_time

import datetime


@freeze_time("2009-03-17")
class Person(models.Model):
    iin = models.CharField(max_length=12, unique=True)

    @property
    def calculate_age(self):
        def iin_to_age(myself):
            today = datetime.date.today()
            try:
                return relativedelta(today, myself.date()).years
            except ValueError as e:
                return False

        year = self.iin[0:2]
        month = self.iin[2:4]
        day = self.iin[4:6]
        century = self.iin[6:7]
        if int(century) == 1 or int(century) == 2:
            year = '18' + year
            iin_convert = year + '-' + month + '-' + day
            iin_convert = datetime.datetime.strptime(iin_convert, '%Y-%m-%d')
            return iin_to_age(iin_convert)
        elif int(century) == 3 or int(century) == 4:
            year = '19' + year
            iin_convert = year + '-' + month + '-' + day
            iin_convert = datetime.datetime.strptime(iin_convert, '%Y-%m-%d')
            return iin_to_age(iin_convert)
        elif int(century) == 5 or int(century) == 6:
            year = '20' + year
            iin_convert = year + '-' + month + '-' + day
            iin_convert = datetime.datetime.strptime(iin_convert, '%Y-%m-%d')
            return iin_to_age(iin_convert)
        else:
            return None

    def __str__(self):
        return self.iin
