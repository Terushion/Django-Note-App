# my_notes/tests.py

from django.test import TestCase
from django.urls import reverse
from .models import PostItNote


# Create your tests here.


class PostModelTest(TestCase):

    def setUp(self):
        # Create a PostItNote object for testing
        self.note = PostItNote.objects.create(
            title="Test Post",
            content="This is a test post.",
            author="Test Author",
        )

    def test_post_has_title(self):
        # Test that a PostItNote object has the expected title
        note = PostItNote.objects.get(id=self.note.id)
        self.assertEqual(note.title, "Test Post")

    def test_post_has_content(self):
        # Test that a PostItNote object has the expected content
        note = PostItNote.objects.get(id=self.note.id)
        self.assertEqual(note.content, "This is a test post.")


class PostViewTest(TestCase):

    def setUp(self):
        # Create a PostItNote object for testing views
        self.note = PostItNote.objects.create(
            title="Test Post",
            content="This is a test post.",
            author="Test Author",
        )

    def test_post_list_view(self):
        # Test the view_notes view
        response = self.client.get(reverse("view"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")

    def test_post_detail_view(self):
        # Test the check_note view
        response = self.client.get(reverse("check", args=[self.note.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")
        self.assertContains(response, "This is a test post.")
