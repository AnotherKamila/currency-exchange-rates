currency-exchange-rates
=======================

Script to retrieve currency exchange rates and put them in a CSV, plus a CSV with data added every day. Attempts to have a lot of currencies.

Uses the Yahoo Finance API (which has a lot of currencies) to retrieve current exchange rates and stick them in a CSV together with the date.

This repository will be updated once in a while to include daily data.

This should not break when the world changes and currencies appear or disappear -- the script will just retrieve whatever is available and correctly merge the new data with the old CSV. (Therefore the CSV file *cannot* be append-only. At least it is written atomically.)

Usage
-----

- `rates.csv`: Data that falls out of the script when it is run once a day (from 2017-01-10).
  Example thing to do with it:
  
  ```python
  from datetime import date
  from currency_converter import CurrencyConverter  # https://pypi.python.org/pypi/CurrencyConverter/
  URL = 'https://raw.githubusercontent.com/AnotherKamila/currency-exchange-rates/master/rates.csv'
  cc = CurrencyConverter(URL, ref_currency='USD')
  print(cc.convert(10, 'EUR', 'CHF', date=date(2016, 12, 20)))  # prints 10.69
  ```
- `getrates.py`: commandline tool to retrieve the data. Make sure to install the requirements (probably in a venv). See `getrates.py --help`.
- `cron.sh`: If your venv is called `venv` and the requirements are installed, this will run `getrates.py` and commit the updated `rates.csv`.

All of this is best effort: I will not be responsible if your world-domination bot makes wrong decisions because of the data/script here.

License
=======

I believe that the currency exchange rates are public domain, correct me if I am wrong.

I [unlicense](https://unlicense.org/) everything in this repository. But it would be nice if you linked to this repo when you use it.
