import os



OKRA_API_VERSION = os.getenv('OKRA_API_VERSION','v2')
OKRA_ENVIRONMENT = os.getenv('OKRA_ENVIRONMENT', 'sandbox')
OKRA_SECRET = os.getenv('OKRA_SECRET', None) 