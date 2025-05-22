import random
from django.core.management.base import BaseCommand
from faker import Faker

from django.contrib.auth import get_user_model
from apps.expenses.models import ExpenseCategory, Expense
from apps.inventory.models import Category, Warehouse, Product, StockMovement
from apps.purchasing.models import Supplier, PurchaseOrder, PurchaseOrderLine
from apps.sales.models import Customer, SaleOrder, SaleOrderLine

User = get_user_model()


class Command(BaseCommand):
    help = "Seed the database with realistic Uzbek hacker–style data"

    def handle(self, *args, **options):
        faker = Faker('uz_UZ')

        # 1. Expense Categories
        expense_cat_names = [
            "Uy-joy xarajatlari",
            "Ta'lim",
            "Sog'liq",
            "Transport",
            "Oziq-ovqat",
        ]
        expense_categories = []
        for name in expense_cat_names:
            cat, _ = ExpenseCategory.objects.get_or_create(name=name)
            expense_categories.append(cat)

        # 2. Inventory Categories
        inv_cat_names = [
            "Elektronika",
            "Oziq-ovqat",
            "Maishiy texnika",
            "Kiyim-kechak",
            "Sport anjomlari",
        ]
        inventory_categories = []
        for name in inv_cat_names:
            cat, _ = Category.objects.get_or_create(name=name)
            inventory_categories.append(cat)

        # 3. Warehouses
        warehouses = []
        for _ in range(5):
            wh, _ = Warehouse.objects.get_or_create(
                name=f"{faker.city()} Omborxona",
                defaults={'address': faker.address()}
            )
            warehouses.append(wh)

        # 4. Products
        products = []
        for _ in range(100):
            prod = Product.objects.create(
                sku=faker.unique.lexify(text='???-#####'),
                name=f"{faker.word().capitalize()} {faker.word().capitalize()}",
                category=random.choice(inventory_categories),
                cost_price=round(random.uniform(1000, 100000), 2),
                sell_price=round(random.uniform(1000, 150000), 2),
                size=random.choice(['S', 'M', 'L', 'XL', '']),
                color=faker.color_name()
            )
            products.append(prod)

        # 5. Stock Movements
        users = list(User.objects.all())
        for _ in range(200):
            StockMovement.objects.create(
                product=random.choice(products),
                warehouse=random.choice(warehouses),
                user=random.choice(users) if users else None,
                movement_type=random.choice([StockMovement.Type.IN, StockMovement.Type.OUT]),
                quantity=random.randint(1, 100)
            )

        # 6. Suppliers & Purchase Orders
        suppliers = []
        for _ in range(20):
            sup = Supplier.objects.create(
                name=faker.company(),
                phone=faker.phone_number(),
                address=faker.address()
            )
            suppliers.append(sup)

        for _ in range(50):
            po = PurchaseOrder.objects.create(
                supplier=random.choice(suppliers),
                warehouse=random.choice(warehouses),
                note=faker.sentence()
            )
            for _ in range(random.randint(1, 5)):
                PurchaseOrderLine.objects.create(
                    order=po,
                    product=random.choice(products),
                    quantity=random.randint(1, 20),
                    cost=round(random.uniform(1000, 100000), 2)
                )

        # 7. Customers & Sale Orders
        customers = []
        for _ in range(100):
            cust = Customer.objects.create(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                phone=faker.phone_number(),
                address=faker.address()
            )
            customers.append(cust)

        for _ in range(200):
            so = SaleOrder.objects.create(
                customer=random.choice(customers),
                cashier=random.choice(users) if users else None,
                note=faker.sentence()
            )
            for _ in range(random.randint(1, 5)):
                SaleOrderLine.objects.create(
                    order=so,
                    product=random.choice(products),
                    quantity=random.randint(1, 10),
                    price=round(random.uniform(1000, 150000), 2)
                )

        # 8. Expenses
        for _ in range(500):
            Expense.objects.create(
                category=random.choice(expense_categories),
                amount=round(random.uniform(1000, 500000), 2),
                note=faker.sentence(),
                user=random.choice(users) if users else None
            )

        self.stdout.write(self.style.SUCCESS('Database seeded with Uzbek hacker–style data.'))
