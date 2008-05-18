"""
Watch for changes in all .py files. If changes, run nosetests. 

By Jeff Winkler, http://jeffwinkler.net

Command line and config file interfaces added by Doug Latornell,
http://douglatornell.ca
"""

import glob
import os
import stat
import time
from ConfigParser import SafeConfigParser


def checkSum(paths):
    """Return a long which can be used to know if any .py files have
    changed.
    """
    val = 0
    for path in paths:
        for f in glob.iglob(path):
            stats = os.stat(f)
            val += stats[stat.ST_SIZE] + stats[stat.ST_MTIME]
    return val


def main():
    config = SafeConfigParser()
    config.readfp(open('nosy.cfg'))
    paths = config.get('nosy', 'paths').split()
    val=0
    while (True):
        if checkSum(paths) != val:
            val = checkSum(paths)
            config.readfp(open('nosy.cfg'))
            nose_opts = config.get('nosy', 'options')
            nose_args = config.get('nosy', 'tests')
            os.system('nosetests %(nose_opts)s %(nose_args)s' % locals())
        time.sleep(1)


if __name__ == '__main__':
    main()

# end of file
