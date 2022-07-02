from django.test import TestCase
import timesheet.views


# Create your tests here.
class Test_timesheet(TestCase):
    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)