from library.models import Genre


def genres_menu(request):
    return {'genres': Genre.objects.all()}
