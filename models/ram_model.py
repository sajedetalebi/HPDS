class RAMStats:
    def __init__(self, total_mb: float, used_mb: float, free_mb: float, timestamp: str):
        self.total_mb = total_mb
        self.used_mb = used_mb
        self.free_mb = free_mb
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "total_mb": self.total_mb,
            "used_mb": self.used_mb,
            "free_mb": self.free_mb,
            "timestamp": self.timestamp
        }
