from django.urls import reverse


class Test_Index:
    def test_unauthenticated(self, client):
        response = client.get(reverse("core:index"))
        assert response.status_code == 200
