import pandas as pd
import math
import hashlib

from IPython.utils.coloransi import value


class DataTable():
    student_names = {}
    groups = {}
    student_to_group = {}
    student_ids = {}
    HW1_results = {}
    HW2_results = {}
    hw1_results = {}
    hw2_results = {}

    def __init__(self):
        table = pd.read_excel("python-2025_HW1.xlsx", sheet_name='hw-01-git', usecols='A:D', index_col=0)
        table_dict = table.to_dict("index")
        self.student_names = {'names': ['_'.join(name.split()) for name in list(table_dict.keys())]}
        self.student_ids = {hashlib.sha1(name.encode()).hexdigest(): name for name in self.student_names['names']}
        self.groups = {24137: [], 24144: [], 24171: []}
        for name in table_dict.keys():
            self.groups[table_dict[name]['Группа']].append('_'.join(name.split()))
            self.student_to_group['_'.join(name.split())] = table_dict[name]['Группа']
        for name in table_dict.keys():
            self.hw1_results['_'.join(name.split())] = table_dict[name]["Баллы"]

        table2 = pd.read_excel("python-2025_HW1.xlsx", sheet_name='hw-02-data-types', usecols='A:D', index_col=0)
        table2_dict = table2.to_dict("index")
        for name in table2_dict.keys():
            self.hw2_results['_'.join(name.split())] = table2_dict[name]["Баллы"]

        table_HW1 = pd.read_excel("python-2025_HW1.xlsx", sheet_name='big-hw-01', usecols='A:D', index_col=0)
        table_HW1_dict = table_HW1.to_dict("index")
        for name in table_HW1_dict.keys():
            self.HW1_results['_'.join(name.split())] = table_HW1_dict[name]["Баллы"]

        table_HW2 = pd.read_excel("python-2025_HW1.xlsx", sheet_name='big-hw-02', usecols='A:D', index_col=0)
        table_HW2_dict = table_HW2.to_dict("index")
        for name in table_HW2_dict.keys():
            self.HW2_results['_'.join(name.split())] = table_HW2_dict[name]["Баллы"]

    def mean_HW1(self):
        val = sum(list(self.HW1_results.values()))
        length = len(self.HW1_results)
        return val / length

    def mean_HW2(self):
        val = sum(list(self.HW2_results.values()))
        length = len(self.HW2_results)
        return val / length

    def mean_HW1_group(self, group: int):
        val = 0
        length = 0
        for name in self.groups[group]:
            if name in self.HW1_results.keys():
                val += self.HW1_results[name]
                length += 1
        if length == 0:
            return math.nan
        return val / length

    def mean_HW2_group(self, group: int):
        val = 0
        length = 0
        for name in self.groups[group]:
            if name in self.HW2_results.keys():
                val += self.HW2_results[name]
                length += 1
        if length == 0:
            return math.nan
        return val / length



    def student_mark(self, student_name: str):
        mark = 0
        if student_name in self.hw1_results.keys():
            if self.hw1_results[student_name] == self.hw1_results[student_name]:
                mark += int(self.hw1_results[student_name])
        if student_name in self.hw2_results.keys():
            if self.hw2_results[student_name] == self.hw2_results[student_name]:
                mark += int(self.hw2_results[student_name])
        if student_name in self.HW1_results.keys():
            if self.HW1_results[student_name] == self.HW1_results[student_name]:
                mark += int(self.HW1_results[student_name])
        if student_name in self.HW2_results.keys():
            if self.HW2_results[student_name] == self.HW2_results[student_name]:
                mark += int(self.HW2_results[student_name])
        return mark


    def return_mark(self, student_id: str, student_name: str | None = None):
        if student_name == None:
            student_name = self.student_ids[student_id]
        mark = 0
        if student_name in self.hw1_results.keys():
            if self.hw1_results[student_name] == self.hw1_results[student_name]:
                mark += int(self.hw1_results[student_name])
        if student_name in self.hw2_results.keys():
            if self.hw2_results[student_name] == self.hw2_results[student_name]:
                mark += int(self.hw2_results[student_name])
        if student_name in self.HW1_results.keys():
            if self.HW1_results[student_name] == self.HW1_results[student_name]:
                mark += int(self.HW1_results[student_name])
        if student_name in self.HW2_results.keys():
            if self.HW2_results[student_name] == self.HW2_results[student_name]:
                mark += int(self.HW2_results[student_name])

        if mark >= 50:
            return 5
        if mark >= 30:
            return 4
        if mark >= 1:
            return 3

    def return_mean_mark_group(self,group:int):
        val = 0
        length = 0
        for name in self.groups[group]:
            val += self.return_mark(0, name)
            length += 1
        if(length == 0): return math.nan
        return val/length


'''data_table = DataTable()
print(data_table.student_names)
print(data_table.groups)
print(data_table.HW1_results)
print(data_table.HW2_results)
print(data_table.mean_HW1())
print(data_table.mean_HW2())
print(data_table.mean_HW1_group(24137))
print(data_table.mean_HW2_group(24144))
print(data_table.student_ids)'''
