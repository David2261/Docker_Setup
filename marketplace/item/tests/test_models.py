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


@pytest.mark.django_db
def test_item_name_1(connect_item):
	item = Item.objects.get(id=1)
	assert "Ecco" == item.name


@pytest.mark.django_db
def test_item_name_2(connect_item):
	item = Item.objects.get(id=2)
	assert "Ecco 2" == item.name


@pytest.mark.django_db
def test_item_name_3(connect_item):
	item = Item.objects.get(id=3)
	assert "Audi" == item.name


@pytest.mark.django_db
def test_item_name_4(connect_item):
	item = Item.objects.get(id=4)
	assert "Mercedes" == item.name


@pytest.mark.django_db
def test_item_name_5(connect_item):
	item = Item.objects.get(id=5)
	assert "Audi 2" == item.name


@pytest.mark.django_db
def test_item_db_count(connect_item):
	item = Item.objects.all()
	assert 5 == item.count()


