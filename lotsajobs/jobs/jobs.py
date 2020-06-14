from sftp.models import Response


def check_for_response(uuid):
    Response.objects.get(uuid=uuid)
