import os
import re


f_count, r_count = 0, 0
p = re.compile(r'\[([^]]*)\]\(([^\s^\)]*)[\s\)]')

def update_links(matchobj):
    """Creates a HTML link that opens in a new tab from an appropriate re.match() object."""
    global r_count
    text = matchobj.group(1)
    url = matchobj.group(2)
    r_count += 1
    return f'<a href="{url}" target="_blank">{text}</a>'

current_dir = os.path.dirname(os.path.abspath(__file__))
for file_ in os.listdir(current_dir):
    if file_.endswith(".md"):
        f_count += 1
        with open(f'{current_dir}/{file_}', 'r+') as f:
            content = f.read()
            # rewind to the beginning of the file and cut out the old content
            f.seek(0)
            f.truncate()
            # write back the content with links replaced
            f.write(re.sub(p, update_links, content))

print(f'Done. Replaced {r_count} links across {f_count} files.')
