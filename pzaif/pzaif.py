#!usr/bin/env python
#-*- coding: utf-8 -*-

import requests
import urllib
from datetime import datetime
import dateutil.parser
import hmac
import hashlib

class ExchangeAPI():

    def __init__(self,key,secret):
        """
        Initialize instance variable
        """
        self.__session=requests.session()
        self.tapi_url="https://api.zaif.jp/tapi"
        self.__key=key
        self.__secret=secret

    def hmac_sha512(self,secret, message):
        sign = hmac.new(secret, message, hashlib.sha512).hexdigest()
        return sign

    def nonce(self):
        # 1/10秒単位のタイムスタンプ
        return datetime.now().strftime('%s.%f')

    def unixtime(self,str):
        utime = dateutil.parser.parse(str).strftime('%s')
        return utime

    def call_api(self,data):

        data.update({'nonce': self.nonce()})

        # HMAC-SHA512
        sign = urllib.urlencode(data)
        sign = self.hmac_sha512(self.__secret, sign)

        # headers
        headers = {'Key': self.__key,
                   'Sign': sign}

        response=self.__session.post(self.tapi_url,data=data,headers=headers)

        return response


    def get_info(self):

        result=self.call_api({'method':'get_info'}).json()

        return result

    def trade_history(self,**kwargs):

        data=kwargs
        data.update({'method':'trade_history'})


        if data.has_key('since'):
            data['since']= self.unixtime(data['since'])
        if data.has_key('end'):
            data['end'] = self.unixtime(data['end'])

        result = self.call_api(data).json()

        return result

    def active_orders(self,**kwargs):

        data=kwargs
        data.update({'method':'active_orders'})

        result = self.call_api(data).json()

        return result


    def trade(self, currency_pair, action, price, amount, **kwargs):
        data = {'method':'trade',
                'currency_pair': currency_pair,
                'action': action,
                'price': price,
                'amount': amount}
        data.update(kwargs)

        result = self.call_api(data).json()

        return result


    def cancel_all_order(self):
        order_list=self.active_orders()
        order_list=order_list['return'].keys()

        for id in order_list:
            print self.cancel_order(id)

    def cancel_order(self,order_id):
        data = {'method': 'cancel_order',
                'order_id': order_id}

        result = self.call_api(data).json()

        return result

    def withdraw(self,currency,address,amount,**kwargs):
        data = {'method':'withdraw',
                'currency':currency,
                'address':address,
                'amount':amount}
        data.update(kwargs)

        if data.has_key('since'):
            data['since']=self.unixtime(data['since'])
        if data.has_key('end'):
            data['end'] = self.unixtime(data['end'])

        result=self.call_api(data).json()

        return result

    def deposit_history(self,currency,**kwargs):
        data = {'method':'deposit_history',
                'currency':currency}
        data.update(kwargs)

        if data.has_key('since'):
            data['since']=self.unixtime(data['since'])
        if data.has_key('end'):
            data['end'] = self.unixtime(data['end'])

        result=self.call_api(data).json()

        return result


class PublicAPI():

    def __init__(self):
        """
        Initialize instance variable
        """
        self.api_url = "https://api.zaif.jp/api/1"

    def last_price(self,currency="btc_jpy"):
        url=self.api_url+"/last_price/"+currency
        res=requests.get(url)
        return res.json()

    def ticker(self,currency="btc_jpy"):
        url=self.api_url+"/ticker/"+currency
        res=requests.get(url)
        return res.json()

    def trades(self,currency="btc_jpy"):
        url=self.api_url+"/trades/"+currency
        res=requests.get(url)
        return res.json()


    def depth(self,currency="btc_jpy"):
        url=self.api_url+"/depth/"+currency
        res=requests.get(url)
        return res.json()
