"""A small module providing TimeDeque, a time-expiring deque."""

from time import monotonic
from collections import deque

class TimeDeque:
    """A deque-like container that removes items older than a time window."""

    def __init__(self, seconds):
        self.seconds = seconds
        self.items = deque()

    def append(self, item) -> None:
        now = monotonic()
        self.items.append((now, item))
        self._expire(now)

    def _expire(self, now=None):
        now = monotonic() if now is None else now
        cutoff = now - self.seconds
        while self.items and self.items[0][0] < cutoff:
            self.items.popleft()

    def __iter__(self):
        self._expire()
        return (item for _, item in self.items)

    def __getitem__(self, index):
        self._expire()
        return self.items[index][1]

    def __len__(self) -> int:
        self._expire()
        return len(self.items)

    def __bool__(self) -> bool:
        self._expire()
        return bool(self.items)

    def clear(self) -> None:
        self.items.clear()

    def to_list(self) -> list:
        self._expire()
        return [item for _, item in self.items]