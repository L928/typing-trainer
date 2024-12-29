# Typing Trainer

This is a tool that helps learning ten finger typing. It aims to be efficient by addressing the individuality of each user. Personal weakness is addressed, and there is no proposal given on any learn method or schedule. It is up to the user to know how to learn things. Some important tipps on how to learn ten finger typing are given below, see *Tipps for learning typing*. It can (in theory) be used with any keyboard layout and any language.

## how to install and run

- python must be installed, see www.python.org
- some libraries, like pyqt5, must be installed
- clone the repo
- double click on the file `run.pyw` in the folder "src".

## How it works

A text is presented to type.
This can be an exercise text of any kind, for example

- a small beginner exercise to practice the 'f' and 'j' key only
- an advanced exercise to practice using the shift keys
- a text from a book

Press one of the top-buttons to load a text from a file, create a 
text for a specific exercise or randomly  create a text.

if a symbol is mistyped, the mistyped symbol as well as the missed one are
inserted into the text several times before and after the mistyped word,
to give extra practcing on the errors made.
There are certain intentional limitations, like space is not considered an error,
and the number of extra added symbols is limited, to not accientially
insert too much extra symbols.

## How to use it

The user must create and decide himself how to practive and what ecersices to do.
However, ther are some starting points:

- The user can load a text form a list of exercises, ordered by difficulty
- The use can load any text, or copy/paste one into the reference window
- The user can generate an ecercise with a wizard

There is no progress measure or statistics of any kind. Th user must
judge and decide how to learn.

The wrongly typed text is removed if additional symbols are added.

The correctly typed text is marked green in the reference, adn the
errors are marked red.

If red text exists, the user must delete the errors.

If everything is finished, it is up to the user what to do next.

# Tipps for learning typing

## don't look at the keyboard

We have a compulsion to look at the keyboard when we type.
Thet compulsion must be adressed. It prevents memorizing
the keys. Here are some tipps.

- Find the rest position for the finges without looking, by feeling 
  the little bumps on the `f` and `j` key. This is always the first to do 
  when starting typing.
- Practice many times setting all fingers on the rest position without
  looking at the keyboard. Take hands off, shake them, put back on rest
  position, repeat. Similar like when you learn an instrument like guitar.
- There are quality keyboards with keys that doesn't have symbols printed
  for learning. Maybe that's something for you, maybe not. I recommend
  trying a quality keyboard anyway. It is a pleasure to type on high quality
  keyboards.
- You may build a cotraption that blocks sight to your keyboard.
- For beginnig, to memorize the key positions, you may use a
  keyboard layout reference chart pinned above your monitor, and look
  at it instead of your keyboard. But you must eventually memorize the
  key positions and remove that chart.

## use a keyboard with keycaps that have convex surfaces

Don't use a laptop keyboard or any keyboard with flat surfaces.
The convex surface of quality keyboards help your fingers adjusting on 
the key position by feeling it's center and improve aiming precision.
This is important for developing the muscle memory for typing.

## move only one finger at a time

This is improtant, even though it feels difficult and unnatural.
It makes your fingers more flexible over time, like in stretching exercises.
Keep all fingers in the rest position while only moving the one finger
that types the letter. Then move that finger back. Repeat this like a
gym exercise several times and repeat regularly. Eventually you notice
your fingers become more agile.
Some motions might appear very difficult, like the "p" or the left
shift key or the numbers. Don't worry, just keep practicing *exactly*,
stretch the finger, have *discipline*.

## relax

Ensure you are relaxed all the time when you do the exercises.
Observe youself, if you feel physical or mental stress, sit back,
take a deep breath, think of something nice and relax all muscles
of the body. Or make a little break.

## practive slow, avoid mistakes

If you make mistakes, you learn making mistakes. 
Don't type too fast, practice *slowly*.
To learn to be fast, you must practice slowly.
You become fast automatically.

## practice daily

Better practice daily a little bit instead of a lot on one day and
then several days nothing. Your ability will get better from one day
to the next.

## learn your way

Find the right difficulty level for you. This is personal.
Some start with two letters, some with ten.
There are some things that are not equal for everyone.
For example, som people use the left finger for the b-key, some the right,
and some use both. There are even different keyboard finger porition charts
in the www. I personally practice the b and the 6 key with both index
fingers.

# develoopment

This is an early release which was tested a lot and is workable and very useful in the humble opinion of the developer. However, there are many things that could be added to it. For example: Providing settings, exercises for beginner to expert, look and feel, I22n, progress track, statistics, ai-generated text, a help system, graphical things like a keyboard chart, audible feedback, an automatic update system, and last but not least an installer and an executable that doesn't depend on python or install all dependencies automatically.

*This project originally started with the intend to explore the quality points of testing strategy (without a test framework) and documentation.*

## testing

### run unit tests

In the /src directory, run:

```
run_unit_test.py
```

This runs the `__test()` function in `app__test.py` and `functions.py`.

### run "hallway usability tests"

In the /src directory, run:

```
run_usability_tests.py
```

These tests are manual, and no test result is recorded.
Each test explains itself.

### run the application in test mode

In the /src directory, run:

```
run_gui_test.py
```

This rund the app in test mode, which makes it easier the test the
whole application.

### run the application and test it

- for debugging, run`run.py` in the `src` folder.
  This gives a console window with logs.
- for 'normal' mode, i.e. to behave as if it was shipped,
  doubleclick `run.py` in the `src` folder.
  This runs it without a console window.

### create documentation

- `doxpypy` must be on the path.
- run
  
  ```
  tools\doc_create\run.py
  ```
  
  and then open
  
  ```
  \generated\html\index.html
  ```
  
  in a browser.

## developing

- Ensure to maintain the testing, i.e. write tests.
- Follow the existing style and structure.

# license

This project is licensed under the terms of the MIT license.
See [LICENSE](LICENSE.md).


