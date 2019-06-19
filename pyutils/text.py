import re

_underscorer1 = re.compile(r'(.)([A-Z][a-z]+)')
_underscorer2 = re.compile('([a-z0-9])([A-Z])')


def camel_to_snake(camel: str) -> str:
    subbed = _underscorer1.sub(r'\1_\2', camel)
    return _underscorer2.sub(r'\1_\2', subbed).lower()
