from common import status
from common import logged_in_client  # pragma: no flakes


def test_an_admin_view_anonymous(client):
    """
    An anonymous client should not be able to access the admin interface.
    The server responds with a redirection to the login page.
    """
    response = client.get('/admin/')
    assert status(response) == 'found'
    assert response.url.startswith('/admin/login/')


def test_an_admin_view_logged_in(logged_in_client):
    """
    A logged-in client should not be able to access the admin interface.
    The server responds with a redirection to the login page.
    """
    response = logged_in_client.get('/admin/')
    assert status(response) == 'found'
    assert response.url.startswith('/admin/login/')


def test_an_admin_view(admin_client):
    """
    An admin client should be able to access the admin interface, just as
    expected.
    """
    response = admin_client.get('/admin/')
    assert status(response) == 'ok'
