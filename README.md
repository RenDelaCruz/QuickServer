# QuickServer

Create a quick HTTP server using Python.

## Setup

Clone this repository and move `server.py` into any directory. Then simply run:

```shell
$ python -m server
```

You can also specify the port:

```shell
$ python -m server 8000
```

## Shutdown

Press `Ctrl+C` to shutdown the server.

## Use in a script

```python
from server import QuickServer

try:
    server = QuickServer(port=8000)
    server.run()
except KeyboardInterrupt:
    server.stop()
```