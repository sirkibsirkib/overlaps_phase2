import os
import subprocess
in_dir = './inputs/'
out_dir = './outputs/'

e = 0.012
t = 80

modes = {"kucherov_1","kucherov_2","kucherov_3","kucherov_4","kucherov_5","kucherov_6","valimaki2"}
fasta_path = "5VM_real.p1.40000.fasta"


fasta_paths = [f for f in os.listdir(in_dir) if f.endswith('.fasta')]
for mode in modes:
	out_path = out_dir + fasta_path[:-6] + '.out'
	if os.path.isfile(out_path):
		print(out_path, "already exists. skipping.")
	else:
		print(out_path, "solving...")
		call_str = ['./rust_overlaps_measure.exe',
					in_dir+fasta_path,
					out_path[:-4]+mode+'.out',
					str(e),
					str(t),
					'-r', '-t', ('-m='+mode)
					]
		print('CALLING', ' '.join(call_str))
		subprocess.call(call_str)
		print(out_path, "...solved!")

