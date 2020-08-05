"""Create a HTML file copy with a clickable TOC through rendering a given .md file."""
import pathlib
import markdown


# get all .md files in the current directory recursively
md_files = pathlib.Path.cwd().cwd().rglob('*.md')
# initialize the Markdown class
md = markdown.Markdown(extensions=['toc'])

for file_ in md_files:
    if str(file_).endswith('README.md') != True:
        with open(file_, 'r') as f:
            content = f.read()
            if not content.find('[TOC]') >= 0:
                print('...')
                continue
            html = md.convert(content)
            with open(pathlib.Path(file_.parent, f"{file_.name[:-2]}html"), "w", encoding="utf-8") as htmlfile:
                htmlfile.write(html)
        print(f"Created HTML with TOC for: {file_}")
