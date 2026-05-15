# TimeDeque

`TimeDeque` is a small Python utility for keeping only the most recent items in a deque.

Each item is stored with the time it was added. When items become older than the configured time window, they are automatically removed.

## Installation

```bash
pip install timedeque
```

## Basic Usage

```python
from timedeque import TimeDeque
from time import sleep

dq = TimeDeque(seconds=2)

dq.append("first")
dq.append("second")

print(list(dq))
# ['first', 'second']

sleep(3)

print(list(dq))
# []
```

## Why use this?

Python's built-in `collections.deque` is useful for storing ordered data, but it does not remove items based on age.

`TimeDeque` is useful when you only care about recent events, such as:

- recent trades
- recent errors
- rate-limit windows
- rolling event buffers
- short-term signals

## API

### `TimeDeque(seconds)`

Creates a new deque that keeps items for the given number of seconds.

```python
dq = TimeDeque(seconds=60)
```

### `append(item)`

Adds an item to the deque with the current time.

```python
dq.append("event")
```

### `len(dq)`

Returns the number of non-expired items.

```python
len(dq)
```

### `bool(dq)`

Returns `True` if the deque has any non-expired items.

```python
if dq:
    print("There are recent items")
```

### Iteration

You can iterate over the current non-expired items.

```python
for item in dq:
    print(item)
```

### Indexing

You can access an item by index.

```python
first_item = dq[0]
```

### `to_list()`

Returns the current non-expired items as a regular list.

```python
items = dq.to_list()
```

### `clear()`

Removes all items.

```python
dq.clear()
```

## Example

```python
from timedeque import TimeDeque
from time import sleep

errors = TimeDeque(seconds=300)

errors.append("connection failed")
errors.append("timeout")

if len(errors) >= 2:
    print("Multiple recent errors")
```

## Requirements

Python 3.10 or newer.

## License

MIT License.