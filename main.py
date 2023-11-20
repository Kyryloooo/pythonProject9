import time
import unittest


def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")
        return result

    return wrapper


# Пример функции, которую мы будем тестировать
@time_it
def example_function():
    time.sleep(2)
    return "Function executed successfully"


# Тесты
class TestTimeIt(unittest.TestCase):
    def test_execution_time(self):
        with self.assertLogs() as logs:
            result = example_function()

        self.assertIn("Execution time:", logs.output[0])
        self.assertEqual(result, "Function executed successfully")


if __name__ == '__main__':
    unittest.main()
