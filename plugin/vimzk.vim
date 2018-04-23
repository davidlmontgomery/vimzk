" vim:tabstop=2:shiftwidth=2:expandtab


if exists("g:loaded_vimzk") || &cp
  finish
endif
let g:loaded_vimzk = 1

if !exists("g:vimwiki_list")
  echom "No registered vimwiki wikis found (set g:vimwiki_list)."
  finish
endif

if !exists("g:vimzk_wiki_index") || g:vimzk_wiki_index < 0 || g:vimzk_wiki_index > len(g:vimwiki_list)
  echom "Invalid wiki selected for zettelkasten (set g:vimzk_wiki_index)."
  finish
endif

" FIXME Following isn't right because it would only have
" the options set explicitly. I want to find where
" in vimwiki I can get the full set of options.
" Failing that, probably just use the index along with
" vimwiki property getting function.
" let g:vimzk_wiki = g:vimwiki_list[g:vimzk_wiki_index]
" echom string(g:vimzk_wiki)

" --------------------------------
" Add vimzk python code to PYTHONPATH
" --------------------------------
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))

" --------------------------------
"  Functions
" --------------------------------

" ZkZidCreate
"
" Print a new zid.
function! ZkZidCreate()
python << endOfPython
from vimzk.zid import create_zid
print(create_zid())
endOfPython
endfunction

" ZkNoteCreate
"
" Create a new zettel with template content.
function! ZkNoteCreate(...)
  " Construct filename and save title words.
  let title_words = []
  let filename = ''
  for arg in a:000
    call add(title_words, arg)
    let filename = filename . '-' . arg
  endfor
  let filename = tolower(filename)

  " Get a new random zid
python << endOfPython
from vimzk.zid import create_zid
zid = create_zid()
vim.command('let zid = "%s"' % zid)
endOfPython

  " Use vimwiki to create the buffer
  let path = vimwiki#vars#get_wikilocal('path', g:vimzk_wiki_index)
  let ext = vimwiki#vars#get_wikilocal('ext', g:vimzk_wiki_index)
  let filename = zid . filename . ext
  call vimwiki#base#edit_file(':e', path . filename, '')

  " Enter new zettel template content
python << endOfPython
from vimzk.zettel import insert_zettel_template
zid = vim.eval('zid')
title_words = vim.eval('title_words')
insert_zettel_template(zid, title_words)
endOfPython
endfunction

" --------------------------------
"  Expose commands to the user
" --------------------------------
command! ZkZidCreate call ZkZidCreate()
command! -nargs=* ZkNoteCreate call ZkNoteCreate(<f-args>)

