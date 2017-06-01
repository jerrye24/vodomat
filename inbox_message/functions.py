def parsing_line38(string):
    data = {}
    try:
        data['number'] = int(string[:4])
        data['time_in_message'] = string[4:16]
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
    except:
        return 'error'


def parsing_line48(string):
    data = {}
    try:
        data['number'] = int(string[:4])
        data['time_in_message'] = string[4:14]
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
    except:
        return 'error'
