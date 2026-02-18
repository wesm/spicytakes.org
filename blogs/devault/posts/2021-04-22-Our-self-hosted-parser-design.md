---
title: "Parsers all the way down: writing a self-hosting parser"
date: 2021-04-22
url: https://drewdevault.com/2021/04/22/Our-self-hosted-parser-design.html
slug: Our-self-hosted-parser-design
word_count: 2973
---

One of the things we’re working on in  [my new programming language](https://drewdevault.com/2021/03/19/A-new-systems-language.html)  is a
self-hosting compiler. Having a self-hosted compiler is a critical step in the
development of (some) programming languages: it signals that the language is
mature enough to be comfortably used to implement itself. While this isn’t right
for some languages (e.g. shell scripts), for a systems programming language like
ours, this is a crucial step in our bootstrapping plan. Our self-hosted parser
design was completed this week, and today I’ll share some details about how it
works and how it came to be.

This is the third parser which has been implemented for this language. We wrote
a sacrificial compiler prototype upfront to help inform the language design, and
that first compiler used  [yacc](https://en.wikipedia.org/wiki/Yacc)  for its parser. Using yacc was helpful at
first because it makes it reasonably simple to iterate on the parser when the
language is still undergoing frequent and far-reaching design changes. Another
nice side-effect starting with a yacc parser is that it makes it quite easy to
produce a formal grammar when you settle on the design. Here’s a peek at some of
our original parser code:

```
struct_type
	: T_STRUCT '{' struct_fields '}' {
		$$.flags = 0;
		$$.storage = TYPE_STRUCT;
		allocfrom((void **)&$$.fields, &$3, sizeof($3));
	}
	| T_UNION '{' struct_fields '}' {
		$$.flags = 0;
		$$.storage = TYPE_UNION;
		allocfrom((void **)&$$.fields, &$3, sizeof($3));
	}
	;

struct_fields
	: struct_field
	| struct_field ',' { $$ = $1; }
	| struct_field ',' struct_fields {
		$$ = $1;
		allocfrom((void **)&$$.next, &$3, sizeof($3));
	}
	;

struct_field
	: T_IDENT ':' type {
		$$.name = $1;
		allocfrom((void**)&$$.type, &$3, sizeof($3));
		$$.next = NULL;
	}
	;
```

This approach has you writing code which is already almost a formal grammar in
its own right. If we strip out the C code, we get the following:

```
struct_type
	: T_STRUCT '{' struct_fields '}'
	| T_UNION '{' struct_fields '}'
	;

struct_fields
	: struct_field
	| struct_field ','
	| struct_field ',' struct_fields
	;

struct_field
	: T_IDENT ':' type
	;
```

This gives us a reasonably clean path to writing a formal grammar (and
specification) for the language, which is what we did next.

All of these samples describe a struct type. The following example shows what
this grammar looks like in real code — starting from the word “struct” and
including up to the “}” at the end.

```
type coordinates = struct {
    x: int,
    y: int,
    z: int,
};
```

In order to feed our parser tokens to work with, we also need a lexer, or a
 *lexical analyzer* . This turns a series of characters like “struct” into a
single token, like the T_STRUCT we used in the yacc code. Like the original
compiler used yacc as a parser generator, we also used  [lex](https://en.wikipedia.org/wiki/Lex_(software))  as a lexer
generator. It’s simply a list of regexes and the names of the tokens that match
those regexes, plus a little bit of extra code to do things like turning “1234”
into an int with a value of 1234. Our lexer also kept track of line and column
numbers as it consumed characters from input files.

```
"struct"	{ _lineno(); return T_STRUCT; }
"union"		{ _lineno(); return T_UNION; }
"{"		{ _lineno(); return '{'; }
"}"		{ _lineno(); return '}'; }

[a-zA-Z][a-zA-Z0-9_]* {
	_lineno();
	yylval.sval = strdup(yytext);
	return T_IDENTIFIER;
}
```

After we settled on the design with our prototype compiler, which was able to
compile some simple test programs to give us a feel for our language design, we
set it aside and wrote the specification, and, alongside it, a second compiler.
This new compiler was written in C — the language was not ready to
self-host yet — and uses a hand-written  [recursive descent](https://en.wikipedia.org/wiki/Recursive_descent_parser)  parser.

To simplify the parser, we deliberately designed a context-free LL(1) grammar,
which means it (a) can parse an input unambiguously without needing additional
context, and (b) only requires one token of look-ahead. This makes our parser
design a lot simpler, which was a deliberate goal of the language design. Our
hand-rolled lexer is  *slightly*  more complicated: it requires two characters of
lookahead to distinguish between the “.”, “..”, and “…” tokens.

I’ll skip going in depth on the design of the second parser, because the hosted
parser is more interesting, and a pretty similar design anyway. Let’s start by
taking a look at our hosted lexer. Our lexer is initialized with an input source
(e.g. a file) from which it can read a stream of characters. Then, each time we
need a token, we’ll ask it to read the next one out. It will read as many
characters as it needs to unambiguously identify the next token, then hand it up
to the caller.

Our specification provides some information to guide the lexer design:

> A token is the smallest unit of meaning in the **** grammar. The lexical analysis phase processes a UTF-8
> source file to produce a stream of tokens by matching the terminals with the
> input text. 
>  Tokens may be separated by *white-space* characters, which are defined as the
> Unicode code-points `U+0009` (horizontal tabulation), `U+000A` (line feed), and
> `U+0020` (space). Any number of whitespace characters may be inserted between
> tokens, either to disambiguate from subsequent tokens, or for aesthetic
> purposes. This whitespace is discarded during the lexical analysis phase. 
>  *Within a single token, white-space is meaningful. For example, the
> string-literal token is defined by two quotation marks **"** enclosing any
> number of literal characters. The enclosed characters are considered part of
> the string-literal token and any whitespace therein is not discarded.* 
>  The lexical analysis process consumes Unicode characters from the source file
> input until it is exhausted, performing the following steps in order: it shall
> consume and discard white-space characters until a non-white-space character
> is found, then consume the longest sequence of characters which could
> constitute a token, and emit it to the token stream.

There are a few different kinds of tokens our lexer is going to need to handle:
operators, like “+” and “-”; keywords, like “struct” and “return”; user-defined
identifiers, like variable names; and constants, like string and numeric
literals.

In short, given the following source code:

```
fn add2(x: int, y: int) int = x + y;
```

We need to return the following sequence of tokens:

```
fn      (keyword)
add2    (identifier)
(       (operator)
x
:
int
,
y
int
)
int
=
x
+
y
;
```

This way, our parser doesn’t have to deal with whitespace, or distinguishing
“int” (keyword) from “integer” (identifier), or handling invalid tokens like
“$”. To actually implement this behavior, we’ll start with an initialization
function which populates a state structure.

```
// Initializes a new lexer for the given input stream. The path is borrowed.
export fn init(in: *io::stream, path: str, flags: flags...) lexer = {
	return lexer {
		in = in,
		path = path,
		loc = (1, 1),
		un = void,
		rb = [void...],
	};
};

export type lexer = struct {
	in: *io::stream,
	path: str,
	loc: (uint, uint),
	rb: [2](rune | io::EOF | void),
};
```

This state structure holds, respectively:

* The input I/O stream
* The path to the current input file
* The current (line, column) number
* A buffer of un-read characters from the input, for lookahead

The main entry point for doing the actual lexing will look like this:

```
// Returns the next token from the lexer.
export fn lex(lex: *lexer) (token | error);

// A single lexical token, the value it represents, and its location in a file.
export type token = (ltok, value, location);

// A token value, used for tokens such as '1337' (an integer).
export type value = (str | rune | i64 | u64 | f64 | void);

// A location in a source file.
export type location = struct {
	path: str,
	line: uint,
	col: uint
};

// A lexical token class.
export type ltok = enum uint {
	UNDERSCORE,
	ABORT,
	ALLOC,
	APPEND,
	AS,
	// ... continued ...
	EOF,
};
```

The idea is that when the caller needs another token, they will call  `lex` , and
receive either a token or an error. The purpose of our lex function is to read
out the next character and decide what kind of tokens it might be the start of,
and dispatch to more specific lexing functions to handle each case.

```
export fn lex(lex: *lexer) (token | error) = {
	let loc = location { ... };
	let rn: rune = match (nextw(lex)?) {
		_: io::EOF => return (ltok::EOF, void, mkloc(lex)),
		rl: (rune, location) => {
			loc = rl.1;
			rl.0;
		},
	};

	if (is_name(rn, false)) {
		unget(lex, rn);
		return lex_name(lex, loc, true);
	};
	if (ascii::isdigit(rn)) {
		unget(lex, rn);
		return lex_literal(lex, loc);
	};

	let tok: ltok = switch (rn) {
		* => return syntaxerr(loc, "invalid character"),
		'"', '\'' => {
			unget(lex, rn);
			return lex_rn_str(lex, loc);
		},
		'.', '<', '>' => return lex3(lex, loc, rn),
		'^', '*', '%', '/', '+', '-', ':', '!', '&', '|', '=' => {
			return lex2(lex, loc, rn);
		},
		'~' => ltok::BNOT,
		',' => ltok::COMMA,
		'{' => ltok::LBRACE,
		'[' => ltok::LBRACKET,
		'(' => ltok::LPAREN,
		'}' => ltok::RBRACE,
		']' => ltok::RBRACKET,
		')' => ltok::RPAREN,
		';' => ltok::SEMICOLON,
		'?' => ltok::QUESTION,
	};
	return (tok, void, loc);
};
```

Aside from the EOF case, and simple single-character operators like “;”, both of
which this function handles itself, its role is to dispatch work to various
sub-lexers.

The sub-lexers handle more specific cases. The lex_name function handles things
which look like identifiers, including keywords; the lex_literal function
handles things which look like literals (e.g. “1234”); lex_rn_str handles rune
and string literals (e.g. “hello world” and ‘\n’); and lex2 and lex3
respectively handle two- and three-character operators like “&&” and “>>=”.

lex_name is the most complicated of these. Because the only thing which
distinguishes a keyword from an identifier is that the former matches a specific
list of strings, we start by reading a “name” into a buffer, then binary
searching against a list of known keywords to see if it matches something there.
To facilitate this, “bmap” is a pre-sorted array of keyword names.

```
const bmap: [_]str = [
	// Keep me alpha-sorted and consistent with the ltok enum.
	"_",
	"abort",
	"alloc",
	"append",
	"as",
	"assert",
	"bool",
	// ...
];

fn lex_name(lex: *lexer, loc: location, keyword: bool) (token | error) = {
	let buf = strio::dynamic();
	match (next(lex)) {
		r: rune => {
			assert(is_name(r, false));
			strio::appendrune(buf, r);
		},
		_: (io::EOF | io::error) => abort(), // Invariant
	};

	for (true) match (next(lex)?) {
		_: io::EOF => break,
		r: rune => {
			if (!is_name(r, true)) {
				unget(lex, r);
				break;
			};
			strio::appendrune(buf, r);
		},
	};

	let name = strio::finish(buf);
	if (!keyword) {
		return (ltok::NAME, name, loc);
	};

	return match (sort::search(bmap[..ltok::LAST_KEYWORD+1],
			size(str), &name, &namecmp)) {
		null => (ltok::NAME, name, loc),
		v: *void => {
			defer free(name);
			let tok = v: uintptr - &bmap[0]: uintptr;
			tok /= size(str): uintptr;
			(tok: ltok, void, loc);
		},
	};
};
```

The rest of the code is more of the same, but I’ve  [put it up here](https://paste.sr.ht/~sircmpwn/25871787b0d41db2b0af573ba1c93e1b6438b942)  if
you want to read it.

Let’s move on to parsing: we need to turn this one dimensional stream of tokens
into an structured form: the  *Abstract Syntax Tree* . Consider the following
sample code:

```
let x: int = add2(40, 2);
```

Our token stream looks like this:

```
let x : int = add2 ( 40 , 2 ) ;
```

But what we need is something more structured, like this:

```
binding
	name="x"
	type="int"
	initializer=call-expression
	=>	func="add2"
		parameters
			constant value="40"
			constant value="2"
```

We know at each step what kinds of tokens are valid in each situation. After we
see “let”, we know that we’re parsing a binding, so we look for a name (“x”)
and a colon token, a type for the variable, an equals sign, and an expression
which initializes it. To parse the initializer, we see an identifier, “add2”,
then an open parenthesis, so we know we’re in a call expression, and we can
start parsing arguments.

To make our parser code expressive, and to handle errors neatly, we’re going to
implement a few helper function that lets us describe these states in terms of
what the parser wants from the lexer. We have a few functions to accomplish
this:

```
// Requires the next token to have a matching ltok. Returns that token, or an error.
fn want(lexer: *lex::lexer, want: lex::ltok...) (lex::token | error) = {
	let tok = lex::lex(lexer)?;
	if (len(want) == 0) {
		return tok;
	};
	for (let i = 0z; i < len(want); i += 1) {
		if (tok.0 == want[i]) {
			return tok;
		};
	};

	let buf = strio::dynamic();
	defer io::close(buf);
	for (let i = 0z; i < len(want); i += 1) {
		fmt::fprintf(buf, "'{}'", lex::tokstr((want[i], void, mkloc(lexer))));
		if (i + 1 < len(want)) {
			fmt::fprint(buf, ", ");
		};
	};
	return syntaxerr(mkloc(lexer), "Unexpected '{}', was expecting {}",
		lex::tokstr(tok), strio::string(buf));
};

// Looks for a matching ltok from the lexer, and if not present, unlexes the
// token and returns void. If found, the token is consumed from the lexer and is
// returned.
fn try(
	lexer: *lex::lexer,
	want: lex::ltok...
) (lex::token | error | void) = {
	let tok = lex::lex(lexer)?;
	assert(len(want) > 0);
	for (let i = 0z; i < len(want); i += 1) {
		if (tok.0 == want[i]) {
			return tok;
		};
	};
	lex::unlex(lexer, tok);
};

// Looks for a matching ltok from the lexer, unlexes the token, and returns
// it; or void if it was not a ltok.
fn peek(
	lexer: *lex::lexer,
	want: lex::ltok...
) (lex::token | error | void) = {
	let tok = lex::lex(lexer)?;
	lex::unlex(lexer, tok);
	if (len(want) == 0) {
		return tok;
	};
	for (let i = 0z; i < len(want); i += 1) {
		if (tok.0 == want[i]) {
			return tok;
		};
	};
};
```

Let’s say we’re looking for a binding like our sample code to show up next. The
grammar from the spec is as follows:

And here’s the code that parses that:

```
fn binding(lexer: *lex::lexer) (ast::expr | error) = {
	const is_static: bool = try(lexer, ltok::STATIC)? is lex::token;
	const is_const = switch (want(lexer, ltok::LET, ltok::CONST)?.0) {
		ltok::LET => false,
		ltok::CONST => true,
	};

	let bindings: []ast::binding = [];
	for (true) {
		const name = want(lexer, ltok::NAME)?.1 as str;
		const btype: nullable *ast::_type =
			if (try(lexer, ltok::COLON)? is lex::token) {
				alloc(_type(lexer)?);
			} else null;
		want(lexer, ltok::EQUAL)?;
		const init = alloc(expression(lexer)?);
		append(bindings, ast::binding {
			name = name,
			_type = btype,
			init = init,
		});
		match (try(lexer, ltok::COMMA)?) {
			_: void => break,
			_: lex::token => void,
		};
	};

	return ast::binding_expr {
		is_static = is_static,
		is_const = is_const,
		bindings = bindings,
	};
};
```

Hopefully the flow of this code is fairly apparent. The goal is to fill in the
following AST structure:

```
// A single variable biding. For example:
//
// 	foo: int = bar
export type binding = struct {
	name: str,
	_type: nullable *_type,
	init: *expr,
};

// A variable binding expression. For example:
//
// 	let foo: int = bar, ...
export type binding_expr = struct {
	is_static: bool,
	is_const: bool,
	bindings: []binding,
};
```

The rest of the code is pretty similar, though some corners of the grammar are a
bit hairier than others. One example is how we parse infix operators for binary
arithmetic expressions (such as “2 + 2”):

```
fn binarithm(
	lexer: *lex::lexer,
	lvalue: (ast::expr | void),
	i: int,
) (ast::expr | error) = {
	// Precedence climbing parser
	// https://en.wikipedia.org/wiki/Operator-precedence_parser
	let lvalue = match (lvalue) {
		_: void => cast(lexer, void)?,
		expr: ast::expr => expr,
	};

	let tok = lex::lex(lexer)?;
	for (let j = precedence(tok); j >= i; j = precedence(tok)) {
		const op = binop_for_tok(tok);

		let rvalue = cast(lexer, void)?;
		tok = lex::lex(lexer)?;

		for (let k = precedence(tok); k > j; k = precedence(tok)) {
			lex::unlex(lexer, tok);
			rvalue = binarithm(lexer, rvalue, k)?;
			tok = lex::lex(lexer)?;
		};

		let expr = ast::binarithm_expr {
			op = op,
			lvalue = alloc(lvalue),
			rvalue = alloc(rvalue),
		};
		lvalue = expr;
	};

	lex::unlex(lexer, tok);
	return lvalue;
};

fn precedence(tok: lex::token) int = switch (tok.0) {
	ltok::LOR => 0,
	ltok::LXOR => 1,
	ltok::LAND => 2,
	ltok::LEQUAL, ltok::NEQUAL => 3,
	ltok::LESS, ltok::LESSEQ, ltok::GREATER, ltok::GREATEREQ => 4,
	ltok::BOR => 5,
	ltok::BXOR => 6,
	ltok::BAND => 7,
	ltok::LSHIFT, ltok::RSHIFT => 8,
	ltok::PLUS, ltok::MINUS => 9,
	ltok::TIMES, ltok::DIV, ltok::MODULO => 10,
	* => -1,
};
```

I don’t really grok this algorithm, to be honest, but hey, it works. Whenever I
write a precedence climbing parser, I’ll stare at the Wikipedia page for 15
minutes, quickly write a parser, and then immediately forget how it works. Maybe
I’ll write a blog post about it someday.

Anyway, ultimately, this code lives in our standard library and is used for
several things, including our (early in development) self-hosted compiler.
Here’s an example of its usage, taken from our documentation generator:

```
fn scan(path: str) (ast::subunit | error) = {
	const input = match (os::open(path)) {
		s: *io::stream => s,
		err: fs::error => fmt::fatal("Error reading {}: {}",
			path, fs::strerror(err)),
	};
	defer io::close(input);
	const lexer = lex::init(input, path, lex::flags::COMMENTS);
	return parse::subunit(&lexer)?;
};
```

Where the “ast::subunit” type is:

```
// A sub-unit, typically representing a single source file.
export type subunit = struct {
	imports: []import,
	decls: []decl,
};
```

Pretty straightforward! Having this as part of the standard library should make
it much easier for users to build language-aware tooling with the language
itself. We also plan on having our type checker in the stdlib as well. This is
something that I drew inspiration for from Golang — having a lot of their
toolchain components in the standard library makes it really easy to write
Go-aware tools.

So, there you have it: the next stage in the development of our language. I hope
you’re looking forward to it!
