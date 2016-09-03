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
[こちら](https://zaif.jp/api_keys)で取得できます。

```
exapi=pzaif.ExchangeAPI(key,secret)

exapi.get_info()

#時刻関連のパラメータはdateutilで適宜パースされます。
exapi.trade_history(count=3,currency_pair="btc_jpy",since="2016/01/01 00:00)
```

以下利用可能です。
* get_info : 残高などのアカウント情報を取得する
* trade_history : 取引履歴を取得する
* active_orders : 現在有効な注文一覧を取得する
* trade : 取引注文を行う
* cancel_order : 注文を取り消す
* withdraw : 暗号通貨の出金リクエストを行う
* deposit_history : 入金履歴を取得する
* withdraw_history : 出金履歴を取得する

## PublicAPI()

currency(通貨)を指定しない場合はデフォルト"btc_jpy"が選択されます。

```
pubapi=pzaif.ExchangeAPI()

pubapi.last_plice("btc_jpy")
```

以下利用可能です。
* last_price : 終値を得る
* ticker : ティッカー
* trades : 全ての取引履歴
* depth : 板情報


## StreamingAPI
気が向いたら作ります。
