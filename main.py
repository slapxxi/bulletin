def show(request, id):
    instance = get_object_or_404(User, pk=id)
    return redirect(instance)


class Person:
    def __init__(self):
        self._name = 'private'

    def get(self, request, id):
        return redirect(instance)

    def post(self, request):
        return render(request, 'index.html', self.context)
