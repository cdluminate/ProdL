default: gpustat

# list of all GPU servers.
.viu_servers.txt:
	touch .viu_servers.txt
	seq 1 14 | xargs -I {} echo viu{}.wse.jhu.edu >> .viu_servers.txt

# list of all GPU servers + storage server.
.viu_servers_all.txt:
	touch .viu_servers_all.txt
	seq 1 14 | xargs -I {} echo viu{}.wse.jhu.edu >> .viu_servers_all.txt
	echo viu-storage.wse.jhu.edu >> .viu_servers_all.txt

# common args for ansible
COMMON_ARGS_ALL = -i .viu_servers_all.txt -o -e 'ansible_remote_tmp=/dev/shm/'
COMMON_ARGS = -i .viu_servers.txt -o -e 'ansible_remote_tmp=/dev/shm/'

# ping all servers
ping: .viu_servers_all.txt
	ansible $(COMMON_ARGS_ALL) all -m ping -o

# list all tmux sessions
tmuxls: .viu_servers.txt
	ansible $(COMMON_ARGS) all -m shell -a "tmux ls"

# list all tmux sessions
gpustat: .viu_servers.txt
	ansible $(COMMON_ARGS) all -m shell -a "nvidia-smi --query-gpu=index,name,utilization.gpu,memory.used,memory.total --format=csv" | sed 's/\\n/\n/g' | python3 pretty.py
