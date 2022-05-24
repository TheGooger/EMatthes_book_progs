class Employee():
    """Creates an employee."""

    def __init__(self, first_n, last_n, salary):
        """Initialization of an employee."""
        self.first_name = first_n
        self.last_name = last_n
        self.salary = salary

    def give_raise(self, increase=5000):
        """Automatically increases salary by $5000."""
        self.salary += increase
