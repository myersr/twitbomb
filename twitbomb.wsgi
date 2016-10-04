import sys

sys.stdout = sys.stderr
sys.path.insert(0,"/var/www/twitbomb/")

from app import app as application
