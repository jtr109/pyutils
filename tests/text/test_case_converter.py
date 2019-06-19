import datetime
from unittest import TestCase

from pyutils.text import camel2snake, snake_to_camel


class CaseConverterTestCase(TestCase):

    def test_camel2snake(self):
        pairs = (
            ('snakesOnAPlane', 'snakes_on_a_plane'),
            ('SnakesOnAPlane', 'snakes_on_a_plane'),
            ('snakes_on_a_plane', 'snakes_on_a_plane'),
            ('IPhoneHysteria', 'i_phone_hysteria'),
            ('iPhoneHysteria', 'i_phone_hysteria'),
        )

        for c, s in pairs:
            self.assertEqual(camel2snake(c), s)

    def test_snake2camel(self):
        pairs = (
            ('snakes_on_a_plane', 'SnakesOnAPlane'),
            ('SnakesOnAPlane', 'SnakesOnAPlane'),
            ('i_phone_hysteria', 'IPhoneHysteria'),
        )

        for s, c in pairs:
            self.assertEqual(snake_to_camel(s), c)
