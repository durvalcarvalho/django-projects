import contextlib
import datetime as dt

from documents.models import Test, Document
from django.core.management import call_command



def my_scheduled_job():
    Test.objects.create(name='test')
    print('I am a scheduled job!')


def documents_expired_check():
    now = dt.datetime.now()
    Document.objects.filter(expiration_date__lte=now).update(expired=True)


def backup_database():
    with contextlib.suppress(Exception):
        call_command('dbbackup')
