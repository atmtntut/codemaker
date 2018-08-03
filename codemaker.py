import tkinter as tk
from collections import namedtuple
import re

Var = namedtuple('Var', 'name first count step')
VarNames = ('A', 'B', 'C', 'D', 'E', 'F')

class CodeMaker():
    def __init__(self):
        self.template = ''
        self.result = ''
        self.vars = {}
        self.cur_vars = []
        for x in VarNames:
            self.vars[x] = Var(x, 0, 1, 1)

    def set_template(self, temp):
        self.template = temp
        pattern = re.compile(r'\([A-F]\)')
        ret = pattern.findall(temp)
        ret = [x[1:2] for x in ret]
        self.cur_vars = []
        for x in ret:
            self.cur_vars.append(self.vars[x])

    def make_code(self):
        total_count = 0
        for v in self.cur_vars:
            total_count += v.count
        for i in range(0, total_count):



c = CodeMaker()
c.make_code()