from django.db import models

class Post(models.Model):
    """
    Model representing a blog post.

    Attributes:
        title (CharField): The title of the post.
        body (TextField): The content of the post.
        date (DateTimeField): The date and time the post was created.
        default (str): Default string value, not used as a model field.
    """
    # Django will create an auto-incrementing primary key by default
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()
    default="Code by Khensani Ntulo"

    def __str__(self):
        """
        Returns the string representation of the Post object.

        Returns:
            str: The title of the post.
        """
        return self.title

