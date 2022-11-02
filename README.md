# National Holidays Bot

## Overview

This is a twitter bot that notice **Japanese national holidays**.
The Twitter account is `@NatlHolidaysJP`.

- On the first day of every month, this bot will tweet a list of national holidays for that month.
- On the national holiday, this bot will tweet the name of the holiday.

## Licence
See [LICENCE.md](./LICENCE.md).

## Note

This source code does not contain tokens. If you want to use `main.py`, you have to rewrite `tweet` function, or add `keys.py`.

a example of `keys.py`:
```python
API_KEY             = "AAAAAAABBBBBBCCCCC"
API_SECRET          = "aaaaaaaaaaaaaaaa"

ACCESS_TOKEN        = "12345678999999999zzzzzzzzzZZZzzzzZZ"
ACCESS_TOKEN_SECRET = "qawsedrftgyhujikolp"
```