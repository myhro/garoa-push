# -*- coding: utf-8 -*-

import logging
from django.conf import settings
import redis
import requests
from main.models import PushbulletClient


def notification():
    logging.basicConfig()
    redis_instance = redis.from_url(settings.REDIS_URL)

    garoa_response = requests.get('http://status.garoa.net.br/status')
    if garoa_response.status_code == 200:
        garoa_response_json = garoa_response.json()
        garoa_opened = garoa_response_json.get('open', False)
        garoa_opened_last_check = bool(redis_instance.get('GAROA_OPEN'))

        if garoa_opened:
            garoa_status = 'aberto!'
            redis_instance.set('GAROA_OPEN', True)
        else:
            garoa_status = 'fechado.'
            redis_instance.delete('GAROA_OPEN')

        if garoa_opened != garoa_opened_last_check:
            notification_request = {
                'title': 'Garoa {status}'.format(status=garoa_status),
                'type': 'note',
            }

            for client in PushbulletClient.objects.all():
                response = requests.post('https://api.pushbullet.com/v2/pushes', auth=(client.access_token, ''), data=notification_request)
                if response.status_code == 200:
                    logging.warn(u'Usuário {id} notificado.'.format(id=client.pk))
                else:
                    logging.warn(u'Erro na notificação do Usuário {id}.'.format(id=client.pk))
        else:
            logging.warn(u'O status do Garoa não mudou desde a última verificação.')
    else:
        logging.warn(u'Erro na consulta à API do status do Garoa.')
