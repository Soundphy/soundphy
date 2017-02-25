import pytest

from common import decode
from common import status
from common import sound_upload
from common import sound_details
from common import is_subdict
from common import incomplete_dict
from common import logged_in_client  # pragma: no flakes


@pytest.mark.django_db
def test_list_sounds_empty_database(client):
    """
    Listing sounds from an empty database should result in an empty list.
    Any client can make this request (no authentication needed).
    """
    response = client.get('/sounds/')
    assert status(response) == 'ok'
    assert decode(response) == []


@pytest.mark.django_db
def test_create_sound_not_authenticated(client):
    """
    Get a no existent sound in an empty database should result in 301 error.
    Any client can make this request (no authentication needed).
    """
    response = client.post('/sounds/', json={})
    assert status(response) == 'forbidden'


@pytest.mark.django_db
@pytest.mark.parametrize('data', incomplete_dict(sound_upload('a.ogg')))
def test_create_sound_autenticated_bad_request(logged_in_client, data):
    """
    When posting a new sound, if the information provided is incomplete,
    the server should response with a bad request status error.
    """
    # Make sure we never send an empty file... (otherwise the bad-request
    # response error could be caused by an empty file and could be hiding
    # the expected behavior)
    if 'sound' in data:
        data['sound'].seek(0)
    response = logged_in_client.post('/sounds/', data=data)
    assert status(response) == 'bad_request'


@pytest.mark.django_db
def test_create_sound_autenticated(logged_in_client):
    """
    Logged-in users should be able to upload new sounds if the data provided
    is complete.
    """
    response = logged_in_client.post('/sounds/', data=sound_upload('a.ogg'))
    assert status(response) == 'created'
    assert is_subdict(sound_details('a.ogg'), decode(response))


@pytest.mark.django_db
def test_sound_details_non_existent(client):
    """
    Requesting the sound details of a non-existent sound should result in
    a not-found error response.
    """
    response = client.get('/sounds/1/')
    assert status(response) == 'not_found'


@pytest.mark.django_db
def test_sound_details(client, logged_in_client):
    """
    Any user can request details about an uploaded sound. These details
    should contain complete information about the sound description and
    properties.
    """
    # Upload a sound while authenticated
    response = logged_in_client.post('/sounds/', data=sound_upload('a.ogg'))
    # Request details while not authenticated
    response = client.get('/sounds/1/')
    assert status(response) == 'ok'
    assert is_subdict(sound_details('a.ogg'), decode(response))


@pytest.mark.django_db
def test_list_sounds_filled_database(client, logged_in_client):
    """
    Listing sounds from a filled database should result in a non-empty list.
    Any client can make this request (no authentication needed).
    """
    # Upload a sound while authenticated
    logged_in_client.post('/sounds/', data=sound_upload('a.ogg'))
    logged_in_client.post('/sounds/', data=sound_upload('b.ogg'))
    # Request details while not authenticated
    response = client.get('/sounds/')
    assert status(response) == 'ok'
    response = decode(response)
    assert len(response) == 2
    assert is_subdict(sound_details('a.ogg'), response[0])
    assert is_subdict(sound_details('b.ogg'), response[1])
