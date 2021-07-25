import codecs
import sys

PYTHON_VERSION_FILENAME = 'python-version.txt'

python_executable = sys.executable

# entry point `pyi-grab_version = PyInstaller.utils.cliutils.grab_version:run`

def run():
    try:
        import PyInstaller.utils.win32.versioninfo
        vs = PyInstaller.utils.win32.versioninfo.decode(python_executable)
        if not vs:
            raise SystemExit("Error: VersionInfo resource not found in exe")
        with codecs.open(PYTHON_VERSION_FILENAME, 'w', 'utf-8') as fp:
            fp.write(u"%s" % (vs,))
        print('Version info written to: %s' % PYTHON_VERSION_FILENAME)
    except KeyboardInterrupt:
        raise SystemExit("Aborted by user request.")

if __name__ == '__main__':
    run()
