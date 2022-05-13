# import os 
# from celery import Celery
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')
# app = Celery('base')
# app.config_from_object('django.conf.settings', namespace='CELERY')

# app.conf.beat_schedule = { 
#     'get_coins_data_30s': {
#         'task': 'crypto.tasks.get_coins_data',
#         'schedule': 30.0

#     }
# }

# app.autodiscover_tasks()
