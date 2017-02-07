import os 
import sys 
import site
 
# Add the site-packages of the chosen virtualenv to work with 
site.addsitedir('/root/venv/local/lib/python2.7/site-packages') 
# Add the app's directory to the PYTHONPATH 
sys.path.append('/root/ck_management') 
sys.path.append('/root/ck_management/ck_management') 
os.environ['DJANGO_SETTINGS_MODULE'] = 'ck_management.settings' 
# Activate your virtual env 
activate_env=os.path.expanduser("/root/venv/bin/activate_this.py") 
execfile(activate_env, dict(__file__=activate_env)) 
from django.core.wsgi import get_wsgi_application 
application = get_wsgi_application()

