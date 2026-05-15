from timedeque import TimeDeque
import time

def test_append_and_to_list():
    dq = TimeDeque(seconds=10)

    dq.append("a")
    dq.append("b")

    assert dq.to_list() == ["a", "b"]

def test_len_counts_current_items():
    dq = TimeDeque(seconds=10)

    dq.append("a")
    dq.append("b")

    assert len(dq) == 2

def test_bool_is_false_when_empty():
    dq = TimeDeque(seconds=10)

    assert not dq

def test_bool_is_true_when_items_exist():
    dq = TimeDeque(seconds=10)

    dq.append("a")

    assert dq

def test_clear_removes_all_items():
    dq = TimeDeque(seconds=10)

    dq.append("a")
    dq.append("b")
    dq.clear()

    assert len(dq) == 0
    assert dq.to_list() == []

def test_iteration_returns_items_without_timestamps():
    dq = TimeDeque(seconds=10)

    dq.append("a")
    dq.append("b")

    assert list(dq) == ["a", "b"]

def test_indexing_returns_item_without_timestamp():
    dq = TimeDeque(seconds=10)

    dq.append("a")
    dq.append("b")

    assert dq[0] == "a"
    assert dq[1] == "b"

def test_expire_removes_old_items():
    dq = TimeDeque(seconds=10)

    dq.items.append((time.monotonic() - 12, "old"))
    dq.items.append((time.monotonic() - 8, "new"))

    assert dq.to_list() == ["new"]

def test_expire_keeps_items_at_cutoff():
    dq = TimeDeque(seconds=10)

    dq.items.append((time.monotonic() - 9, "kept"))

    assert dq.to_list() == ["kept"]

def test_expire_removes_multiple_old_items():
    dq = TimeDeque(seconds=10)

    dq.items.append((time.monotonic() - 20, "old 1"))
    dq.items.append((time.monotonic() - 15, "old 2"))
    dq.items.append((time.monotonic() - 5, "new"))

    assert dq.to_list() == ["new"]