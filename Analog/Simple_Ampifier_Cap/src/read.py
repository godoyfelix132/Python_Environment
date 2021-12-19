import re
from src.mosfet import *


class Read:
    def __init__(self, root):
        file = open(root, 'r')
        text = file.readlines()
        dc_lines, ac_lines = self.split_dc_ac(text)
        header_list, gm_list, gds_list = get_ac_list(ac_lines)
        self.mosfets = self.create_objects(header_list, gm_list, gds_list)

    @staticmethod
    def create_objects(header_list, gm_list, gds_list):
        mos_list = []
        for i in range(len(header_list)):
            mos = Mosfet(header_list[i], gm_list[i], gds_list[i])
            mos_list.append(mos)
        return mos_list


    @staticmethod
    def clean_list(list):
        for i in range(len(list)):
            n = re.findall(r"[-+]?\d*\.\d+|\d+", list[i])
            n = float(n[0])
            if 'm' in list[i]:
                list[i] = n * (10**-3)
            else:
                if 'u' in list[i]:
                    list[i] = n * (10**-6)
                else:
                    if 'n' in list[i]:
                        list[i] = n * (10**-9)
                    else:
                        if 'p' in list[i]:
                            list[i] = n * (10**-12)
        return list

    @staticmethod
    def split_dc_ac(text):
        dc_lines = []
        ac_lines = []
        state = 0
        for line in text:
            if state == 0:
                res = re.search(r'\bDC ANALYSIS', line)
                if res:
                    dc_lines.append(line)
                    state = 1
            if state == 1:
                res = re.search(r'\bAC SMALL-SIGNAL', line)
                if res:
                    ac_lines.append(line)
                    state = 2
                else:
                    dc_lines.append(line)
            if state == 2:
                res = re.search(r'\bVOLTAGE SOURCES', line)
                if res:
                    break
                else:
                    ac_lines.append(line)
        return dc_lines, ac_lines


def get_ac_list(ac_lines):
    header_list = []
    gm_list = []
    gds_list = []
    for line in ac_lines:
        res = re.search(r'\bMn|\bMp', line)
        if res:
            li = re.findall(r'\S+', line)
            header_list = header_list + li

        res = re.match(r'GM ', line)
        if res:
            li = re.findall(r'\S+', line)
            gm_list = gm_list + li[1:]

        res = re.match(r'GDS ', line)
        if res:
            li = re.findall(r'\S+', line)
            gds_list = gds_list + li[1:]
    gm_list = Read.clean_list(gm_list)
    gds_list = Read.clean_list(gds_list)
    return header_list, gm_list, gds_list


if __name__ == '__main__':
    r = Read("D:\\Respaldo\\Maestria\\2 - Cuatrimestre\\Analog\\1er Parcial\\Simulaciones\\practica\\Source follower\\Source follower.op")
    for m in r.mosfets:
        if m.name == 'Mna3':
            mna3 = m
    print(mna3.gds)