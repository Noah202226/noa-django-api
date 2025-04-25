
from rest_framework import generics, status
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class BlogPostListCreate(generics.ListCreateAPIView):
    """
    API view to retrieve and create blog posts.
    """
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def delete(self, request, *args, **kwargs):
        """
        Handle DELETE requests to delete all blog posts.
        """
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BlogPostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete a blog post.
    """
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'pk'  # Use 'id' as the lookup field instead of the default 'pk'


class BlogPostList(APIView):
    """
    API view to retrieve all blog posts.
    """
    def get(self, request, format=None):

        title = request.query_params.get('title', None)
        if title:
            blog_posts = BlogPost.objects.filter(title__icontains=title)
        else:
            blog_posts = BlogPost.objects.all()

        blog_posts = BlogPost.objects.all()
        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data)