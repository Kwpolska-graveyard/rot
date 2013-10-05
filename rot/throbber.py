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

from rot.progress import FrontProgressThrobber

__all__ = ['Throbber']


class Throbber(object):
    """A nice animated throbber.

    Usage::

        with Throbber('Doing important stuff...'):
            dostuff()
    """
    throb = False
    states = ('|', '/', '-', '\\')
    _tt = None

    def __init__(self, msg, finalthrob='*', printback=True):
        """Initialize."""
        self.msg = msg
        self.finalthrob = finalthrob
        self.printback = printback

    def __enter__(self):
        """Run the throbber in a thread."""
        self._tt = threading.Thread(target=self._throb, args=(
            self.msg, self.finalthrob, self.printback))
        self._tt.start()
        return self

    def __exit__(self, *args, **kwargs):
        """Clean stuff up."""
        self.throb = False
        while self.throbber_alive:
            time.sleep(0.1)

    def _throb(self, msg, finalthrob='*', printback=True):
        """Display a throbber."""
        self.throb = True
        i = 0
        while self.throb:
            sys.stdout.write('\r({0}) {1}'.format(self.states[i], self.msg))
            sys.stdout.flush()
            time.sleep(0.1)
            i += 1
            if i == len(self.states):
                i = 0
        if not self.throb and self.printback:
            sys.stdout.write('\r({0}) {1}'.format(self.finalthrob, self.msg))
            sys.stdout.flush()
            time.sleep(0.1)
            print()

    @property
    def throbber_alive(self):
        """Check the status of a throbber."""
        if self._tt:
            return self._tt.is_alive()
        else:
            return False
