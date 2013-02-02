from django.conf import settings
import hmac
import hashlib
import base64
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from models import Reg_User
from django.shortcuts import redirect,HttpResponseRedirect,render_to_response

@csrf_exempt
def fb_register(request):

    """Return dictionary with signed request data."""
    if request.method == 'GET':
        return render_to_response('error.html')

    signed_request = request.POST['signed_request']
    try:
        l = signed_request.split('.', 2)
        encoded_sig = str(l[0])
        payload = str(l[1])

    except IndexError:
        return render_to_response('error.html')

    sig = base64.urlsafe_b64decode(encoded_sig + "=" * ((4 - len(encoded_sig) % 4) % 4))
    data = base64.urlsafe_b64decode(payload + "=" * ((4 - len(payload) % 4) % 4))
    data = json.loads(data)

    if data.get('algorithm').upper() != 'HMAC-SHA256':
        return render_to_response('error.html')

    else:
        expected_sig = hmac.new(settings.FACEBOOK_APP_SECRET, msg=payload, digestmod=hashlib.sha256).digest()

    if sig != expected_sig:
        return render_to_response('error.html')

    else:
        try:
            user = Reg_User.objects.get(name=data['registration']['name'],email=data['registration']['email'])
            return HttpResponseRedirect('//www.technex.in')
        except:
            user = Reg_User()
            user.name = data['registration']['name']
            user.contact = data['registration']['contact']
            user.college = data['registration']['college']
            user.gender = data['registration']['gender']
            user.birthday = data['registration']['birthday']
            user.location = data['registration']['location']['name']
            user.email = data['registration']['email']
            user.fb_ID = data['user_id']
            user.save()
            return HttpResponseRedirect('//www.technex.in')
