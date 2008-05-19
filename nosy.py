#!/usr/bin/env python
"""Watch for changes in all source files. If changes, run nosetests. 

By Jeff Winkler, http://jeffwinkler.net

Command line and config file interfaces added by Doug Latornell,
http://douglatornell.ca
"""

import glob
import os
import stat
import time
from ConfigParser import SafeConfigParser, NoSectionError, NoOptionError
from optparse import OptionParser


class Nosy(object):
    """Watch for changes in all source files. If changes, run nosetests.
    """
    
    def __init__(self):
        """Return an instance with the default configuration, and a
        command line parser.
        """
        self.config = SafeConfigParser()
        self.config.add_section('nosy')
        self.config.set('nosy', 'paths', '*.py')
        self.config.set('nosy', 'options',  '')
        self.config.set('nosy', 'tests', '')
        self._build_cmdline_parser()


    def _build_cmdline_parser(self):
        description = 'Automatically run nose whenever source files change.'
        self._opt_parser = OptionParser(description=description)
        self._opt_parser.add_option('-c', '--config',
                                    action='store', dest='config_file',
                                    help='Configuration file path and name')


    def parse_cmdline(self):
        """Parse the command line and set the config_file attribute.
        """
        options, args = self._opt_parser.parse_args()
        if len(args) > 0:
            self._opt_parser.error('no arguments allowed')
        self.config_file = options.config_file


    def _read_config(self):
        if self.config_file:
            try:
                self.config.readfp(open(self.config_file, 'r'))
            except IOError, msg:
                self._opt_parser.error("can't read config file:\n %(msg)s"
                                       % locals())
        try:
            self.paths = self.config.get('nosy', 'paths').split()
            self.nose_opts = self.config.get('nosy', 'options')
            self.nose_args = self.config.get('nosy', 'tests')
        except NoSectionError:
            self._opt_parser.error("nosy section not found in config file")
            sys.exit(1)
        except NoOptionError:
            # Use default (s) from __init__()
            pass


    def _checksum(self):
        """Return a long which can be used to know if any files in the
        paths list have changed.
        """
        val = 0
        for path in self.paths:
            for f in glob.iglob(path):
                stats = os.stat(f)
                val += stats[stat.ST_SIZE] + stats[stat.ST_MTIME]
        return val


    def run(self):
        """Run nose whenever the source files (default ./*.py) change.

        Re-read the configuration before each nose run so that options
        and aruments may be changed.
        """
        val = 0
        self._read_config()
        while True:
            if self._checksum() != val:
                self._read_config()
                val = self._checksum()
                os.system('nosetests %(nose_opts)s %(nose_args)s'
                          % self.__dict__)
            time.sleep(1)


def main():
    nosy = Nosy()
    nosy.parse_cmdline()
    nosy.run()


if __name__ == '__main__':
    main()

# end of file
