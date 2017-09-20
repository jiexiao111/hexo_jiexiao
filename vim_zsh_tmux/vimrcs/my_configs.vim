" 设置配色
set hlsearch
set nu 
set t_Co=256
set so=0
set nowrap

" 自定义 mapping
nmap <C-\>l mZ<c-l>'Zzt
nmap <F1> <esc>

" 通过 vim 查看 man 帮助信息
source $VIMRUNTIME/ftplugin/man.vim
nmap K :Man <c-r><c-w><cr>
nmap K1 :Man 1 <c-r><c-w><cr>
nmap K2 :Man 2 <c-r><c-w><cr>
nmap K3 :Man 3 <c-r><c-w><cr>
nmap K4 :Man 4 <c-r><c-w><cr>
nmap K5 :Man 5 <c-r><c-w><cr>
nmap K6 :Man 6 <c-r><c-w><cr>
nmap K7 :Man 7 <c-r><c-w><cr>
nmap K8 :Man 8 <c-r><c-w><cr>
nmap K9 :Man 9 <c-r><c-w><cr>


" 设置字符集，防止中文乱码
set fileencodings=ucs-bom,utf-8,cp936,gb18030,big5,euc-jp,euc-kr,latin1
set fileencoding=cp936
set encoding=utf-8

" cscope 的搜索结果通过 quickfix 窗口显示,并将窗口显示在当前窗口
set cscopequickfix=s-,c-,d-,i-,t-,e-
set switchbuf=useopen

" cscope 在右侧显示新建分割窗口
set splitright

" 查找时，大小写敏感
set noignorecase

" 当前行/列高亮
set cursorcolumn
set cursorline
hi CursorColumn cterm=NONE ctermbg=black guibg=NONE guifg=NONE
hi CursorLine   cterm=NONE ctermbg=black guibg=NONE guifg=NONE


set tags+=./../tags,./../../tags,./../../../tags,./../../../../tags

"光标悬停处自动高亮
hi CursorHightlight term=reverse cterm=reverse ctermfg=115 guifg=Black guibg=Yellow
autocmd CursorMoved * silent! exe printf('match CursorHightlight /\<%s\>/', expand('<cword>'))


let Tlist_Show_One_File           = 1  " 不同时显示多个文件的tag，只显示当前文件的
let Tlist_Exit_OnlyWindow         = 1  " 如果taglist窗口是最后一个窗口，则退出vim
let Tlist_GainFocus_On_ToggleOpen = 1  " 焦点出现在 List 窗口
