class ObjectPool:
    def __init__(self, size, cls):
        self._object_pool = [cls() for _ in size]

    def acquire(self):
        return self._object_pool.pop()

    def release(self, cls):
        return self._object_pool.append(cls)