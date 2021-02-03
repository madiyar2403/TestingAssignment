from django.core.validators import RegexValidator
from rest_framework import serializers

from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    iin = serializers.CharField(
        validators=[RegexValidator(regex='^[0-9]{12}$',
                                   message='Length of iin must be 12',
                                   code='nomatch')], max_length=12, required=True)
    age = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Person
        fields = ('iin', 'age',)

    def get_age(self, person):
        return person.calculate_age

