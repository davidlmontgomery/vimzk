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
function! ZkNoteCreate(subdirectory, ...)
  " Construct filename
  let filename = join(a:000, '-')
  let filename = tolower(filename)

  " Get a new random zid
python << endOfPython
from vimzk.zid import create_zid
zid = create_zid()
vim.command('let zid = "%s"' % zid)
endOfPython

  " Use vimwiki to create the buffer
  let path = vimwiki#vars#get_wikilocal('path', g:vimzk_wiki_index) . a:subdirectory
  let ext = vimwiki#vars#get_wikilocal('ext', g:vimzk_wiki_index)
  let filename = filename . '.' . zid . ext
  call vimwiki#base#edit_file(':e', path . filename, '')

  " Enter new zettel template content
python << endOfPython
from vimzk.zettel import insert_zettel_template
zid = vim.eval('zid')
title_words = vim.eval('a:000')
insert_zettel_template(zid, title_words)
endOfPython
endfunction


" ZkComplete
"
" Extend vimwiki omni completion with zkext: filename completion for files under
" external base path (g:vimzk_ext_base).
"
" To enable this functionality, add the line
"
"   set omnifunc=ZkComplete
"
" in ~/.vim/after/ftplugin/vimwiki.vim.
function! ZkComplete(findstart, base)
  let result = Complete_wikifiles(a:findstart, a:base)
  if a:findstart == 1
    return result
  endif
  if a:base =~# '^zkext:'
    if !exists("g:vimzk_ext_base")
      echom "No external file directory set for zettelkasten (set g:vimzk_ext_base)."
      return []
    endif

" Obtain 'zkext:' link completions
python << endOfPython
from vimzk.fs_utils import zkext_completions
external_files_base = vim.eval('g:vimzk_ext_base')
completion_base = vim.eval('a:base')
link_completions = zkext_completions(external_files_base, completion_base)

# Problems were encountered with filenames that had non-ASCII characters
# when the python list was directly assigned to a vimscript variable.
# Constructing the vimscript list item by item, as below, avoids this problem.
vim.command("let link_completions = []")
for link in link_completions:
  vim.command("call add(link_completions, '%s')" % link)
endOfPython

    let result = result + link_completions
  endif
  return result
endfunction


" ZkExternalLinkHandler
"
" Open zettelkasten external files, linked relative to g:vimzk_ext_base.
"
" Hook up this link handling by including a VimwikiHandler in your vimrc,
" like this:
"
"   function! VimwikiLinkHandler(link)
"     return ZkExternalLinkHandler(a:link)
"   endfunction
"
" FIXME: Have vimzk install this automatically. The only tricky thing
" is preserving a user's existing handler. I should be able to check if
" they have such an handler defined, and if so, call it after my processing
" for cases where the link doesn't have the 'zkext:' scheme.
function! ZkExternalLinkHandler(link)
  if a:link =~# '^zkext:'
    let fname = a:link[6:]
    let full_path = g:vimzk_ext_base . fname
    call system('xdg-open ' . shellescape(full_path) . ' &')
    return 1
  endif
  return 0
endfunction


" --------------------------------
"  Expose commands to the user
" --------------------------------
command! ZkZidCreate call ZkZidCreate()
command! -nargs=+ ZkNoteCreate call ZkNoteCreate('', <f-args>)
command! -nargs=+ ZkSlipBoxCreate call ZkNoteCreate('slipbox/', <f-args>)

