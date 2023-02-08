import pytest
from item.models import Category, Item


@pytest.mark.django_db
def test_category_db_1(connect_category):
	category = Category.objects.get(id=1)
	assert "shoes" == category.name


@pytest.mark.django_db
def test_category_db_2(connect_category):
	category = Category.objects.get(id=2)
	assert "clothes" == category.name


@pytest.mark.django_db
def test_category_db_3(connect_category):
	category = Category.objects.get(id=3)
	assert "cars" == category.name


@pytest.mark.django_db
def test_category_db_count(connect_category):
	category = Category.objects.all()
	assert 3 == category.count()

