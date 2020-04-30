from pathlib import Path
import re


f_count, r_count = 0, 0
p = re.compile(r'\[([^]]*)\]\(([^\s^\)]*)[\s\)]')  # regex that matches Markdown Links

def update_links(matchobj):
    """Creates a HTML link that opens in a new tab from an appropriate re.match() object."""
    global r_count
    text = matchobj.group(1)
    url = matchobj.group(2)
    r_count += 1
    return f'<a href="{url}" target="_blank">{text}</a>'


def replace(directory):
    """Replaces all Markdown-style links with HTML new-tab links recursively in a folder structure."""
    global f_count
    print(f'Replacing links in {directory.name}')
    for file_ in sorted(directory.rglob('*.md')):
        # not replacing links in README file because that makes the file that isn't used in the course more messy
        if file_.name != "README.md" and file_.name.endswith(".md"):
            f_count += 1
            with open(file_.absolute(), 'r+') as f:
                content = f.read()
                # rewind to the beginning of the file and cut out the old content
                f.seek(0)
                f.truncate()
                # write back the content with links replaced
                f.write(re.sub(p, update_links, content))


def main():
    current_dir = Path.cwd()
    replace(current_dir)
    print(f'Done. Replaced {r_count} links across {f_count} files.')


if __name__ == "__main__":
    main()
