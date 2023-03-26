from django.contrib.auth.models import User
import pytest


@pytest.mark.django_db
@pytest.mark.xfail
def test_my_user():
	me = User.objects.get(username="AdmiralGeneral")
	assert me.is_superuser
