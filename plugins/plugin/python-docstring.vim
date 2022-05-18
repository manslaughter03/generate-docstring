let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

python3 << EOF
import sys
from os.path import normpath, join
import vim
try:
    from docstring import parse
except ModuleNotFoundError:
   print("Can't find docstring module")
   print("Please install with: pip install docstring")

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
	_, res = parse("\n".join(vim.current.buffer), vim.current.buffer.name)
	set_buffer_content(vim.current.buffer, res.code)
EOF

function! GenerateDocString()
  python3 generate_docstring()
endfunction

command! -nargs=0 GenerateDocString call GenerateDocString()
