let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

python3 << EOF
import sys
from os.path import normpath, join
import vim
from docstring import parse

def set_buffer_content(buf, text):
    buf[:] = None
    first = True
    for l in text.split('\n'):
        if first:
            buf[0] = l
            first = False
        else:
            buf.append(l)

def generate_docstring():
#current_line = vim.current.buffer[row-1]
#row, col = vim.current.window.cursor
	res = parse("\n".join(vim.current.buffer), vim.current.buffer.name)
	set_buffer_content(vim.current.buffer, res)
EOF

function! GenerateDocString()
  python3 generate_docstring()
endfunction

command! -nargs=0 GenerateDocString call GenerateDocString()
