import pytest
from item.models import Category, Item



@pytest.fixture
@pytest.mark.django_db
def connect_category():
	Category.objects.create(
		name="shoes"
	)
	Category.objects.create(
		name="clothes"
	)
	Category.objects.create(
		name="cars"
	)


@pytest.fixture
@pytest.mark.django_db
def connect_item(connect_category):
	Item.objects.create(
		category="shoes",
		name="Ecco",
		description="Some shoes ECCO",
		price=4500,
		is_sold=False
	)
