from django.test import TestCase

from apps.expenses.models import ExpenseCategory


class TestExpenseCategory(TestCase):
    def setUp(self):
        self.expense = ExpenseCategory(
            name='<NAME>',
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.expense, ExpenseCategory))