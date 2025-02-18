'''
Pretty print such kind of output:
viu14.wse.jhu.edu | CHANGED | rc=0 | (stdout) index, name, utilization.gpu [%], memory.used [MiB], memory.total [MiB]
0, NVIDIA H100 80GB HBM3, 100 %, 78942 MiB, 81559 MiB
1, NVIDIA H100 80GB HBM3, 98 %, 78990 MiB, 81559 MiB
2, NVIDIA H100 80GB HBM3, 100 %, 78990 MiB, 81559 MiB
3, NVIDIA H100 80GB HBM3, 100 %, 78750 MiB, 81559 MiB
4, NVIDIA H100 80GB HBM3, 100 %, 21340 MiB, 81559 MiB
5, NVIDIA H100 80GB HBM3, 98 %, 19760 MiB, 81559 MiB
6, NVIDIA H100 80GB HBM3, 100 %, 19742 MiB, 81559 MiB
7, NVIDIA H100 80GB HBM3, 99 %, 19770 MiB, 81559 MiB
'''
import sys
import re
import rich
console = rich.get_console()

RESET = '\033[0m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BG_RED = '\033[41m'
BG_GREEN = '\033[42m'
BG_YELLOW = '\033[43m'

for line in sys.stdin:
    line = line.strip()
    if '| CHANGED |' in line:
        m = re.match(r'^(.*).wse.jhu.edu | CHANGED |.*', line)
        hostname = m.group(1)
        print(f' Host: {hostname} '.center(72, '='), flush=True)
        print('| ID | Name                         |  Util  |    Used    |    Total   |', flush=True)
    elif re.match(r'^\d+,', line):
        m = re.match(r'(\d+), (.*?), (.*?), (.*?), (.*?)$', line)
        idx, name, util, used, total = m.groups()
        idx = idx.ljust(2)
        name = name.ljust(28)
        util = util.ljust(6)
        used = used.rjust(10)
        total = total.rjust(10)
        mem_ratio = float(used.split()[0]) / float(total.split()[0])
        utility = int(util.split()[0])
        if mem_ratio > 0.5 or utility > 80:
            name = BG_RED + name + RESET
            used = RED + used + RESET
        elif mem_ratio > 0.2 or utility > 50:
            name = BG_YELLOW + name + RESET
            used = YELLOW + used + RESET
        else:
            name = BG_GREEN + name + RESET
            used = GREEN + used + RESET
        if utility > 50:
            util = RED + util + RESET
        elif utility > 20:
            util = YELLOW + util + RESET
        else:
            util = GREEN + util + RESET
        print(f'| {idx} | {name} | {util} | {used} | {total} |', flush=True)
    else:
        print('no match. seems to be a bug', flush=True)
