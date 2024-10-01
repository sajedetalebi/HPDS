import unittest
from services.ram_service import RAMService
from repository.ram_repository import RAMRepository

class TestRAMService(unittest.TestCase):
    def setUp(self):
        self.service = RAMService()
        self.repository = RAMRepository()

    def test_collect_ram_stats(self):
        try:
            self.service.collect_ram_stats()
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Failed to collect RAM stats: {e}")

    def test_get_last_n_ram_stats(self):
        try:
            result = self.service.get_last_n_ram_stats(1)
            self.assertIsInstance(result, list)
        except Exception as e:
            self.fail(f"Failed to retrieve RAM stats: {e}")

if __name__ == '__main__':
    unittest.main()
