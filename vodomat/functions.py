import datetime


def parsing_line38(string, time):
    number = int(string[:4])
    data = {}
    try:
        data['number'] = number
        data['how_money'] = float(string[16:22]) / 100
        data['water_balance'] = float(string[22:28]) / 100
        data['water_price'] = float(string[28:32]) / 100
        data['ev_water'] = int(string[32])
        data['ev_bill'] = int(string[33])
        data['ev_volt'] = int(string[34])
        data['ev_counter_water'] = int(string[35])
        data['event'] = int(string[36:38])
        data['ev_register'] = 0
        data['grn'] = 0
        data['kop'] = 0
        data['time_to_block'] = 99
        return data
    except Exception as err_38:
        file_38 = open('/tmp/error_38.txt', 'a')
        error_38 = time.strftime('%c') + ' AVTOMAT: %s - ' % number + str(err_38) + '\n'
        file_38.write(error_38)
        file_38.close()
        return 'error'


def parsing_line48(string, time):
    number = int(string[:4])
    data = {}
    try:
        data['number'] = number
        data['how_money'] = float(string[14:20]) / 100
        data['water_balance'] = float(string[20:26]) / 100
        data['water_price'] = float(string[26:30]) / 100
        data['ev_water'] = int(string[40])
        data['ev_bill'] = int(string[42])
        data['ev_volt'] = int(string[41])
        data['ev_counter_water'] = int(string[43])
        data['event'] = int(string[46:48])
        data['ev_register'] = int(string[44])
        data['grn'] = int(string[32:36])
        data['kop'] = int(string[36:40])
        data['time_to_block'] = int(string[30:32])
        return data
    except Exception as err_48:
        file_48 = open('/tmp/error_48.txt', 'w')
        error_48 = time.strftime('%c') + ' AVTOMAT: %s - ' % number + str(err_48) + '\n'
        file_48.write(error_48)
        file_48.close()
        return 'error'


def last_date():
    year = datetime.date.today().year
    month = datetime.date.today().month - 1
    if datetime.date.today().month == 1:
        year -= 1
        month = 12
    last = datetime.datetime(year, month, 1)
    last_7 = datetime.date.today() - datetime.timedelta(days=7)
    return last, last_7
