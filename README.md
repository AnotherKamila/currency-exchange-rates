currency-exchange-rates
=======================

Script to retrieve currency exchange rates and put them in a CSV, plus a CSV with data added once a week. Attempts to have a lot of currencies.

Uses the Yahoo Finance API (which has a lot of currencies) to retrieve current exchange rates and stick them in a CSV together with the date.

This repository will be updated once in a while to include weekly data.

Usage
-----

- `getrates.py`: commandline tool to retrieve the data. Make sure to install the requirements (probably in a venv). See `getrates.py --help`.
- `rates.csv`: Data that falls out of the script when it is run once a week (from 2016-12-21).
  Example thing to do with it:
  ```
  # pip install CurrencyConverter
  from currency_converter import CurrencyConverter
  cc = CurrencyConverter('https://raw.githubusercontent.com/AnotherKamila/currency-exchange-rates/master/rates.csv', ref_currency='USD')
  cc.convert(10, 'EUR', 'CHF')
  ```

All of this is best effort: I will not be responsible if your world-domination bot makes wrong decisions because of the data/script here.

License
=======

I believe that the currency exchange rates are public domain, correct me if I am wrong.

I [unlicense](https://unlicense.org/) everything in this repository.
