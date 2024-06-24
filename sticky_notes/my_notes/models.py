from django.db import models


class PostItNote(models.Model):
    """
    Model representing a sticky note (a.k.a post-it note).
    Fields:
    - title: CharField for the note title with a maximum length of 200 characters.
    - content: TextField for the note content.
    - created_at: DateTimeField set to the current date and time when the note is created.
    - author: CharField for the author's name with a maximum length of 30 characters.
    """

    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=30)

    def __str__(self):
        """
        Returns a string representation of the PostItNote, which is its title.
        """
        return self.title


# The User model is currently commented out.
# Uncomment and modify this model if you need a custom user model in the future.

# class User(models.Model):
#     """
#     Model representing a user with the following fields:
#     - name: CharField for the user's name.
#     - email: EmailField for the user's unique email address.
#     - password: CharField for the user's password.
#     - mobile_number: CharField for the user's mobile number.
#     - date_of_birth: DateField for the user's date of birth.
#     """
#     name = models.CharField(max_length=30)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)
#     mobile_number = models.CharField(max_length=15)
#     date_of_birth = models.DateField()

#     def __str__(self):
#         """
#         Returns a string representation of the User, which is their name.
#         """
#         return self.name
