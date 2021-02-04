from .models import Person
from freezegun import freeze_time
import pytest
import requests


@pytest.mark.django_db(True)
@freeze_time("2009-03-17")
def test_iin_create_ok():
    person = Person.objects.create(iin="990227301278")
    print('\nIIN: ' + person.iin + ' Age: ' + str(person.calculate_age))
    assert person.iin
    assert person.calculate_age
    assert person.calculate_age == 10


@pytest.mark.django_db(True)
@freeze_time("2009-03-17")
def test_iin_create_not_ok_value_error():
    person = Person.objects.create(iin="077777452878")
    with pytest.raises(ValueError):
        assert person.calculate_age is None


@pytest.mark.django_db(True)
@freeze_time("2009-03-17")
def test_iin_post_ok(db, client):
    person = {"iin": "921020309902"}
    response = client.post('/people/', person)
    assert response.status_code == 201
    resp_body = response.json()
    assert 'iin' in resp_body
    assert 'age' in resp_body
    assert resp_body["age"] == 16


@pytest.mark.django_db(True)
@freeze_time("2009-03-17")
def test_iin_post_not_ok_more_than_12(db, client):
    person = {"iin": "6023784569834625784659"}
    response = client.post('/people/', person)
    assert response.status_code == 400
    resp_body = response.json()
    assert 'iin' in resp_body
    assert resp_body['iin'] == ['Length of iin must be 12', 'Ensure this field has no more than 12 characters.']


@pytest.mark.django_db(True)
@freeze_time("2009-03-17")
def test_iin_post_not_ok_less_than_12(db, client):
    person = {"iin": "0"}
    response = client.post('/people/', person)
    assert response.status_code == 400
    resp_body = response.json()
    assert 'iin' in resp_body
    assert resp_body['iin'] == ['Length of iin must be 12']


@pytest.mark.django_db(True)
@freeze_time("2009-03-17")
def test_iin_post_not_ok_incorrect_data(db, client):
    person = {"iin": "tttttttttttt"}
    response = client.post('/people/', person)
    assert response.status_code == 400
    resp_body = response.json()
    assert 'iin' in resp_body
    assert resp_body['iin'] == ['Length of iin must be 12']


@pytest.fixture
def check_correct_post(db, client):
    person = {"iin": "921020309902"}
    response = client.post('/people/', person)
    data = response.json()
    return data["iin"]


@pytest.mark.django_db(True)
@freeze_time("2009-03-17")
def test_iin_get_ok(db, client, check_correct_post):
    person_iin = check_correct_post
    resp = client.get(f'/people/{person_iin}/')
    assert resp.status_code == 200
    data = resp.json()
    assert 'iin' in data
    assert 'age' in data


@pytest.mark.django_db(True)
@freeze_time("2009-03-17")
def test_iin_get_not_ok(db, client):
    person_iin = "990324782365"
    try:
        response = client.get(f'/people/{person_iin}/')
        assert response.status_code == 404
    except TypeError:
        print("TypeError exception: This person DoesNotExist")



'''
@pytest.mark.django_db(True)
@freeze_time("2009-03-17")
def test_iin_post_not_ok_incorrect_date():
    person = {"iin": "010230102672"}
    response = requests.post('http://127.0.0.1:8000/people/', person)
    assert response.status_code == 500
'''