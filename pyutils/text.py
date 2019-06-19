import re

_underscorer1 = re.compile(r'(.)([A-Z][a-z]+)')
_underscorer2 = re.compile('([a-z0-9])([A-Z])')


def camel2snake(camel: str) -> str:
    subbed = _underscorer1.sub(r'\1_\2', camel)
    return _underscorer2.sub(r'\1_\2', subbed).lower()


def snake_to_camel(snake: str) -> str:
    return re.sub(r'(?:^|_)([a-z])', lambda x: x.group(1).upper(), snake)
