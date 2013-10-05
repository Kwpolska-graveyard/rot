# -*- encoding: utf-8 -*-
# River of Text v0.1.0
# INSERT TAGLINE HERE.
# Copyright © 2013, Kwpolska.
# See /LICENSE for licensing information.

"""
    rot.throbber
    ~~~~~~~~~~~~

    Throbbers, of various uses.

    :Copyright: © 2013, Kwpolska.
    :License: BSD (see /LICENSE).
"""

import sys
import time
import threading

__all__ = ['Throbber']


class Throbber(object):
    """A nice animated throbber.

    Usage::

        with Throbber(u'Doing important stuff...'):
            dostuff()
    """
    throb = False
    states = ('|', '/', '-', '\\')
    _tt = None

    def __init__(self, msg='Working...', finalthrob='+',
                 end_with_newline=True):
        """Initialize."""
        self.msg = msg
        self.finalthrob = finalthrob
        self.end_with_newline = end_with_newline

    def __enter__(self):
        """Run the throbber in a thread."""
        self._tt = threading.Thread(target=self._throb)
        self._tt.start()
        return self

    def __exit__(self, *args, **kwargs):
        """Clean stuff up."""
        self.throb = False
        while self.throbber_alive:
            time.sleep(0.1)

    def _throb(self):
        """Display a throbber."""
        self.throb = True
        i = 0
        while self.throb:
            sys.stdout.write(u'\r({0}) {1}'.format(self.states[i], self.msg))
            sys.stdout.flush()
            time.sleep(0.1)
            i += 1
            if i == len(self.states):
                i = 0
        if not self.throb and self.end_with_newline:
            sys.stdout.write(u'\r({0}) {1}'.format(self.finalthrob, self.msg))
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write(u'\n')
            sys.stdout.flush()

    @property
    def throbber_alive(self):
        """Check the status of a throbber."""
        if self._tt:
            return self._tt.is_alive()
        else:
            return False
