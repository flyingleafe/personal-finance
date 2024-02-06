# Personal finance tracking
What constitutes a good personal finance accounting app?

## Requirements
+ Multi-currency accounting, including crypto tokens
+ Automation of all transaction imports where possible
+ Support of easy manual transaction imports (e.g. for cash)
+ Automatic re-calculation of prices between currencies
    + Getting reports renumerated in any currency
+ Automatic accounting exchange and transfer fees/costs
+ Pretty customizable visualizations (e.g. using matplotlib/plotly/jupyter)

## Accounting

### Double-entry bookkeeping
#### [Ledger](https://github.com/ledger/ledger)
#### [Beancount](https://github.com/beancount/beancount)
+ TODO: Can it be used customly, as a lib?

## Automatic data imports

### Crypto wallets

#### Tron (TRC-20)
+ `tronscan-client` package
  + Support for fetching transactions + transfers from API

### Crypto exchanges

#### Binance
+ [Python SDK](https://github.com/sammchardy/python-binance)

#### Bybit
+ [Python SDK](https://github.com/bybit-exchange/pybit)

### Banks
#### Wise
+ [Wise API](https://docs.wise.com/api-docs/api-reference)
  + TODO: Which methods are available for personal accounts?

#### OCBC NISP
+ ???

#### Tinkoff
+ [Tinkoff API](https://developer.tinkoff.ru/docs/api)
  + TODO: Non-business access -- ???

#### Manual CSV imports
+ TODO: CLI import from CSV
+ TODO: Telegram bot for CSV file forwarding


