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
" Add our plugin to the path
" --------------------------------
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))

" --------------------------------
"  Function(s)
" --------------------------------
function! CreateZid()
python << endOfPython

from vimzk.zid import create_zid
print(create_zid())

endOfPython
endfunction

" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! Zid call CreateZid()
