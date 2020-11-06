"""Prepares a simple Markdown doc for publishing on the CN Blog site."""
import argparse
from pathlib import Path
import re

import markdown
from markdown.preprocessors import Preprocessor
import md_toc


# Create the parser
my_parser = argparse.ArgumentParser(description='Prepare a pure Markdown article for blog publishing.')
# Add the arguments
my_parser.add_argument('File',
                       metavar='file',
                       type=str,
                       help='the path to the file to be prepared')
my_parser.add_argument('-toc',
                       action='store_true',
                       help='whether to create a clickable TOC at the top')
my_parser.add_argument('-p',
                       action='store_true',
                       help='if the Markdown is copied from a CN Learning Platform Resource')
# Execute the parse_args() method
args = my_parser.parse_args()

input_path = Path(args.File)
add_toc = args.toc
is_platform = args.p

if not input_path.is_file():
    print('The file specified does not exist')
    sys.exit()


new_tab_link_pattern = re.compile(r'(?<!!)(\[([^\s\]]*)\]\(([^\s\)]*)\))')
"""
the regex matches all Markdown links of the form following form:
    [Example](http://www.example.com)
and replaces them with new-tab HTML links, e.g.:
    <a href="http://www.example.com" target="_blank">Example</a>

NOTE: it does **NOT** match Markdown image links, e.g.
    ![Example](imgs/example.jpg)
which is intentional and expected behavior
"""

def update_links(matchobj):
    """Creates a HTML link that opens in a new tab from an appropriate re.match() object."""
    text = matchobj.group(1)
    url = matchobj.group(2)
    return f'<a href="{url}" target="_blank">{text}</a>'


if add_toc:
    class RenderOnlyHeadings(Preprocessor):
        """Skip any line with that is NOT a heading."""
        def run(self, lines):
            new_lines = []
            for line in lines:
                m = re.search(r"^#+\s*\w+", line)
                if m:  # only lines that are headings are passed through
                    new_lines.append(line)  
            return new_lines
    # initialize the Markdown class
    md = markdown.Markdown(extensions=['toc'])
    md.preprocessors.register(RenderOnlyHeadings(md.parser), 'skip', 710)


with open(input_path, 'r+') as fin:
    content = fin.read()

    # Replaces all Markdown-style links with HTML new-tab links
    content = re.sub(new_tab_link_pattern, update_links, content)
    print(f'{input_path.name}: Replaced Links')

    if is_platform:
        # take out bootstrap-specific formatting of information boxes
        # and replace with making them blockquotes, which render nicely on our blog
        content = re.sub(r"<div\sclass='alert+\s+\w+-\w+'\srole='alert'>\n\s+(<strong>\w+:<\/strong>\s)?", ">", content)
        content = re.sub(r"<\/div>\n", "", content)
        # upscale the levels of the headings by one (title will remain only 1st-level heading)
        content = re.sub(r"###\s+", "## ", content)
        content = re.sub(r"####\s+", "### ", content)
        print(f'{input_path.name}: Substituted Learning-Platform specific syntax')

    if add_toc:  # only add the TOC if specified for the file

        # first, get the HTML-converted links with page-stub ids
        converted_headings = md.convert(content)
        section_links = converted_headings.split('\n')
        # breakpoint()

        if converted_headings:
            # now build the clickable Markdown TOC
            # the below settings keep two levels of headings for the TOC: h2 and h3
            toc = md_toc.build_toc(input_path, keep_header_levels=3)
            # write to the beginning of the file
            content = f"{toc}\n{content}"
            if toc:
                print(f"{input_path.name}: Added TOC")
            
            # the listcomp below takes the HTML headings, e.g.:
            # <h3 id="installing-git-on-linux">Installing Git on Linux</h3>
            # and fetches only the content of each tags, then saves it in a list
            headings = [h.split('>')[-2].split('<')[0] for h in section_links]
            for i, h in enumerate(headings):
                p = r'#{2,3}[ \w]' + h
                content = re.sub(p, section_links[i], content)
            else:
                print(f'{input_path.name}: TOC is now clickable')

    # reset the file and write the changed content
    fin.seek(0)
    fin.truncate(0)
    fin.write(content)


if __name__ == '__main__':
    args = my_parser.parse_args()
    print(f"----- finished processing file ----")
