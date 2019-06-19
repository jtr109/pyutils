import datetime
from unittest import TestCase

from pyutils.text import camel_to_snake


class CaseConverterTestCase(TestCase):

    def test_camel_case_to_lower_case(self):
        self.assertEqual(camel_to_snake('snakesOnAPlane'), 'snakes_on_a_plane')
        self.assertEqual(camel_to_snake('SnakesOnAPlane'), 'snakes_on_a_plane')
        self.assertEqual(camel_to_snake('snakes_on_a_plane'), 'snakes_on_a_plane')
        self.assertEqual(camel_to_snake('IPhoneHysteria'), 'i_phone_hysteria')
        self.assertEqual(camel_to_snake('iPhoneHysteria'), 'i_phone_hysteria')
