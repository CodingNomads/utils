"""Adds a clickable TOC to the top of your Markdown documents."""
import pathlib
import md_toc


# get all .md files in the current directory recursively
md_files = pathlib.Path.cwd().rglob('*.md')

for file_ in md_files:
    with open(file_, 'r+') as f:
        content = f.read()
        # only add the TOC if specified for the file
        if content.find('<!--TOC-->') >= 0:  # .find() returns -1 if substring doesn't exist
            # the below settings keep two levels of headings for the TOC: h3 and h4
            #   h3 should be the main headings for a page on our platform
            toc = md_toc.build_toc(file_, keep_header_levels=4)
            # write to the beginning of the file
            f.seek(0, 0)
            f.write(f"{toc}{content}")
            if toc:
                print(f"Added TOC to: {file_}")
        else:
            print('...')
