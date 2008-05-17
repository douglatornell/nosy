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


def checkSum():
    """Return a long which can be used to know if any .py files have changed.
    Only looks in the current directory.
    """
    val = 0
    for f in glob.glob('*.py'):
        stats = os.stat(f)
        val += stats[stat.ST_SIZE] + stats[stat.ST_MTIME]
    for f in glob.glob('tests/*.py'):
        stats = os.stat (f)
        val += stats[stat.ST_SIZE] + stats[stat.ST_MTIME]
    return val


val=0
config = SafeConfigParser()
while (True):
    if checkSum() != val:
        val = checkSum()
        config.readfp(open('nosy.cfg'))
        options = config.get('nosy', 'options')
        tests = config.get('nosy', 'tests')
        os.system('nosetests %(options)s %(tests)s' % locals())
    time.sleep(1)

# end of file
