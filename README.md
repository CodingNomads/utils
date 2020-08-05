# Helper Scripts

This repository contains scripts to help keep our labs and repos organized, as well as help with content creation.

## `rename.py`

Renames lab files by changing their first double-digit to the double-digit of their containing folder. Takes away some of the headache of moving labs between sections.

**Possible result**:

```text
python_labs
|
├── 01_python_fundamentals
│   ├── 01_01_run_it.py
│   ├── 01_02_seconds_years.py
│   ├── 01_03_yeehaw.py
│   ├── 01_04_formula.py
│   ├── 01_05_addition.py
│   ├── 01_06_hello5.py
│   └── 01_07_area_perimeter.py

--- snip ---

└── 18_lambdas
    ├── 18_01_first_lambda.py
    ├── 18_02_return.py
    ├── 18_03_rewrite.py
    ├── 18_04_hello.py
    ├── 18_05_names.py
    └── 18_06_tuple_sort.py
```

## `replace_links.py`

Replaces all occurrences of Markdown links in `.md` files in the current folder with HTML links that open up in a new tab. If you create your content in a Markdown editor and you use normal MD links, run this script before adding your content to the platform.

E.g.:

```md
[Example](http://www.example.com)
```

turns into:

```html
<a href="http://www.example.com" target="_blank">Example</a>
```

The rest of your content remains unchanged.

## `add_toc.py`

This script allows you to add a clickable TOC to the top of your Markdown documents. It requires the external package called `md-toc`. You can install it via the included `Pipfile` or `requirements.txt`.

If you execute the script inside of the top-level folder of your course content, it will add a linked TOC to the top of each file that contains the following **HTML comment**:

```html
<!--TOC-->
```

It doesn't matter where it appears, but it needs to be part of your file for the script to pick it up, analyze the headings, and create the TOC.

**Note:** The HTML comment does _not_ get removed and the script does _not_ check whether a TOC already exists. If you run it multiple times you will get multiple TOC. Therefore, I suggest to run the script _once_ at the _end_ of your content creation workflow before adding the content to the course on the learning platform.
