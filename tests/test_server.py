import unittest
import sleek_py


class ServerTests(unittest.TestCase):
    def test_server_socket_being_set(self):
        sleek = sleek_py.Sleek()
        assert sleek.socket_name is not None


if __name__ == "__main__":
    unittest.main()
