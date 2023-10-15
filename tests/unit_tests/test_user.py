import pytest


class TestClassUsers:
    pytestmark = pytest.mark.django_db

    def test_register_user(self, client):
        pyload = dict(
            username="adm2",
            email="t2@t.com",
            password="Wf!34fgf)WWs"
        )
        response = client.post("/auth/register/", pyload)
        data = response.data

        assert data["username"] == pyload["username"]
        assert data["email"] == pyload["email"]
        assert "password" not in data

    def test_login_user(self, client, user):
        pyload = dict(
            email="t1@t.com",
            password="TestUserPassword"
        )
        response = client.post("/auth/login/", pyload)
        data = response.data

        assert response.status_code == 200
        assert data["email"] == pyload["email"]

    def test_login_user_fail(self, client):
        pyload = dict(
            email="t2@t.com",
            password="Wf!34fgf)WWs"
        )
        response = client.post("/auth/login/", pyload)

        assert response.status_code == 400

    def test_user_info(self, api_client_with_credentials, user):
        response = api_client_with_credentials.get("/auth/")
        data = response.data

        assert response.status_code == 200
        assert data["email"] == user.email
        assert data["username"] == user.username

    def test_user_profile(self, api_client_with_credentials, user_profile):
        response = api_client_with_credentials.get("/auth/profile/")
        data = response.data

        assert response.status_code == 200
        assert data["description"] == user_profile.profile.description

    def test_user_profile_avatar(self, api_client_with_credentials, user_profile):
        response = api_client_with_credentials.get("/auth/profile/avatar/")
        data = response.data

        assert response.status_code == 200
        assert data["avatar"] == f"/media{user_profile.profile.avatar}"

    def test_user_token_refresh(self, api_client_with_credentials, refresh_token):
        pyload = dict(
            refresh=refresh_token
        )
        response = api_client_with_credentials.post("/auth/token/refresh/", pyload)
        data = response.data

        assert response.status_code == 200
        assert data['refresh'] != refresh_token

    def test_user_logout(self, api_client_with_credentials, refresh_token):
        pyload = dict(
            refresh=refresh_token
        )
        response = api_client_with_credentials.post("/auth/logout/", pyload)

        assert response.status_code == 205
