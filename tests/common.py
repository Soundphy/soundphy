import json
from itertools import chain
from itertools import combinations
from http import HTTPStatus

import pytest


HTTP_STATUS = dict((int(s), s.name) for s in HTTPStatus)


sounds = {
    'a.ogg': {
        'description': {
            'title': '440 Hz sound',
            'description': 'An A note playing at 440 Hz.',
        },
        'properties': {
            'size': 5171,
            'duration': 0.0,
            'codec': 'ogg',
            'sha1': '2f16bca1d0482e1d38962a690bb27757f7651387',
        }
    },
    'b.ogg': {
        'description': {
            'title': '493.88 Hz sound',
            'description': 'A B note playing at 493.88 Hz.',
        },
        'properties': {
            'size': 4437,
            'duration': 0.0,
            'codec': 'ogg',
            'sha1': '586e25c129b20bb20adb6e359c4350cb050551f5',
        }
    },
}


def sound_upload(sound):
    """
    Create a dictionary with the necessary fields to upload a sound.
    """
    upload = {'sound': open('tests/audio/%s' % sound, 'rb')}
    upload.update(sounds[sound]['description'])
    return upload


def sound_details(sound):
    """
    Create a dictionary with all the sound details.
    """
    details = {}
    details.update(sounds[sound]['description'])
    details.update(sounds[sound]['properties'])
    return details


def decode(response):
    """
    Decode an HTTP response with JSON content.
    """
    return json.loads(response.content.decode('utf'))


def status(response):
    """
    Convert an HTTP response's status code to a readable string.
    """
    return HTTP_STATUS[response.status_code].lower()


def is_subdict(small, big):
    """
    Check if a dictionary is "contained" in another dictionary.
    """
    return small.items() <= big.items()


def incomplete_dict(dictionary):
    """
    Given a dictionary, return all its possible incomplete dictionaries.

    In example, if the input dictionary has keys {1, 2, 3}, seven
    dictionaries will be created: {}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}.
    """
    items = dictionary.items()
    powerset = chain.from_iterable(combinations(items, size)
                                   for size in range(len(items)))
    return (dict(s) for s in powerset)


@pytest.fixture(scope='function')
def logged_in_client(request, client, django_user_model):
    """
    Logged-in client fixture.

    A standard client that logs-in with credentials that are previously
    added to the Django user model objects.
    """
    user = dict(username='johndoe', email='jd@example.com', password='123456')
    django_user_model.objects.create_user(**user)
    client.login(**user)
    return client
