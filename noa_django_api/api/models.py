from django.db import models

# ORM (Object-Relational Mapping) is a programming technique used to convert data between incompatible type systems in object-oriented programming languages.
# It allows developers to interact with the database using Python objects instead of writing raw SQL queries.

class BlogPost(models.Model):
    title = models.CharField(max_length=200)  # Title of the blog post
    content = models.TextField()  # Content of the blog post
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the post was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the post was last updated

    def __str__(self):
        return self.title  # String representation of the model, returns the title of the blog post