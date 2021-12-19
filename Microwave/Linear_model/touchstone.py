from src.read import *
import re
from datetime import datetime

class Touchstone:

    def __init__(self, path):
        self.readings = []
        file = open(path, 'r')
        lines = file.readlines()
        file.close()
        lines = self.clean_lines(lines)
        for line in lines:
            line = line.split()
            read = Read(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8])
            self.readings.append(read)

    @staticmethod
    def clean_lines(lines):
        valid_list = []
        for line in lines:
            # Start with !
            r = re.match("^[!\n\#]", line)
            if not r:
                valid_list.append(line.rstrip("\n"))
        return valid_list

    @staticmethod
    def write_touchstone(parameters_list, touchstone_name):
        # Creating text file
        file = open(touchstone_name, "w")
        # datetime object containing current date and time
        now = datetime.now()
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        file.write("! Created on " + dt_string + "\n")
        file.write("! CINVESTAV" + "\n\n")

        file.write("! S-Parameter data\n")
        file.write("! freq S11 S21 S12 S22\n")
        file.write("# GHz S RI R 50\n")
        for line in parameters_list:
            frequency, s11, s12, s21, s22 = line[0], line[1], line[2], line[3], line[4]
            file.write("{:.15f}".format(frequency) + " " + "{:.15f}".format(s11.real) + " " + "{:.15f}".format(s11.imag) + " "
                       + "{:.15f}".format(s21.real) + " " + "{:.15f}".format(s21.imag) + " "
                       + "{:.15f}".format(s12.real) + " " + "{:.15f}".format(s12.imag) + " "
                       + "{:.15f}".format(s22.real) + " " + "{:.15f}".format(s22.imag) + "\n")
        file.close()