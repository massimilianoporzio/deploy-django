"""Views for the home app."""

from django.http import HttpResponse
from django.shortcuts import render


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


# Test AI Review


def test_ai_function(user_id, posts_data):
    # Funzione con diversi problemi per testare l'AI Review

    from django.contrib.auth.models import User

    # Problema 1: Query N+1 potential
    user = User.objects.get(id=user_id)  # Dovrebbe essere get_object_or_404

    # Problema 2: Lista invece di comprehension
    result_posts = []
    for post in posts_data:
        if post["active"] == True:  # Dovrebbe essere 'is True'
            result_posts.append(post["title"])

    # Problema 3: String concatenation invece di f-string
    message = "User " + user.username + " has " + str(len(result_posts)) + " posts"

    # Problema 4: Doppia negazione
    if not user.is_active != True:
        pass

    # Problema 5: Unused import e variable
    unused_var = "test"

    return {"message": message, "posts": result_posts}
