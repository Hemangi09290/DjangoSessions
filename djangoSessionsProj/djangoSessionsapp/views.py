from django.shortcuts import render
from .models import Author
# Create your views here.
def index(request):
    num_authors = Author.objects.count()  # The 'all()' is implied by default.
    num_books = num_authors
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable.
    return render(request, 'index.html', context=context)