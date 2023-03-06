"""
График btc/usdt
Посчитать еженедельную динамику роста и падения стоимости в процентах по телам свеч (годовой диапазон 2023)
Поставить условие, если роста стоимости больше чем падения, тренд восходящий, иначе нисходящий.
Для вывода данных тип dict. Например, каждой неделе как ключу присвоить значение в %
Чтобы найти разницу в процентах, можно использовать формулу: 
(«новая» стоимость – «прежняя» стоимость) / «прежняя» стоимость * 100%.
"""""
# Atayev Akmuhammet
# Lab 10

from binance import Client
import pandas as pd
import mplfinance as mpf


class Data_BTCUSDT:

    def get_data(self, symbol):
        _client = Client()
        print('DATA BTC-USDT from 2023y')
        _interval = input('interval: d = day / w = week / else = month\nChoice = ')
        if _interval == 'd':
            _kline = _client.get_historical_klines(symbol, _client.KLINE_INTERVAL_1DAY, '1 Jan, 2023')  # получение данных
            _data = pd.DataFrame(_kline)
        elif _interval == 'w':
            _kline = _client.get_historical_klines(symbol, _client.KLINE_INTERVAL_1WEEK, '1 Jan, 2023')
            _data = pd.DataFrame(_kline)
        else:
            _kline = _client.get_historical_klines(symbol, _client.KLINE_INTERVAL_1MONTH, '1 Jan, 2023')
            _data = pd.DataFrame(_kline)

        # inplace - сделать копию или обновить текущий датаФрейм / axis - для удаления столбцы или строки (1-столбец, 0-строка)
        _data.drop(columns=_data.columns[6:], axis=1, inplace=True)  # удаление не нужных столбцов
        _data.columns = ['open_time', 'open', 'high', 'low', 'close', 'volume']  # названия столбцов


        # преобразования
        _data.index = pd.to_datetime(_data['open_time'] / 1000, unit='s')    # 'open-time' => date-time ************

        # others = > float
        _numeric = ['open', 'high', 'low', 'close', 'volume']
        _data[_numeric] = _data[_numeric].apply(pd.to_numeric, axis=1)

        print(_data)
        return mpf.plot(_data, type='candle', style='charles', volume=True)  # graph


ob = Data_BTCUSDT()
print(ob.get_data('BTCUSDT'))

