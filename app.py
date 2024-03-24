import sys
import pandas as pd
from enum import Enum

class RateEnum(Enum):
    Not_Second = ('介護保険第２号被保険者に該当しない場合', 0.0977)
    Second = ('介護保険第２号被保険者に該当する場合', 0.1137)
    Employees_Insurance = ('厚生年金保険料', 0.183)

FILE_PATH = 'import/range.tsv'
def load_tsv(file_path):
    tmp_list = pd.read_csv(file_path, sep='\t').values.tolist()
    return_list = []
    for l in tmp_list:
        tmp_l = []
        for x in l:
            x = x.replace(',', '').replace(' ', '')
            tmp_l.append(x)
        return_list.append(tmp_l)
    return return_list

CENTER_PATH = 'import/center.txt'
def load_center(file_path):
    return_list = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            l = line.replace(' ', '').replace('\n', '').replace('\r', '')
            if l != '' and l != '0':
                return_list.append(int(l))
    return return_list

def get_index(salaly, data):
    for i in range(len(data)):
        if int(data[i][0]) <= salaly <= int(data[i][1]):
            return i

def exec():
    args = sys.argv
    salaly = int(args[1])

    data = load_tsv(FILE_PATH)
    center = load_center(CENTER_PATH)

    index = get_index(salaly, data)
    
    print(f'報酬月額: {salaly}')
    print(f'標準報酬月額: {center[index]}')
    for e in RateEnum:
        print(f'{e.value[0]}: {center[index] * e.value[1]}')
        print(f'{e.value[0]}（折半額）: {(center[index] * e.value[1]) / 2}')
    
if __name__ == '__main__':
    exec()