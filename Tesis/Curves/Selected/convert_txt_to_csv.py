import numpy as np


def get_id_list(temp_list):
    l_list = []
    for l in temp_list:
        r = l.split("\t")
        r = r[1].split('\n')
        l_list.append(float(r[0]) * 1000)
    return l_list


file=open('L 100-24.txt', 'r')
text = file.readlines()

init = 2
end = 83
temp_1 = text[init:end]

init = end + 1
end = init + 81
temp_2 = text[init:end]

init = end + 1
end = init + 81
temp_3 = text[init:end]

init = end + 1
end = init + 81
temp_4 = text[init:end]

init = end + 1
end = init + 81
temp_5 = text[init:end]

init = end + 1
end = init + 81
temp_6 = text[init:end]

init = end + 1
end = init + 81
temp_7 = text[init:end]

init = end + 1
end = init + 81
temp_8 = text[init:end]

vgs1 = np.array(get_id_list(temp_1))
