class AuthorRequiredMixin:
  def dispatch(self, request, pk, *args, **kwargs):
    instance = get_object_or_404(self.model, pk=pk)
    if not instance.is_author(request.user):
      return redirect(instance)
    return super().dispatch(request, instance, *args, **kwargs)
