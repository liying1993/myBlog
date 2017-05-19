# -*- coding: utf-8 -*-
import urllib2
import pycurl
import StringIO
import json
import decimal
import urllib
from django.core.cache import cache
from django.conf import settings
# from utils.wechat import get_access_token, decimal_default, post_url_data, wx_oauth2_url
from share.models import SmsMessage
from django.core.management.base import BaseCommand, CommandError
import httplib
from django.conf import settings
# from debug.decorators import log_exceptions
version = "v2"

sms_tpl_send_uri = "/" + version + "/sms/tpl_single_send.json"
def tpl_send_sms(tpl_id, tpl_value, mobile):
	params = urllib.urlencode({'apikey': settings.SMS_YUNPIAN_APIKEY, 'tpl_id':tpl_id, 'tpl_value': urllib.urlencode(tpl_value), 'mobile':mobile})
	headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
	conn = httplib.HTTPSConnection(settings.SMS_HOST, port=443, timeout=30)
	conn.request("POST", sms_tpl_send_uri, params, headers)
	response = conn.getresponse()
	response_str = response.read()
	conn.close()
	return response_str
class Command(BaseCommand):
    args = '<Ref Ref ...>'
    help = 'Send notice to user...'
    version = "v2"
    sms_tpl_send_uri = "/" + version + "/sms/tpl_single_send.json"

    def handle(self, *args, **options):
        # for message in SmsMessage.objects.filter(need_notice=True):
        #     if message.message_type == 0:
                tpl_id = 1733098
                # ref = message.message_text

                # tpl_value = {'#number#': ref}
                tpl_value = {'#number#': '123121'}
                # mobile = message.mobile
                mobile = '13040871404'
                # tpl_send_sms(tpl_id, tpl_value, mobile)
                # message.need_notice = False
                # message.save()





