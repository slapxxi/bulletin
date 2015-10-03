from nose.tools import ok_, eq_, raises

from django.test import Client
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from utils.decorators import test

from ads.models import Ad
from ads.forms import AdForm
