import datetime

from utilities.testing import ViewTestCases

from netbox_inventory.models import Purchase, Supplier
from netbox_inventory.tests.custom import ModelViewTestCase


class PurchaseTestCase(
    ModelViewTestCase,
    ViewTestCases.PrimaryObjectViewTestCase,
):
    model = Purchase

    @classmethod
    def setUpTestData(cls):
        supplier1 = Supplier.objects.create(
            name='Supplier 1',
            slug='supplier1',
        )
        supplier2 = Supplier.objects.create(
            name='Supplier 2',
            slug='supplier2',
        )
        purchase1 = Purchase.objects.create(
            name='Purchase 1',
            supplier=supplier1,
            status='closed',
        )
        purchase2 = Purchase.objects.create(
            name='Purchase 2',
            supplier=supplier1,
            status='closed',
        )
        purchase3 = Purchase.objects.create(
            name='Purchase 3',
            supplier=supplier1,
            status='closed',
        )
        cls.form_data = {
            'name': 'Purchase',
            'supplier': supplier1.pk,
            'description': 'Purchase description',
            'status': 'open',
            'date': datetime.date(day=1, month=1, year=2023),
        }
        cls.csv_data = (
            'name,supplier,date,status',
            f'Purchase 4,{supplier1.name},2023-03-26,open',
            f'Purchase 5,{supplier1.name},2023-03-26,open',
            f'Purchase 6,{supplier1.name},2023-03-26,open',
        )
        cls.csv_update_data = (
            'id,description,supplier,status',
            f'{purchase1.pk},description 1,{supplier2.name},closed',
            f'{purchase2.pk},description 2,{supplier2.name},closed',
            f'{purchase3.pk},description 3,{supplier2.name},closed',
        )
        cls.bulk_edit_data = {
            'description': 'bulk description',
            'date': datetime.date(day=1, month=1, year=2022),
            'status': 'partial',
        }
