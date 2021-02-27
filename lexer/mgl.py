import re

from pygments.lexer import Lexer, RegexLexer, include, bygroups, using, \
this, combined, default, words
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
Number, Punctuation
from pygments.util import shebang_matches
from pygments import unistring as uni

class MGLLexer(RegexLexer):
"""
For `MGL <http://xtend-lang.org/>`_ source code.
.. versionadded:: 1.6
"""

name = 'MGL'
aliases = ['mgl']
filenames = ['*.mgl']
mimetypes = ['text/x-mgl']

flags = re.MULTILINE | re.DOTALL

tokens = {
	'root': [
	# method names
	(r'^(\s*(?:[a-zA-Z_][\w.\[\]]*\s+)+?)'  # return arguments
	r'([a-zA-Z_$][\w$]*)'                  # method name
	r'(\s*)(\()',                          # signature start
	bygroups(using(this), Name.Function, Text, Operator)),
	(r'[^\S\n]+', Text),
	(r'//.*?\n', Comment.Single),
	(r'/\*.*?\*/', Comment.Multiline),
	(r'@[a-zA-Z_][\w.]*', Name.Decorator),
	(r'(assert|break|case|catch|continue|default|do|else|finally|for|'
	r'if|goto|instanceof|new|return|switch|this|throw|try|while|IF|'
	r'ELSE|ELSEIF|ENDIF|FOR|ENDFOR|SEPARATOR|BEFORE|AFTER)\b',
	Keyword),
	(r'(def|abstract|const|enum|extends|final|implements|native|private|'
	r'protected|public|static|strictfp|super|synchronized|throws|'
	r'transient|volatile)\b', Keyword.Declaration),
	(r'(boolean|byte|char|double|float|int|long|short|void)\b',
	Keyword.Type),
	(r'(package)(\s+)', bygroups(Keyword.Namespace, Text)),
	(r'(true|false|null)\b', Keyword.Constant),
	(r'(class|interface)(\s+)', bygroups(Keyword.Declaration, Text),
	'class'),
	(r'(import)(\s+)', bygroups(Keyword.Namespace, Text), 'import'),
	(r"(''')", String, 'template'),
	(r'(\u00BB)', String, 'template'),
	(r'"(\\\\|\\[^\\]|[^"\\])*"', String.Double),
	(r"'(\\\\|\\[^\\]|[^'\\])*'", String.Single),
	(r'[a-zA-Z_]\w*:', Name.Label),
	(r'[a-zA-Z_$]\w*', Name),
	(r'[~^*!%&\[\](){}<>\|+=:;,./?-]', Operator),
	(r'[0-9][0-9]*\.[0-9]+([eE][0-9]+)?[fd]?', Number.Float),
	(r'0x[0-9a-fA-F]+', Number.Hex),
	(r'[0-9]+L?', Number.Integer),
	(r'\n', Text)
	],
	'class': [
	(r'[a-zA-Z_]\w*', Name.Class, '#pop')
	],
	'import': [
	(r'[\w.]+\*?', Name.Namespace, '#pop')
	],
	'template': [
	(r"'''", String, '#pop'),
	(r'\u00AB', String, '#pop'),
	(r'.', String)
	],
}