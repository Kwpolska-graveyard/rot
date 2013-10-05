# -*- encoding: utf-8 -*-
# River of Text v0.1.0
# INSERT TAGLINE HERE.
# Copyright © 2013, Kwpolska.
# See /LICENSE for licensing information.

"""
    rot.progress
    ~~~~~~~~~~~~

    Progress indicators.

    :Copyright: © 2013, Kwpolska.
    :License: BSD (see /LICENSE).
"""

import sys
import time
from rot import throbber

__all__ = ['FrontProgress', 'FrontProgressThrobber']


class FrontProgress(object):
    """A static progress indicator with numbers.

    Usage::

        fp = Progress(2, 'Doing step 1...')
        step1()
        fp.step('Doing step 2...')
        step2()
        fp.step()

    Or (with static message)::

        fp = Progress(2, 'Performing an action...')
        step1()
        fp.step()
        step2()
        fp.step()

    """
    current = -1
    total = 1
    _pml = 0

    def __init__(self, total, msg='Working...', end_with_newline=True):
        """Initialize a Progress message."""
        self.total = total
        self.msg = msg
        self.end_with_newline = end_with_newline
        self.step(msg)

    def step(self, msg=None, newline=False):
        """Print a progress message."""
        if msg is None:
            msg = self.msg
        else:
            self.msg = msg
        self.current += 1
        ln = len(str(self.total))
        sys.stdout.write('\r' + ((ln * 2 + 4 + self._pml) * ' '))
        self._pml = len(msg)
        sys.stdout.write('\r')
        sys.stdout.flush()
        sys.stdout.write(('({0:>' + str(ln) + '}/{1}) ').format(self.current,
                                                                self.total))
        sys.stdout.write(msg)
        sys.stdout.write('\r')
        sys.stdout.flush()
        if newline:
            print()
        if self.current == self.total:
            if self.end_with_newline:
                print()
            self.total = 0
            self.current = 0


class FrontProgressThrobber(FrontProgress, throbber.Throbber):
    """An animated progress throbber.

    Similar to Progress, but the / is animated.

    Usage::

        with ProgressThrobber(2, 'Doing stuff...') as pt:
            dostuff()
            pt.step('Cleaning up...')
            cleanup()
    """
    printback = True

    def __init__(self, total, msg='Working...', finalthrob='/', end_with_newline=True):
        self.total = total
        self.msg = msg
        self.finalthrob = finalthrob
        self.ln = len(str(self.total))
        self.step(msg)

    def _throb(self, msg, finalthrob='/', printback=True):
        """Display a throbber."""
        self.throb = True
        i = 0
        while self.throb:
            sys.stdout.write(('\r({0:>' + str(self.ln) +
                              '}{1}{2}) {3}').format(self.current,
                                                     self.states[i],
                                                     self.total, self.msg))
            sys.stdout.write('\r')
            sys.stdout.flush()
            time.sleep(0.1)
            i += 1
            if i == len(self.states):
                i = 0

        sys.stdout.write('\r({0}{1}{2}) {3}'.format(self.current,
                                                    self.finalthrob,
                                                    self.total, self.msg))
        sys.stdout.flush()
        time.sleep(0.1)
        if self.printback:
            print()

    def step(self, msg=None):
        if msg is None:
            msg = self.msg
        sys.stdout.write('\r' + ((self.ln * 2 + 4 + self._pml) * ' '))
        self._pml = len(msg)
        self.current += 1
        self.msg = msg
