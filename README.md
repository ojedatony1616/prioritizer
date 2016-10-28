# Prioritizer

Simple, but useful command line app that helps you determine what's most important from a list of things you enter.

## Suggested Installation

To utilize this tool on a regular basis, install it to your `$PATH`. You can do this by copying `prioritizer.py` to one of the locations in your path, e.g. `/usr/local/bin` or by creating a `bin` directory in your home directory, and adding it to your path (preferred). If you don't already have a `~/bin` directory, create one with `mkdir ~/bin` then edit your `.profile` or `.bash_profile` in your home directory, adding the following if it doesn't already exist:

```
export PATH=$HOME/bin:$PATH
```

You then must source your profile: `source ~/.profile` in order to make sure the `$PATH` gets updated appropriately. Then assuming you're in the root directory of the repository:

```
$ cp prioritizer.py ~/bin/prioritize
$ chmod +x ~/bin/prioritizer.py
```

You should now be able to utilize the priorities from the command line:

```
$ prioritize
Enter item to prioritize (leave blank when done):
```
