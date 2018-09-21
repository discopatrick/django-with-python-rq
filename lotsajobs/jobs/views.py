from django.shortcuts import render

def jobs_index(request):
    html = "<html><body>Index of jobs</body></html>"
    return HttpResponse(html)
