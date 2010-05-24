#!/usr/bin/env python
#
# Usage:
#   ./autocompile.py path extn cmd
#
# Blocks monitoring |path| and its subdirectories for modifications on
# files ending with suffix |extk|. Run |cmd| each time a modification
# is detected. |cmd| is optional and defaults to 'make'.
#
# Example:
#   ./autocompile.py /my-latex-document-dir .tex "make pdf"
#
# Dependancies:
#   Linux, Python 2.x, Pyinotify
#
import sys
import pyinotify

import commands, re

def checkResult(command_output, regex, doc_type):
    result_value = True
    search_result = re.search(regex, command_output)
    if search_result and search_result.group(0):
        print 'SUCCESS: %s built okay.' % doc_type
    else:
        print 'FAIL: %s build not okay.' % doc_type
        result_value = False
    return result_value


class OnWriteHandler(pyinotify.ProcessEvent):
    def my_init(self, cwd, extension, cmd):
        self.cwd = cwd
        self.extensions = extension.split(',')
        self.cmd = cmd

    def _run_cmd(self):
        print '==> Modification detected'
        result = commands.getoutput(self.cmd)
        html_result = checkResult(result, 'The HTML pages are in (.*)\.', 'HTML')
        latex_result = checkResult(result, 'Output written on (.*)\.pdf', 'LaTeX')
        if html_result and latex_result:
            print 'OKAY: Waiting now until next ReST modification'
        else:
            print 'BUILD FAILED: Traceback in-bound...'
            print result

    def process_IN_MODIFY(self, event):
        for ext in self.extensions:
            if not event.pathname.endswith(ext): return
        self._run_cmd()

def auto_compile(path, extension, cmd):
    wm = pyinotify.WatchManager()
    handler = OnWriteHandler(cwd=path, extension=extension, cmd=cmd)
    notifier = pyinotify.Notifier(wm, default_proc_fun=handler)
    wm.add_watch(path, pyinotify.ALL_EVENTS, rec=True, auto_add=True)
    print '==> Start monitoring %s (type c^c to exit)' % path
    notifier.loop()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print >> sys.stderr, "Command line error: missing argument(s)."
        sys.exit(1)

    # Required arguments
    path = sys.argv[1]
    extension = sys.argv[2]

    # Optional argument
    cmd = 'make'
    if len(sys.argv) == 4:
        cmd = sys.argv[3]

    # Blocks monitoring
    auto_compile(path, extension, cmd)

