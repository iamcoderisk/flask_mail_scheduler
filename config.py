SECRET_KEY = 'hwfiwfjw340304-3##dd'
# Flask-Mail
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'ekeminyd@gmail.com'
MAIL_PASSWORD ='*******'
CELERY_BROKER_URL = 'pyamqp://guest@localhost//'
CELERY_RESULT_BACKEND = 'rpc://'