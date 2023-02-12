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
def connect_item():
	category_1 = Category.objects.create(name="shoes")
	category_2 = Category.objects.create(name="clothes")
	category_3 = Category.objects.create(name="cars")
	Item.objects.create(
		category=category_1.name,
		name="Ecco",
		description="Some shoes ECCO",
		price=4500,
		is_sold=False
	)
	Item.objects.create(
		category=category_2,
		name="Ecco 2",
		description="Some clothes ECCO",
		price=5500,
		is_sold=False
	)
	Item.objects.create(
		category=category_3,
		name="Audi",
		description="Some car Audi",
		price=550000,
		is_sold=False
	)
	Item.objects.create(
		category=category_3,
		name="Mercedes",
		description="Some car Mercedes",
		price=650000,
		is_sold=False
	)
	Item.objects.create(
		category=category_3,
		name="Audi 2",
		description="Some car Audi 2",
		price=650000,
		is_sold=False
	)


