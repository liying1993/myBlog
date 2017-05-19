# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class SmsMessage(models.Model):

	MTYPE = (('0',u'qqq'), ('1',u'qq'), ('2',u'xx'), ('3',u'as'), ('4',u'ds'))


	message_type = models.CharField(max_length=4, choices = MTYPE, default = '1')

	mobile = models.CharField(unique=True, max_length=32, default='', null=True, blank=True)


	message_text = models.CharField(max_length=2046, null=True, blank=True, default=None)
	
	need_notice = models.BooleanField(default=False)