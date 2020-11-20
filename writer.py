"""
This module contains concrete implementations of the Writer interface.
Simplest possible implementation would just print the command prompt and wrap printing into stdout.
"""

from traits import Writer

class SimpleWriter(Writer):
    def write(self, data: str):
        print(f'{data}\n\n')


class AsciiFormatter(Writer):
    def write(self, data: str):
        pass
