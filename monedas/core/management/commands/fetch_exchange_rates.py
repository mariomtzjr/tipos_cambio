from django.conf import settings
from django.core.management.base import BaseCommand

from core import utils
from core.models import ExchangeRate


class Command(BaseCommand):
    def handle(self, *args, **options):
        for base_currency in settings.CURRENCIES:
            currencies = list(settings.CURRENCIES).copy()
            currencies.remove(base_currency)
            rates = utils.fetch_exchange_rates(base_currency, currencies)
            for rate_code, rate_value in rates['rates'].items():
                ExchangeRate.objects.create(base_currency=base_currency, currency=rate_code, value=rate_value)
                self.stdout.write('Tasa detectada %s a %s' % (base_currency, rate_code))
