" Vundle 默认配置关闭了自动识别文件类型
set nocompatible              
filetype off                 

" 插件安装路径
set rtp+=~/.vim/bundle/Vundle.vim

call vundle#begin()
" BEGIN 定义需要的插件

" 插件管理
Plugin 'VundleVim/Vundle.vim'
" vim 主题颜色
Plugin 'altercation/vim-colors-solarized'
" 文件查找
Plugin 'ctrlp.vim'
" 好看的状态栏
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
" 保存多个剪切项
Plugin 'YankRing.vim'
" 函数导航
Plugin 'Tagbar'
" 代码片段
Plugin 'SirVer/ultisnips'
Plugin 'honza/vim-snippets'
" 快速注释
Plugin 'commentary.vim'
" 目录导航
Plugin 'scrooloose/nerdtree'
" 快速对齐
Plugin 'junegunn/vim-easy-align'
" 动态编译补全及语法高亮
Plugin 'Valloric/YouCompleteMe'
" 快速查找
Plugin 'rking/ag.vim'
" 快速跳转
Plugin 'easymotion/vim-easymotion'
" 根据 cscopy/ctag 高亮显示代码
Plugin 'TagHighlight'
" C 标准库高亮
Plugin 'c-standard-functions-highlight'

" END 定义需要的插件
call vundle#end()            
filetype plugin indent on   

" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => CTRL-P
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let g:ctrlp_working_path_mode = 0
let g:ctrlp_map = '<c-f>'
map <leader>b         :CtrlPBuffer<cr>
map <leader>d         :CtrlPBookmarkDir<cr>
map <leader><leader>d :CtrlPDir<cr>
map <leader>t         :CtrlPBufTag<cr>
map <leader>tt        :CtrlPTag<cr>
map <leader><leader>t :CtrlPBufTagAll<cr>
map <leader>c         :CtrlPChange<cr>
map <leader>cc        :CtrlPChangeAll<cr>
map <leader><leader>m :CtrlPMRUFiles<cr>
map <leader>mm        :CtrlPMixed<cr>
map <leader>q         :CtrlPQuickfix<cr>
map <leader>l         :CtrlPLine<cr>
map <leader><leader>r :CtrlPRTS<cr>
map <leader>u         :CtrlPUndo<cr>
map <leader>ff        :CtrlPCurFile<cr>

let g:ctrlp_max_height = 20
let g:ctrlp_extensions = ['tag', 'buffertag', 'quickfix', 'dir', 'rtscript',
            \ 'undo', 'line', 'changes', 'mixed', 'bookmarkdir']
let g:ctrlp_custom_ignore = {
            \ 'dir':  '\.git$\|\.hg$\|\.svn$',
            \ 'file': '\.exe$\|\.so$\|\.dll$\|\.pyc$' }
let s:ctrlp_fallback = 'ag %s --nocolor -l -g ""'

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => vim-airline config (force color)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let g:airline_theme="luna"
let g:airline_powerline_fonts = 1

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Colorscheme
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
syntax enable
set background=dark
colorscheme solarized

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"" => Nerdtree
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
nmap <Leader>nn :NERDTreeToggle<CR>
let NERDTreeWinPos="right"

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"" => Tagbar
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
nmap <F9> :TagbarToggle<CR>
let g:tagbar_left = 1

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"" => Snippets
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let g:UltiSnipsExpandTrigger = '<C-j>'
let g:UltiSnipsJumpForwardTrigger = '<C-j>'
let g:UltiSnipsJumpBackwardTrigger = '<C-k>'
let g:snips_author = 'Jie Xiao <jiexiao111@gmail.com>'

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"" => TagHighlight
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
hi DefinedName ctermfg=61
hi GlobalVariable ctermfg=71
hi DefinedName ctermfg=6 guifg=#ffa0a0
hi EnumerationValue ctermfg=6 guifg=#ffa0a0
hi Member ctermfg=12 ctermbg=8
hi LocalVariable  ctermfg=12 ctermbg=8
function! UpdateTags()
    let curdir=getcwd()
    while !filereadable("./cscope.files")
        cd ..
        if getcwd() == "/"
            break
        endif
    endwhile
    if filewritable("./cscope.files")
        !cscope -bq 
        cs kill 0
        cs add cscope.out
        !ctags  --fields=+iaS --c-kinds=+xpl -L cscope.files
        "UpdateTypesFileOnly 
    endif
    execute ":cd " . curdir
endfunction
nmap <F5> :call UpdateTags() <CR>

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"" => ctags
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set tags+=./../tags,./../../tags,./../../../tags,./../../../../tags

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"" => scscope
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" cscope 的搜索结果通过 quickfix 窗口显示,并将窗口显示在当前窗口
set cscopequickfix=s-,c-,d-,i-,t-,e-
set switchbuf=useopen

" cscope 在右侧显示新建分割窗口
set splitright

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"" => man.vim
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
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

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"" => YouCompleteMe 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let g:acp_enableAtStartup = 0
set completeopt-=preview

" enable completion from tags
let g:ycm_collect_identifiers_from_tags_files = 1

" remap Ultisnips for compatibility for YCM
let g:UltiSnipsExpandTrigger = '<C-j>'
let g:UltiSnipsJumpForwardTrigger = '<C-j>'
let g:UltiSnipsJumpBackwardTrigger = '<C-k>'

"nnoremap <leader>gh :YcmCompleter GoToInclude<CR>
nnoremap <leader>gp :YcmCompleter GoToDeclaration<CR>
nnoremap <leader>gd :YcmCompleter GoToDefinition<CR>
nnoremap <leader>gg :YcmCompleter GoTo<CR>
nnoremap <leader>gr :YcmCompleter GoToReferences<CR>
"nnoremap <leader>gi :YcmCompleter GoToImprecise<CR>
"nnoremap <leader>jd :YcmCompleter ClearCompilationFlagCache<CR>
"nnoremap <leader>gt :YcmCompleter GetType<CR>
"nnoremap <leader>jd :YcmCompleter GetParent<CR>
"nnoremap <leader>jd :YcmCompleter FixIt<CR>
nnoremap <leader>gq :YcmCompleter GetDoc<CR>
"nnoremap <leader>jd :YcmCompleter StartServer<CR>
"nnoremap <leader>jd :YcmCompleter StopServer<CR>
"nnoremap <leader>jd :YcmCompleter RestartServer<CR>
"nnoremap <leader>jd :YcmCompleter ReloadSolution<CR>
"nnoremap <leader>jd :YcmCompleter GoToImplementation<CR>
"nnoremap <leader>jd :YcmCompleter GoToImplementationElseDeclaration<CR>

function! SWITCH_CHECK()
    if g:ycm_show_diagnostics_ui
        let g:ycm_show_diagnostics_ui = 0
    else
        let g:ycm_show_diagnostics_ui = 1
    endif
endfunction
nmap <F6> :call SWITCH_CHECK() <CR>

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"" => EasyAlign 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Start interactive EasyAlign in visual mode (e.g. vipga)
xmap ga <Plug>(EasyAlign)

" Start interactive EasyAlign for a motion/text object (e.g. gaip)
nmap ga <Plug>(EasyAlign)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"" => EasyMotion 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let g:EasyMotion_do_mapping = 0 " Disable default mappings

" Jump to anywhere you want with minimal keystrokes, with just one key binding.
" `s{char}{char}{label}`
" Need one more keystroke, but on average, it may be more comfortable.
nmap <Leader>s <Plug>(easymotion-overwin-f2)

" Turn on case insensitive feature
let g:EasyMotion_smartcase = 1

" JK motions: Line motions
map <Leader>j <Plug>(easymotion-j)
map <Leader>k <Plug>(easymotion-k)

" Gif config
" map  / <Plug>(easymotion-sn)
" omap / <Plug>(easymotion-tn)

" " These `n` & `N` mappings are options. You do not have to map `n` & `N` to EasyMotion.
" " Without these mappings, `n` & `N` works fine. (These mappings just provide
" " different highlight method and have some other features )
" map  n <Plug>(easymotion-next)
" map  N <Plug>(easymotion-prev)

" Move to line
map <Leader>L <Plug>(easymotion-bd-jk)
nmap <Leader>L <Plug>(easymotion-overwin-line)

" Move to word
map  <Leader>W <Plug>(easymotion-bd-w)
nmap <Leader>W <Plug>(easymotion-overwin-w)
