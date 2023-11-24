def reduce(data): # menghilang kan 2 jenis data, co: IPA dan IPS
    if type(data) is dict:
        if 'IPA' in data:
            del data['IPA']
        if 'IPS' in data:
            del data['IPS']
        res = data 
    elif type(data) is list:
        # uji peserta
        res = data 
    else:
        res = data 
    return res

def combine(data1, data2): # menggabung kan 2 data yang bersifat dict
    if (type(data1) is dict) and (type(data2) is dict):
        res = {}
        for key in data1:
            res[key] = data1[key]
        for key in data2:
            if key not in res:
                res[key] = data2[key]
    else:
        None
    
    return res

def convert(data_json): # ubah dari json of list, jadi list of json: Test!
    if not (type(data_json) is dict):
        return None

    data_list = []
    key_0 = list(data_json)[0]
    len_data = len(data_json[key_0]) # asumsi seluruh data panjangnya sama
    for i in range(len_data):
        res_elm = {}
        for key in data_json:
            res_elm[key] = data_json[key][i]
        data_list.append(res_elm)

    return data_list


if __name__ == "__main__":
    data_absen = {'No': [1.0, 2.0, 3.0, 4.0, 5.0, 6.0], 'Murid': ['Andi', 'Budi', 'Caca', 'Densu', 'Endah', 'Faris'], 'Gender': ['L', 'L', 'P', 'L', 'P', 'L'], 'Kota Asal': ['Jakarta', 'Semarang', 'Jakarta', 'Cilegon', 'Bandung', 'Surabaya']}

    data_smt_1 = {'No': [1.0, 2.0, 3.0, 4.0, 5.0, 6.0], 'Murid': ['Andi', 'Budi', 'Caca', 'Densu', 'Endah', 'Faris'], 'Matematika': [80, 83, 68, 84, 97, 72], 'IPA': [66, 65, 100, 77, 95, 95], 'IPS': [98, 85, 70, 76, 92, 95], 'Bahasa': [84, 94, 65, 63, 74, 98], 'Seni': [66, 60, 78, 61, 99, 90], 'Olahraga': [92, 62, 82, 89, 88, 94]}

    data_smt_2 = [{'No': 1.0, 'Murid': 'Andi', 'Matematika': 69, 'IPA': 97, 'IPS': 86, 'Bahasa': 70, 'Seni': 60, 'Olahraga': 73}, {'No': 2.0, 'Murid': 'Budi', 'Matematika': 75, 'IPA': 81, 'IPS': 71, 'Bahasa': 78, 'Seni': 78, 'Olahraga': 68}, {'No': 3.0, 'Murid': 'Caca', 'Matematika': 81, 'IPA': 100, 'IPS': 77, 'Bahasa': 64, 'Seni': 94, 'Olahraga': 62}, {'No': 4.0, 'Murid': 'Densu', 'Matematika': 64, 'IPA': 64, 'IPS': 69, 'Bahasa': 89, 'Seni': 60, 'Olahraga': 88}, {'No': 5.0, 'Murid': 'Endah', 'Matematika': 86, 'IPA': 80, 'IPS': 63, 'Bahasa': 86, 'Seni': 72, 'Olahraga': 99}, {'No': 6.0, 'Murid': 'Faris', 'Matematika': 62, 'IPA': 80, 'IPS': 78, 'Bahasa': 72, 'Seni': 60, 'Olahraga': 76}]

    print(data_absen)
    print(data_smt_1)
    print(data_smt_2)
    print('\n')

    print('Reduce Data')
    res_reduce = reduce(data_smt_1)
    print(res_reduce)
    print('\n')

    print('Combine')
    res_combine = combine(data_absen, data_smt_1)
    print(res_combine)
    print('\n')

    print('Convert')
    res_convert = convert(data_smt_1)
    print(res_convert)