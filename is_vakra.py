import os
import sys

import pandas as pd

df = pd.read_csv('500_Ragas_Phase_1.csv')

is_vakra = []
ragas = df['Name_Eng'].to_list()
aros = df['Arohana_Order'].to_list()
avros = df['Avarohana_Order'].to_list()

swara_num_map = dict()
swara_num_map["S"] = 1
swara_num_map["R1"] = 2
swara_num_map["R2"] = 3
swara_num_map["R3"] = 4
swara_num_map["G1"] = 5
swara_num_map["G2"] = 6
swara_num_map["G3"] = 7
swara_num_map["M1"] = 8
swara_num_map["M2"] = 9
swara_num_map["P"] = 10
swara_num_map["D1"] = 11
swara_num_map["D2"] = 12
swara_num_map["D3"] = 13
swara_num_map["N1"] = 14
swara_num_map["N2"] = 15
swara_num_map["N3"] = 16
swara_num_map["S'"] = 17


def vakra(aro, avro): #arohana and avarohana are passed as lists of numbers
    n1 = len(aro)
    n2 = len(avro)
    if n1 > 8:
        return 1
    if n2 > 8:
        return 2
    aro_sorted = sorted(aro)
    avro_sorted = sorted(avro, reverse=True)
    print(aro)
    print(aro_sorted)
    print(avro)
    print(avro_sorted)
    if aro == aro_sorted and avro == avro_sorted:
        return 0
    if aro != aro_sorted and avro != avro_sorted:
        return 3
    if aro != aro_sorted:
        return 1
    if avro != avro_sorted:
        return 2
    return 0

for i in range(0, len(ragas)):
    raga = ragas[i]
    print(raga)
    aro = aros[i].split("|")
    avro = avros[i].split("|")
    print(aro)
    print(avro)
    aro_num = []
    avro_num = []
    for j in aro:
        aro_num.append(swara_num_map[j])
    for j in avro:
        avro_num.append(swara_num_map[j])
    is_vakra.append(vakra(aro_num, avro_num))

df['is_vakra'] = is_vakra

df.to_csv('500_Ragas_Phase_1_w_vakra.csv')
