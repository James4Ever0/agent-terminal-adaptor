<div align="center"><img src="https://github.com/james4ever0/agent-terminal-adaptor/blob/main/assets/logo.jpg?v=1&type=image" alt="TermAdaptor logo"></div>

<h1 align="center">TermAdaptor</h1>

<p align="center">
<a href="https://github.com/james4ever0/agent-terminal-adaptor/blob/master/LICENSE"><img alt="License: WTFPL" src="https://img.shields.io/badge/license-UNLICENSE-green.svg?style=flat"></a>
<a href="https://pypi.org/project/termadaptor/"><img alt="PyPI" src="https://img.shields.io/pypi/v/termadaptor"></a>
<a href="https://pepy.tech/project/termadaptor"><img alt="Downloads" src="https://static.pepy.tech/badge/termadaptor"></a>
<a href="https://github.com/james4ever0/agent-terminal-adaptor"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

## Demo

Built on top of [`tmux`](https://github.com/tmux/tmux) and many other libraries, Cybergod is capable of understanding and interacting terminal interface with both text-only and multimodal modes. With the help of [`wcwidth`](https://github.com/jquast/wcwidth), cursor is placed precisely at the right position even if there are multi-width unicode chars (CJK characters for example).

Code can be found [here](tmux_trials/lib.py).

To interact with the environment programmatically, check out [here](tmux_trials/test_lib.py)

```python
# env: TmuxEnvironment
env.send_key("vim")
env.send_key("Enter")
```

Terminal parsing (colorless):

![Cybergod demo](propaganda/tmux_show_0.gif)

Terminal parsing (colorful):

![Cybergod demo](propaganda/tmux_show_1.gif)

Terminal screenshot converted from HTML (cursor in red):

![Vim screenshot](propaganda/vim_edit_tmux_screenshot.png)

Terminal with dark theme and grayscale effects except for the cursor:

![Cursor highlight](propaganda/grayscale_dark_tmux.png)

You can also have a block-styled cursor:

![Block cursor](propaganda/block_cursor_terminal_screenshot.png)

Change the cursor character to underline:

![Underline cursor char](propaganda/custom_cursor_char.png)

Override the cursor block style:

![Custom block style](propaganda/custom_block_style.png)

## Usage

### Terminal environment integration

First, install required binaries:

```bash
sudo apt install -y tmux tmuxp aha
```

Next, install the following dependencies:

```bash
pip install parse playwright beautifulsoup4

# setup playwright if you want to take terminal screenshots
playwright install chromium
```

Finally copy the [`lib.py`](https://github.com/James4Ever0/agi_computer_control/blob/master/tmux_trials/lib.py), then run [`test_lib.py`](https://github.com/James4Ever0/agi_computer_control/blob/master/tmux_trials/test_lib.py) next to the `lib.py`. 

The `SESSION_COMMAND` in `test_lib.py` is the initial terminal environment command to be executed. Change it according to your need.

To view the environment:

```python
preview = session.preview_html(show_cursor=True,wrap_html=True, dark_mode=True, grayscale=True)
```

To interact with the environment:

```python
# note that both special key and literal strings can be sent.
env.send_key("date")
env.send_key("Enter") # special key
```

A full mapping from conventional special keys to standard Tmux special keys can be generated by running [`generate_funckey_alias.py`](https://github.com/James4Ever0/agi_computer_control/blob/master/tmux_trials/generate_funckeys_alias.py)

You can read the test file for further integration.

## Star History

<img src="https://api.star-history.com/svg?repos=james4ever0/agent-terminal-adaptor&Timeline" style="filter: invert(100%);"></img>
