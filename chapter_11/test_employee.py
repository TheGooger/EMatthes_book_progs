import unittest
from employee import Employee


class EmployeeTestCase(unittest.TestCase):
    """Tests for 'Employee' class."""

    def setUp(self):
        """Creates an employee."""
        self.new_employee = Employee('Vladimir', 'Ivanov', 200)

    def test_give_default_raise(self):
        """Checks if default raise works."""
        self.new_employee.give_raise()
        self.assertEqual(self.new_employee.salary, 5200)

    def test_give_custom_raise(self):
        """Checks if custom raise works correctly,"""
        self.new_employee.give_raise(3000)
        self.assertEqual(self.new_employee.salary, 3200)
