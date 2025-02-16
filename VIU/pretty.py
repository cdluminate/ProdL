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
        print(f'| {idx.ljust(2)} | {name.ljust(28)} | {util.rjust(6)} | {used.rjust(10)} | {total.rjust(10)} |', flush=True)
    else:
        print('no match. seems to be a bug', flush=True)
