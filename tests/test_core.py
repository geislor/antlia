from django.test import TestCase


class CoreTestCase(TestCase):
    def test_core(self):
        self.assertTrue(True)

    def test_core_false(self):
        self.assertTrue(False)
