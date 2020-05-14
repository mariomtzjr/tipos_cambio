import requests
from decimal import Decimal, ROUND_HALF_UP

# Api para obtener el valor de cada moneda
EXCHANGERATES_API_URL = 'https://api.exchangeratesapi.io/latest?base=%s&symbols=%s'

def fetch_exchange_rates(base_currency, currencies):
    """Tipo de cambio
    Esta función realiza la conversión al tipo de cambio que se especifica
    en la variable CURRENCIES del archivo settings.py de acuerdo
    a la moneda base.
    """

    # Limpiamos la variable currencies
    currencies = (str(currencies)).replace('[', '').replace(']', '').replace(' ', '').replace("'", '')
    url = EXCHANGERATES_API_URL % (base_currency, currencies)

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
