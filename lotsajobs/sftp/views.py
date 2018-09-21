from django.http import HttpResponse
from django.shortcuts import render


def sftp_index(request):
    html = "<html><body>Index of sftp</body></html>"
    return HttpResponse(html)
