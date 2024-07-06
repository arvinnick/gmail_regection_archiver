from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


# Create your views here.
def archiver(request):
    if (request.get("message").find("Unfortunately") != -1 and
            request.get("subject").find("Your application at") != -1 and
            request.get("from").find("linkedin")):  #change the values based on Gmail API
        return Response("archive", status=HTTP_200_OK)
    else:
        return Response("nothing", status=HTTP_200_OK)
