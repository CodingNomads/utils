"""
Replaces easily spottable 'us', 'our', 'we' etc. with the corresponding words
such as 'you', 'your', 'you', following the styleguide.
"""
import argparse
import os
import sys

# Create the parser
my_parser = argparse.ArgumentParser(description='Replace "we" with "you".')

# Add the arguments
my_parser.add_argument('File',
                       metavar='file',
                       type=str,
                       help='the file you want to clean')

# Execute the parse_args() method
args = my_parser.parse_args()

input_path = args.File

if not os.path.isfile(input_path):
    print('The file we specified does not exist. Check our spelling.')
    sys.exit()

with open(input_path, 'r+') as fin:
    content = fin.read()
    content = content.replace(" our ", " your ")
    content = content.replace(" we ", " you ")
    content = content.replace(" us ", " you ")
    content = content.replace(" ourselves ", " yourself ")
    content = content.replace("We ", "You ")
    content = content.replace("Our ", "Your ")
    fin.seek(0)
    fin.truncate()
    fin.write(content)
    print(f"Processed our file named {input_path}")
