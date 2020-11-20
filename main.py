import sys
import asyncio
from traits import Canvas, Writer, CommandExecutor
from primitives import Command
from canvas import MemoryLessCanvas as CanvasClass
from command_executor import SyncCommandExecutor as ExecutorClass
from writer import SimpleWriter as WriterClass

class App:
    """Text drawing application
        The state of the application is the 'canvas' field

        The main loop reads a user's input from the command line and does a simple
        stateless validation of the entered command to make sure it conforms with the syntax.

        After that the call is dispatched to the [asynchronous] command handler for processing and state update.

        The updated state is printed to the console.
        """

    def __init__(self, canvas: Canvas, executor: CommandExecutor, writer: Writer):
        self.canvas = canvas
        self.executor = executor
        self.writer = writer

    def parse_command(self) -> Command:
        r = input('enter command: ').split()
        if len(r) == 0:
            return Command(Command.Keyword.UNKNOWN)
        if r[0] == 'C' or r[0] == 'c':
            return Command(Command.Keyword.CREATE, *r[1:])
        if r[0] == 'L' or r[0] == 'l':
            return Command(Command.Keyword.LINE, *r[1:])
        if r[0] == 'R' or r[0] == 'r':
            return Command(Command.Keyword.RECT, *r[1:])
        if r[0] == 'B' or r[0] == 'b':
            return Command(Command.Keyword.FILL, *r[1:])
        if r[0] == 'Q' or r[0] == 'q':
            return Command(Command.Keyword.QUIT)
        return Command(Command.Keyword.UNKNOWN)

    async def start(self):
        """Starts the main command loop"""
        while True:
            cmd = self.parse_command()
            if cmd.keyword == Command.Keyword.UNKNOWN:
                print('Unknown command, please repeat')
                continue
            if cmd.keyword == Command.Keyword.QUIT:
                break
            try:
                self.executor.execute(self.canvas, cmd)
            except (TypeError, ValueError) as e:
                print(f'{e}\n')
                continue
            self.writer.write(self.canvas.to_string())


if __name__ == '__main__':
    app = App(CanvasClass(), ExecutorClass(), WriterClass())
    asyncio.run(app.start())
