import platform

PYTHON_VERSION_FILENAME = 'python-version.txt'

python_version_tuple = platform.python_version_tuple()

# https://stackoverflow.com/questions/14624245/what-does-a-version-file-look-like
python_version_data = '''VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=({0}, {1}, {2}, 0),
    prodvers=({0}, {1}, {2}, 0)
    )
)
'''.format(*python_version_tuple)

with open(PYTHON_VERSION_FILENAME, 'w') as f:
    f.write(python_version_data)
