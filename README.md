# PyUtils

## Installation

[Pipenv](https://docs.pipenv.org/en/latest/) is recommended for creating python virtual environments.

Just use the command below to install it in you project.

```shell
pipenv install -e git+https://github.com/jtr109/pyutils.git@develop#egg=pyutils
```

## Quick Start

```python
import datetime
from pyutils.datetime import timestamp

timestamp(datetime.datetime.now())
```
