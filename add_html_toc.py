"""Create a HTML file copy with a clickable TOC through rendering a given .md file."""
import pathlib
import markdown
from markdown.preprocessors import Preprocessor
import re


class RenderOnlyHeadings(Preprocessor):
    """Skip any line with that is NOT a heading."""
    def run(self, lines):
        new_lines = []
        for line in lines:
            m = re.search(r"^#+\s*\w+", line)
            if m:  # only lines that are headings are passed through
                new_lines.append(line)  
        return new_lines

# get all .md files in the current directory recursively
md_files = pathlib.Path.cwd().cwd().rglob('*.md')
# initialize the Markdown class
md = markdown.Markdown(extensions=['toc'])
md.preprocessors.register(RenderOnlyHeadings(md.parser), 'skip', 710)

for file_ in md_files:
    if str(file_).endswith('README.md') != True:
        with open(file_, 'r') as f:
            content = f.read()
            if not content.find('[TOC]') >= 0:
                print('...')
                continue
            html = md.convert(content)
            html_list = html.split('\n')
            # the listcomp below takes the HTML headings, e.g.:
            # <h3 id="installing-git-on-linux">Installing Git on Linux</h3>
            # and fetches only the content of each tags, then saves it in a list
            headings = [h.split('>')[-2].split('<')[0] for h in html_list]
            for i, h in enumerate(headings):
                p = r'#{3,4} ?' + h
                content = re.sub(p, html_list[i], content)
            # with open(pathlib.Path(file_.parent, f"{file_.name[:-2]}html"), "w", encoding="utf-8") as htmlfile:
            #     htmlfile.write(html)
            print(content)
        print(f"Created HTML with TOC for: {file_}")
