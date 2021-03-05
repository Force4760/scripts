# Note-Me Vim Plugin

A plugin made for (Neo)Vim to help users use the note-me app.

## Install
There are various ways to install Vim plugins, but the way I reccomend is using Vim Plug.

To install this add this to your rc file:
```
Plug 
```

## How to use
This plugin offers a few functions:

### NoteCopySelection
It copies the first hour section (Started with **### hour:minutes**) bellow the current line
```
:NoteCopySelection
```

### NoteFormatNote
It formats the note, deleting exceding blank lines
```
:NoteFormatNote
```

### NoteToggleCB
This command is intended to help users with **checklists** and **To-Do's**
when this command is used:
    
- If the line has no **[]**:
    
    - **-[]** will be added to the beggining of the line

- If the line has **[]** (not checked):

    - The checkbox will be switched to **[x]**

- If the line has **[x]** (checked):

    - The checkbox will be switched to **[]** 
```
:NoteToggleCB
```

## Configure

### Change the characters considered as checked

default = ['x', 'X']

to change it add this to your rc file:

```vim
let g:notes_cb_checked = ['x', 'X']
```

### Configure KeyBoard Shortcuts
The plugin does not set default keyboard shortcuts.

For you to use them you can add a version of this lines to you rc file:
```vim
nnoremap <C-f> :NoteFormatNote<CR>
nnoremap <C-h> :NoteCopySelection<CR>
nnoremap <C-t> :NoteToggleCB<CR>
```
