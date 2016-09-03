# PZaif

python用のZaifAPIラッパー。
入力値の検証等は実施せずにそのままAPIをコールさせてます。

# Enviroment
 python2.7

# Install

pipでインストールしてください。

```
pip install git+https://github.com/safari029/simple_zaif
```

# Usage

現状はExchangeAPI(),PublicAPI()を作成してます。
ExchangeAPI()にはAPIキーが必要です。

```
import pzaif
```

## ExchangeAPI()

```
exapi=pzaif.ExchangeAPI(key,secret)

exapi.get_info()

exapi.trade_history(count=3,currency_pair="btc_jpy",since="2016/01/01 00:00)　#時刻関連のパラメータはdateutilでパースされます。
```

## PublicAPI()

currency(通貨)を指定しない場合はデフォルト"btc_jpy"が選択されます。

```
pubapi=pzaif.ExchangeAPI()

pubapi.last_plice("btc_jpy")
```

## StreamingAPI
気が向いたら作ります。

