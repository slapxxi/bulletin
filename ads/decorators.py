from django.shortcuts import redirect, get_object_or_404
from utils.decorators import decorator

from .models import Ad


@decorator
def author_required(view, request, id, *args, **kwargs):
    """
    A view decorator that requires user to be an author of the model.
    Otherwise it redirects to the model's page.
    """
    ad = get_object_or_404(Ad, pk=id)
    if ad.is_author(request.user):
        return view(request, ad, *args, **kwargs)
    return redirect(ad)
