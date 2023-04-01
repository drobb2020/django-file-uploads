from django.shortcuts import get_object_or_404, redirect, render

from core.forms import DogForm
from core.models import Dog


def index(request):
    if request.method == "POST":
        form = DogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            context = {"form": form}
            return render(request, "core/index.html", context)

    context = {"form": DogForm()}
    return render(request, "core/index.html", context)


def list_dogs(request):
    dogs = Dog.objects.all()
    context = {"dogs": dogs}
    return render(request, "core/list_dogs.html", context)


def delete_image(request, pk):
    dog = get_object_or_404(Dog, pk=pk)
    dog.delete()
    return redirect('list-dogs')
