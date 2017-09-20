" ������ɫ
set hlsearch
set nu 
set t_Co=256
set so=0
set nowrap

" �Զ��� mapping
nmap <C-\>l mZ<c-l>'Zzt
nmap <F1> <esc>

" ͨ�� vim �鿴 man ������Ϣ
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


" �����ַ�������ֹ��������
set fileencodings=ucs-bom,utf-8,cp936,gb18030,big5,euc-jp,euc-kr,latin1
set fileencoding=cp936
set encoding=utf-8

" cscope ���������ͨ�� quickfix ������ʾ,����������ʾ�ڵ�ǰ����
set cscopequickfix=s-,c-,d-,i-,t-,e-
set switchbuf=useopen

" cscope ���Ҳ���ʾ�½��ָ��
set splitright

" ����ʱ����Сд����
set noignorecase

" ��ǰ��/�и���
set cursorcolumn
set cursorline
hi CursorColumn cterm=NONE ctermbg=black guibg=NONE guifg=NONE
hi CursorLine   cterm=NONE ctermbg=black guibg=NONE guifg=NONE


set tags+=./../tags,./../../tags,./../../../tags,./../../../../tags

"�����ͣ���Զ�����
hi CursorHightlight term=reverse cterm=reverse ctermfg=115 guifg=Black guibg=Yellow
autocmd CursorMoved * silent! exe printf('match CursorHightlight /\<%s\>/', expand('<cword>'))


let Tlist_Show_One_File           = 1  " ��ͬʱ��ʾ����ļ���tag��ֻ��ʾ��ǰ�ļ���
let Tlist_Exit_OnlyWindow         = 1  " ���taglist���������һ�����ڣ����˳�vim
let Tlist_GainFocus_On_ToggleOpen = 1  " ��������� List ����
