# -*- coding: utf-8 -*-

from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
import django_rq
from main.tasks import notification


class Command(BaseCommand):
    help = u'Agenda execução da consulta à API de Status do Garoa'

    def handle(self, *args, **options):
        scheduler = django_rq.get_scheduler('default')

        self.stdout.write('Limpando agendamentos antigos...')
        for job in scheduler.get_jobs():
            job.cancel()

        self.stdout.write(u'Agendando tarefa de consulta à API de Status do Garoa...')
        scheduler.schedule(
            scheduled_time=datetime.now(),
            func=notification,
            interval=300,
            repeat=None,
        )

        self.stdout.write('Pronto.')
