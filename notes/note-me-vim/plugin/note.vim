if !exists('g:notes_cb_checked')
  let g:notes_cb_checked = ['x', 'X']
endif


fun! NoteCopySection()
  execute '/### \d*:\d*\_[^#]*[^#]/'
  execute ':normal gn "+yy'
endfun

fun! NoteToggleCB()
  let line = getline(".")
  if (match(line, '\[.*\]')!=-1)
    if (match(line, '\[\s*\]') != -1)
      let line = substitute(line, '\[\s*\]', '[' . g:notes_cb_checked[0] . ']', '')
      call setline('.', line)
    else
      for symbol in g:notes_cb_checked
        if (match(line, '\['. symbol .'\]') != -1)
          let line = substitute(line, '\['. symbol .'\]', '[]', '')
          call setline('.', line)
          break
        endif
      endfor
    endif
  else
    let line = join(['    -[]', line], ' ')
    call setline('.', line)
    execute ":normal $"
  endif
endfun


fun! NoteFormatNote()
  execute ':%s/\n\{3,}/\r\r\r/e'
endfun

command! NoteFormatCB :call NoteFormatCB()
command! NoteCopySection :call NoteCopySection()
command! NoteFormatNote :call NoteFormatNote()
