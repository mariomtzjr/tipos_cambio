# tipos_cambio

## Especificaciones
En el archivo settings.py:
- BASE_CURRENCY: Moneda base
- CURRENCIES: Monedas disponibles

## API
[EXCHANGE RATES API](https://api.exchangeratesapi.io)

## Uso
`python manage.py fetch_exchange_rates`  
La salida del comando anterior devuelve la tasa de conversión modificando la moneda base por cada opción disponible en la variable currencies.  
 ```
 ## URL ##
https://api.exchangeratesapi.io/latest?base=EUR&symbols=MXN,USD
# Response #
{'rates': {'MXN': 26.2304, 'USD': 1.0875}, 'base': 'EUR', 'date': '2020-05-13'}
Tasa detectada EUR a MXN
Tasa detectada EUR a USD
## URL ##
https://api.exchangeratesapi.io/latest?base=MXN&symbols=EUR,USD
# Response #
{'rates': {'EUR': 0.0381237038, 'USD': 0.0414595279}, 'base': 'MXN', 'date': '2020-05-13'}
Tasa detectada MXN a EUR
Tasa detectada MXN a USD
## URL ##
https://api.exchangeratesapi.io/latest?base=USD&symbols=EUR,MXN
# Response #
{'rates': {'EUR': 0.9195402299, 'MXN': 24.119908046}, 'base': 'USD', 'date': '2020-05-13'}
Tasa detectada USD a EUR
Tasa detectada USD a MXN
 ````
