# Python Utilities

Build useful standalone binary executable programs from Python standard library.

Name format of binary executable program is `"python-{module_path.replace('.', "-").replace('_', '-')}`.

They are the same as `python -m {module_path}`.

(module_path -> name of binary executable program)

* calendar -> python-calendar
* encodings.rot_13 -> python-encodings-rot-13
* gzip -> python-gzip
* http.server -> python-http-server
* json.tool -> python-json-tool
* platform -> python-platform
* smtpd -> python-smtpd
* tarfile -> python-tarfile
* tkinter.colorchooser -> python-tkinter-colorchooser
* uu -> python-uu
* webbrowser -> python-webbrowser
* zipfile -> python-zipfile

There are other modules but not for common use:

* ast
* asyncio
* cProfile
* code
* compileall
* imghdr
* inspect
* pdb
* pickle
* pickletools
* profile
* pstats
* py_compile
* pydoc
* timeit
* tokenize
* trace
* venv
* ...

And tools in Python's `Tool/scripts` directory.

And demos of turtle module.

...

## How to generate the utilities

Before building, install required tools:

```
pip install -r requirements.txt
```

First, generate Python version for the utilities:

```
python generate-version.py
```

Second, generate the utilities:

```
python generate-utilities.py
```

All generated utilities are under `dist` directory.
