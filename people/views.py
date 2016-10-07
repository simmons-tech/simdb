from django.shortcuts import render


def directory(request):
    results = []
    if request.method == 'POST':
        results = ['amol']
    return render(request, 'people/directory.html', {'results': results})


def entry(request, username):
    return render(request, 'people/entry.html')
