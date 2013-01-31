from django.conf import settings
import hmac
import hashlib
import base64
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
#from models import *
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.db import IntegrityError
@csrf_exempt
def fb_register(request):

    """Return dictionary with signed request data."""

    signed_request = request.POST['signed_request']
    try:

      l = signed_request.split('.', 2)

      encoded_sig = str(l[0])

      payload = str(l[1])

    except IndexError:

      raise ValueError("'signed_request' malformed")



    sig = base64.urlsafe_b64decode(encoded_sig + "=" * ((4 - len(encoded_sig) % 4) % 4))

    data = base64.urlsafe_b64decode(payload + "=" * ((4 - len(payload) % 4) % 4))



    data = json.loads(data)



    if data.get('algorithm').upper() != 'HMAC-SHA256':

      raise ValueError("'signed_request' is using an unknown algorithm")

    else:

      expected_sig = hmac.new(settings.FACEBOOK_APP_SECRET, msg=payload, digestmod=hashlib.sha256).digest()



    if sig != expected_sig:

      raise ValueError("'signed_request' signature mismatch")

    else:
      try:
        user = User.objects.create_user(data['registration']['name'],data['registration']['email'])
        user.save()
        return redirect('/')
      except IntegrityError:
		  return HttpResponse('You have already registered. Return to <a href="/">Home</a>')

