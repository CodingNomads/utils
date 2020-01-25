# Helper Scripts

This repository contains scripts to help keep our labs and repos organized, as well as help with content creation.

## `rename.py`

Renames lab files by cahnging their first double-digit to the double-digit of their containing folder. Takes away some of the headache of moving labs between sections.

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

Replaces all occurences of Markdown links in `.md` files in the current folder with HTML links that open up in a new tab. If you create your content in a Markdown editor and you use normal MD links, run this script before adding your content to the platform.

E.g.:

```md
[Example](http://www.example.com)
```

turns into:

```html
<a href="http://www.example.com" target="_blank">Example</a>
```

The rest of your content remains unchanged.
