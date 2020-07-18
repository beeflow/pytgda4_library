from django.test import TestCase
from faker import Faker

from user.models import User


class UserTest(TestCase):
    def setUp(self) -> None:
        self.faker = Faker()

    def tearDown(self) -> None:
        del self.faker

    def test_create_with_card(self):
        expected = "1".zfill(9)
        user = User.objects.create(
            username=self.faker.simple_profile()["username"],
            card_number=self.faker.word
        )

        self.assertEqual(expected, user.card_number)

    def test_create_without_card(self):
        expected = "1".zfill(9)
        user = User.objects.create(
            username=self.faker.simple_profile()["username"]
        )

        self.assertEqual(expected, user.card_number)

    def test_create_without_card_a(self):
        expected = "1".zfill(9)
        user = User(
            username=self.faker.simple_profile()["username"]
        )
        user.save()

        self.assertEqual(expected, user.card_number)
