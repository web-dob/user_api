import pytest
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import CustomUser


@pytest.fixture
@pytest.mark.django_db
def user():
    return CustomUser.objects.create_user(
        username="test_user",
        email="t1@t.com",
        password="TestUserPassword"
    )


@pytest.fixture
@pytest.mark.django_db
def user_profile(user):
    user.profile.description = "test_description"
    user.profile.avatar = "/upload/test_image.png"
    user.save
    return user


@pytest.fixture
def refresh_token(user):
    return str(RefreshToken.for_user(user))


@pytest.fixture
@pytest.mark.django_db
def auth_client(client, user):
    """
    pyload = dict(
        email = user.email,
        password = "TestUserPassword"
    )
    client.login(**pyload)
    """
    """ OR Method django-pytest """
    client.force_login(user)
    return client


@pytest.fixture
@pytest.mark.django_db
def api_client_with_credentials(user, client):
    client.force_authenticate(user=user)
    yield client
    client.force_authenticate(user=None)
