import psutil
from repository.ram_repository import RAMRepository

class RAMService:
    def __init__(self):
        self.repository = RAMRepository()

    def collect_ram_stats(self):
        mem = psutil.virtual_memory()
        total_mb = mem.total / (1024 * 1024)
        used_mb = mem.used / (1024 * 1024)
        free_mb = mem.available / (1024 * 1024)

        self.repository.insert_ram_stats(total_mb, used_mb, free_mb)

    def get_last_n_ram_stats(self, n: int):
        return self.repository.get_last_n_stats(n)
