"""
WSGI config for asddiagnoses project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os, sys

exec(open("/bin/activate_this.py").read(), {'__file__': "/bin/activate.py"})

sys.path.append('/core/core')

sys.path.append('/lib/python3.10/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asddiagnoses.settings')

application = get_wsgi_application()
app = application