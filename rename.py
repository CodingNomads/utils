"""Script to rename lab file names with updated folder numbers."""
import os
import re


file_pattern = re.compile(r'^\d{2}\_\d{2}\_\w+\.py')
dir_pattern = re.compile(r'\d{2}')  # path contains two digits, e.g. 04

for root, dirs, files in os.walk('.'):
    for f in files:
        if re.match(file_pattern, f):
            #print('\n' + root)
            if re.search(dir_pattern, root):
                dir_num = re.search(dir_pattern, root).group(0)
                new_name = dir_num + f[2:]
                #print(new_name)
                os.rename(os.path.join(root, f), os.path.join(root, new_name))
