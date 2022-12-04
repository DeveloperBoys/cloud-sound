from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed

from .. import serializers


def google_login(request):
    return render(request, 'oauth/google_login.html')


@api_view(['POST'])
def google_auth(request):
    google_data = serializers.GoogleAuth(data=request.data)
    if google_data.is_valid():
        pass
    else:
        return AuthenticationFailed(code=403, detail='Bad data Google')
