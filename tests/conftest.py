"""This module contains the fixtures and hooks for the calculator test suite."""
# conftest.py
from decimal import Decimal
import pytest
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker()
# pylint disable=comaparison-with-callable
def generate_test_data(num_records):
    '''Generate test data for Calculator and Calculation tests.'''
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2))\
              if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]

        if operation_func is divide:
            b = Decimal('1') if b == Decimal('0') else b

        try:
            expected = operation_func(a, b)\
                  if operation_func is not divide or b != Decimal('0')\
                      else "ZeroDivisionError"
        except ZeroDivisionError:
            expected = "ZeroDivisionError"
        yield a, b, operation_name, operation_func, expected\
                # Yield results instead of calling itself

def pytest_addoption(parser):
    '''Add custom command line options for the test suite.'''
    parser.addoption("--num_records", action="store",\
                      default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    '''Generate test data for Calculator and Calculation tests.'''
    # Check if the test is expecting any of the dynamically generated fixtures
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        # Adjust the parameterization to include both operation_name\
        #  and operation for broad compatibility
        # Ensure 'operation_name' is used for identifying\
        #  the operation in Calculator class tests
        # 'operation' (function reference) is used for Calculation class tests.
        parameters = list(generate_test_data(num_records))
        # Modify parameters to fit test functions' expectations
        modified_parameters = [(a, b, op_name\
                                 if 'operation_name' in metafunc.fixturenames\
                                      else op_func, expected)\
                                      for a, b, op_name, op_func, expected in parameters]
        metafunc.parametrize("a,b,operation,expected", modified_parameters)

@pytest.mark.parametrize("num_records", [0, 1, 5])
def test_generate_test_data_various_counts(num_records):
    """Test generate_test_data function with varying record counts."""
    data = list(generate_test_data(num_records))
    assert len(data) == num_records, f"Expected {num_records} records, got {len(data)}."
