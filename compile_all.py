import glob
import os
import subprocess

# Get all .qmd files
qmd_files = glob.glob('*.qmd')

for file in qmd_files:
    try:
        # Use subprocess to execute the quarto render command
        subprocess.run(['quarto', 'render', file], check=True)
        print(f'Successfully compiled {file}')
    except subprocess.CalledProcessError as e:
        print(f'Failed to compile {file}')
        print(f'Error: {e}')

print('Done compiling all Quarto files.')