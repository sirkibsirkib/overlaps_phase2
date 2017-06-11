import os
import subprocess
in_dir = './inputs/'
out_dir = './outputs/'

e = 0.012
t = 80

fasta_paths = [f for f in os.listdir(in_dir) if f.endswith('.fasta')]
for fasta_path in fasta_paths:
	out_path = out_dir + fasta_path[:-6] + '.out'
	if os.path.isfile(out_path):
		print(out_path, "already exists. skipping.")
	else:
		print(out_path, "solving...")
		call_str = ['./rust_overlaps.exe',
					in_dir+fasta_path,
					out_path,
					str(e),
					str(t),
					'-r', '-t']
		print('CALLING', ' '.join(call_str))
		subprocess.call(call_str)
		print(out_path, "...solved!")

