# pyit - Python YAML Issue Tracker
**pyit** is a simple issue issue ticket system made in Python with the yaml library
to quickly add, track, and close issue tickets to better manage projects.

## Features
* Create new tickets
* List existing tickets
* Filter and sort lists to find specific types of tickets
* Show more specific info of specific tickets
* Close tickets

## Getting Started
### 1) Clone this repository
To get all the necessary files, run the following command:
```bash
git clone https://github.com/Zentiph/pyit
```
### 2) Install the necessary tools
If you don't have Python, make sure to install it. Any version above 3.10 should be fine.
Then, install all of the required Python packages by running this command in the directory you cloned into:
```bash
pip install -r requirements.txt
```
### 3) Using the tool
The file you want to run is `yamtik.py`. Running it with no arguments will print a simple usage message to help you get started:
```bash
python yamtik.py
```
For a full list of possible input options, use:
```bash
python yamtik.py -h
```
### 4) Accessing the tool from anywhere
If you want to be able to run this file from anywhere on your device, follow the steps corresponding to your OS below.
**Windows:**
1. Create a person bin folder (e.g. `C:\Users\<you>\bin`) and add it to your User PATH.
2. Create a `yamtik.cmd` file inside the bin directory you created in step 1.
3. Place the following inside the `yamtik.cmd` file:
```bash
@echo off
py "C:\path\to\pyit\yamtik.py" %*
```
where "C:\path\to\pyit\yamtik.py" is replaced by the full path to wherever you are storing `yamtik.py`.
4. Open a new terminal and run:
```bash
yamtik
```
If it prints output, it worked!
**Unix:**
1. Ensure `~bin` exists and is on your PATH (add `export PATH="$HOME/bin:$PATH"` to your shell rc).
2. Create a symlink:
```bash
ln -s /path/to/pyit/yamtik.py ~/bin/yamtik
chmod +x /path/to/pyit/yamtik.py
```
where "/path/to/pyit/yamtik.py" is replaced by the full path to wherever you are storing `yamtik.py`.
3. Open a new terminal and run:
```bash
yamtik
```
