import pytest
import time

from api.user_api import UsersAPI


BASE_URL = "https://reqres.in"


@pytest.mark.api
def test_get_user():

    api = UsersAPI(BASE_URL)

    response = api.get_user(2)

    assert response.status_code == 200

    data = response.json()

    assert data["data"]["id"] == 2


@pytest.mark.api
def test_get_users():

    api = UsersAPI(BASE_URL)

    response = api.get_users(2)

    assert response.status_code == 200

    data = response.json()

    assert "data" in data

    assert len(data["data"]) > 0


@pytest.mark.api
def test_create_user():
    time.sleep(5)  
    api = UsersAPI(BASE_URL)

    response = api.create_user(
        "Sanskar",
        "QA Automation Engineer"
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Sanskar"

    assert data["job"] == \
        "QA Automation Engineer"


@pytest.mark.api
def test_update_user():  
    time.sleep(5)  



    api = UsersAPI(BASE_URL)

    response = api.update_user(
        2,
        "Sanskar Updated",
        "Automation Tester"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == \
        "Sanskar Updated"


@pytest.mark.api
def test_delete_user():   
    time.sleep(2)  



    api = UsersAPI(BASE_URL)

    response = api.delete_user(5)

    assert response.status_code == 204
