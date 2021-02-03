from datetime import date
from .models import Person
from freezegun import freeze_time
from dateutil.relativedelta import *
import pytest
import requests


@pytest.mark.django_db(True)
@freeze_time("2009-03-17")
def test_iin_create_ok():
    person = Person.objects.create(iin="990227301278")
    print('\nIIN: ' + person.iin + ' Age: ' + str(person.calculate_age))
    assert person.iin
    assert person.calculate_age



@pytest.mark.django_db(True)
@freeze_time("2009-03-17")
def test_iin_create_not_ok_value_error():
    person = Person.objects.create(iin="077777452878")
    with pytest.raises(ValueError):
        assert person.calculate_age is None


@pytest.mark.django_db(True)
@freeze_time("2009-03-17")
def test_iin_post_ok():
    person = {"iin": "921020309902"}
    response = requests.post('http://127.0.0.1:8000/people/', person)
    assert response.status_code == 201
    resp_body = response.json()
    assert 'iin' in resp_body
    assert 'age' in resp_body


@pytest.mark.django_db(True)
@freeze_time("2009-03-17")
def test_iin_post_not_ok_more_than_12():
    person = {"iin": "6023784569834625784659"}
    response = requests.post('http://127.0.0.1:8000/people/', person)
    assert response.status_code == 400


@pytest.mark.django_db(True)
@freeze_time("2009-03-17")
def test_iin_post_not_ok_less_than_12():
    person = {"iin": "0"}
    response = requests.post('http://127.0.0.1:8000/people/', person)
    assert response.status_code == 400


@pytest.mark.django_db(True)
@freeze_time("2009-03-17")
def test_iin_post_not_ok_incorrect_data():
    person = {"iin": "tttttttttttt"}
    response = requests.post('http://127.0.0.1:8000/people/', person)
    assert response.status_code == 400


@pytest.mark.django_db(True)
@freeze_time("2009-03-17")
def test_iin_get_ok():
    person_iin = "921020309902"
    response = requests.get(f'http://127.0.0.1:8000/people/{person_iin}/')
    assert response.status_code == 200
    data = response.json()
    assert 'iin' in data
    assert 'age' in data


@pytest.mark.django_db(True)
@freeze_time("2009-03-17")
def test_iin_get_not_ok():
    person_iin = "777777777777"
    response = requests.get(f'http://127.0.0.1:8000/people/{person_iin}/')
    assert response.status_code == 500


'''
@pytest.mark.django_db(True)
@freeze_time("2009-03-17")
def test_iin_post_not_ok_incorrect_date():
    person = {"iin": "010230102672"}
    response = requests.post('http://127.0.0.1:8000/people/', person)
    assert response.status_code == 500
'''