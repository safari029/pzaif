# PZaif

python用のZaifAPIラッパー。
入力値の検証等は実施せずにそのままAPIをコールさせてます。

# Enviroment
 python2.7

# Install

pipでインストールしてください。

```
pip install git+https://github.com/safari029/pzaif
```

# Usage

現状はExchangeAPI(),PublicAPI()を作成してます。
以下でimportします。

```
from pzaif import pzaif
```

## ExchangeAPI()

ExchangeAPI()にはAPIキーが必要です。



```
exapi=pzaif.ExchangeAPI(key,secret)

exapi.get_info()

#時刻関連のパラメータはdateutilで適宜パースされます。
exapi.trade_history(count=3,currency_pair="btc_jpy",since="2016/01/01 00:00)
```

## PublicAPI()

currency(通貨)を指定しない場合はデフォルト"btc_jpy"が選択されます。

```
pubapi=pzaif.ExchangeAPI()

pubapi.last_plice("btc_jpy")
```

## StreamingAPI
気が向いたら作ります。