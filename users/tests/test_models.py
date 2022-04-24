from django.test import TestCase

from users.models import Contact


class TestContactModel(TestCase):
    
    def test_should_create_contact(self):
        name=""
        email=""
        subject=""
        message=""
        contact=Contact(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        contact.save()
        self.assertEqual(contact.name,name)