Simple console drawing program

### Prerequisites

Python 3.8 is required in order to run the program. Follow your OS specific instructions to install Python 3.8 on your machine or in a virtual environment.

### Depenencies
Once Python has been installed, get the required dependencies:
Assuming the repo has been cloned or extracted to the `console-drawing` folder in your current working directory, do the following:

```bash
# install dependencies
$ cd console-drawing 
$ pip install -r requirements.txt
```

Now you are all set to run start drawing in the terminal console.

### Running the program

From the program folder `console-drawing` run
```bash
$ python main.py
```

The command prompt will appear suggesting to enter commands. Currently supported set of commands includes:
```bash
Command         Description
C w h           Should create a new canvas of width w and height h.
L x1 y1 x2 y2   Should create a new line from (x1,y1) to (x2,y2). Currently only
                horizontal or vertical lines are supported. Horizontal and vertical lines
                will be drawn using the 'x' character.
R x1 y1 x2 y2   Should create a new rectangle, whose upper left corner is (x1,y1) and
                lower right corner is (x2,y2). Horizontal and vertical lines will be drawn
                using the 'x' character.
B x y c         Should fill the entire area connected to (x,y) with "colour" c. The
                behavior of this is the same as that of the "bucket fill" tool in paint
                programs.
Q               Should quit the program.
```

The commands are case insensitive.

### Running test

Navigate to the program folder and run
```bash
$ python -m unittest
```
