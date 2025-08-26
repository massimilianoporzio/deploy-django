"""Views for the home app."""

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render


def hello_world(request):
    """Render the hello world template."""
    return render(request, "hello-world.html", {})


def healthz_view(request):
    """Health check view that returns OK status.

    Args:
        request: HTTP request object.

    Returns:
        HttpResponse with "OK" status.
    """
    return HttpResponse("OK")


def test_ai_function(user_id: int, posts_data: list[dict]) -> dict:
    """Build a summary message and list of active post titles for a user.

    Args:
        user_id: Primary key of the target user.
        posts_data: Iterable of post dicts with keys 'title' and 'active'.

    Returns:
        A dict with 'message' and 'posts' keys.
    """
    user = get_object_or_404(User, id=user_id)
    result_posts = [post["title"] for post in posts_data if post.get("active")]
    message = f"User {user.username} has {len(result_posts)} posts"
    return {"message": message, "posts": result_posts}
