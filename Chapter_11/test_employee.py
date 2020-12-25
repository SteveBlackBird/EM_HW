import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    """Тесты для класса Employee."""

    def setUp(self):
        """Создание экземпляра класса работника."""
        self.worker = Employee('Sergey', 'Ivanov', 1000000)

    def test_give_default_raise(self):
        """Стандартное повышение ЗП."""
        self.worker.salary += 5000
        self.assertEqual(self.worker.salary, 1005000)

    def test_give_custom_raise(self):
        """Нестандартное повышение ЗП."""
        custom_salary_raise = 33000
        self.worker.salary += custom_salary_raise
        self.assertEqual(self.worker.salary, self.worker.salary)

if __name__ == '__main__':
    unittest.main()