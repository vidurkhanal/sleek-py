import unittest
from sleek_py import Sleek


class TestSleek(unittest.TestCase):
    def test_if_server_instance_is_created(self):
        sleek = Sleek()
        assert sleek.socket_name is not None

if __name__ == "__main__":
    unittest.main()
