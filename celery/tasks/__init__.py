from celery import Celery

url = "redis://localhost:6379/0"
app = Celery('tasks', broker=url, backend=url)

app.conf.result_backend = 'redis://localhost:6379/0'
app.conf.broker_transport_options = {'visibility_timeout': 300}

# app.conf.update(
#     CELERY_TASK_SERIALIZER='json',
#     CELERY_ACCEPT_CONTENT=['json'],  # Ignore other content
#     CELERY_RESULT_SERIALIZER='json',
#     CELERY_TIMEZONE='Europe/Oslo',
#     CELERY_ENABLE_UTC=True,
#     # CELERY_RESULT_BACKEND='rpc',
#     CELERY_RESULT_PERSISTENT=True,
#     CELERY_RESULT_BACKEND=url,
# )

# app.conf["CELERY_ALWAYS_EAGER"] = False
# app.conf["CELERYD_CONCURRENCY"] = 4

# CELERY_TASK_ANNOTATIONS = {'*': {'max_retries': 3}}

from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)

print(1)
