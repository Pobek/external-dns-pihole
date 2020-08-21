import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
  DOMAIN_NAME = os.environ.get("DOMAIN_NAME")
  PIHOLE_DNS = os.environ.get("PIHOLE_DNS")
  MODE = os.environ.get("MODE") or "PROD"