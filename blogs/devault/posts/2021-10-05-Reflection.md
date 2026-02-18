---
title: "How reflection works in ****"
date: 2021-10-05
url: https://drewdevault.com/2021/10/05/Reflection.html
slug: Reflection
word_count: 1730
---

*Note: this is a redacted copy of a blog post published on the internal
development blog of a new systems programming language. The name of the project
and further details are deliberately being kept in confidence until the initial
release. You may be able to find it if you look hard enough — you have my
thanks in advance for keeping it to yourself. For more information, see “[We are
building a new systems programming language](https://drewdevault.com/2021/03/19/A-new-systems-language.html)”.*

I’ve just merged support for reflection in  xxxx .
Here’s how it works!

## Background

“Reflection” refers to the ability for a program to examine the type system of
its programming language, and to dynamically manipulate types and their values
at runtime. You can learn more at  [Wikipedia](https://en.wikipedia.org/wiki/Reflective_programming) .

## Reflection from a user perspective

Let’s start with a small sample program:

```
use fmt;
use types;

export fn main() void = {
    const my_type: type = type(int);
    const typeinfo: *types::typeinfo = types::reflect(my_type);
    fmt::printfln("int\nid: {}\nsize: {}\nalignment: {}",
        typeinfo.id, typeinfo.sz, typeinfo.al)!;
};
```

Running this program produces the following output:

```
int
id: 1099590421
size: 4
alignment: 4
```

This gives us a simple starting point to look at. We can see that “type” is used
as the type of the “my_type” variable, and initialized with a “type(int)”
expression. This expression returns a type value for the type given in the
parenthesis — in this case, for the “int” type.

To learn anything useful, we have to convert this to a “types::typeinfo”
pointer, which we do via  `types::reflect` . The typeinfo structure looks like
this:

```
type typeinfo = struct {
	id: uint,
	sz: size,
	al: size,
	flags: flags,
	repr: repr,
};
```

The ID field is the type’s unique identifier, which is universally unique and
deterministic, and forms part of  xxxx ’s ABI. This
is derived from an FNV-32 hash of the type information. You can find the ID for
any type by modifying our little example program, or you can use the helper
program in the  `cmd/xxxxtype`  directory
of the  xxxx  source tree.

Another important field is the “repr” field, which is short for
“representation”, and it gives details about the inner structure of the type.
The repr type is defined as a tagged union of all possible type representations
in the  xxxx  type system:

```
type repr = (alias | array | builtin | enumerated | func | pointer | slice | struct_union | tagged | tuple);
```

In the case of the “int” type, the representation is “builtin”:

```
type builtin = enum uint {
  BOOL, CHAR, F32, F64, I16, I32, I64, I8, INT, NULL, RUNE, SIZE, STR, U16, U32,
  U64, U8, UINT, UINTPTR, VOID, TYPE,
};
```

`builtin::INT` , in this case. The structure and representation of the “int” type
is defined by the  xxxx  specification and cannot be
overridden by the program, so no further information is necessary. The relevant
part of the spec is:

More information is provided for more complex types, such as structs.

```
use fmt;
use types;

export fn main() void = {
	const my_type: type = type(struct {
		x: int,
		y: int,
	});
	const typeinfo: *types::typeinfo = types::reflect(my_type);
	fmt::printfln("id: {}\nsize: {}\nalignment: {}",
		typeinfo.id, typeinfo.sz, typeinfo.al)!;
	const st = typeinfo.repr as types::struct_union;
	assert(st.kind == types::struct_kind::STRUCT);
	for (let i = 0z; i < len(st.fields); i += 1) {
		const field = st.fields[i];
		assert(field.type_ == type(int));
		fmt::printfln("\t{}: offset {}", field.name, field.offs)!;
	};
};
```

The output of this program is:

```
id: 2617358403
size: 8
alignment: 4
	x: offset 0
	y: offset 4
```

Here the “repr” field provides the “types::struct_union” structure:

```
type struct_union = struct {
	kind: struct_kind,
	fields: []struct_field,
};

type struct_kind = enum {
	STRUCT,
	UNION,
};

type struct_field = struct {
	name: str,
	offs: size,
	type_: type,
};
```

Makes sense? Excellent. So how does it all work?

## Reflection internals

Let me first draw the curtain back from the magic “types::reflect” function:

```
// Returns [[typeinfo]] for the provided type.
export fn reflect(in: type) const *typeinfo = in: *typeinfo;
```

It simply casts the “type” value to a pointer, which is what it is. When the
compiler sees an expression like  `let x = type(int)` , it statically allocates
the typeinfo data structure into the program and returns a pointer to it, which
is then wrapped up in the opaque “type” meta-type. The “reflect” function simply
converts it to a useful pointer. Here’s the generated IR for this:

```
%binding.4 =l alloc8 8
storel $rt.builtin_int, %binding.4
```

A clever eye will note that we initialize the value to a pointer to
“rt.builtin_int”, rather than allocating a typeinfo structure here and now. The
runtime module provides static typeinfos for all built-in types, which look like
this:

```
export const @hidden builtin_int: types::typeinfo = types::typeinfo {
	id = 1099590421,
	sz = 4, al = 4, flags = 0,
	repr = types::builtin::INT,
};
```

These are an internal implementation detail, hence “@hidden”. But many types are
not built-in, so the compiler is required to statically allocate a typeinfo
structure:

```
export fn main() void = {
	let x = type(struct { x: int, y: int });
};
```

```
data $strdata.7 = section ".data.strdata.7" { b "x" }

data $strdata.8 = section ".data.strdata.8" { b "y" }

data $sldata.6 = section ".data.sldata.6" {
  l $strdata.7, l 1, l 1, l 0, l $rt.builtin_int,
  l $strdata.8, l 1, l 1, l 4, l $rt.builtin_int,
}

data $typeinfo.5 = section ".data.typeinfo.5" {
  w 2617358403, z 4,
  l 8,
  l 4,
  w 0, z 4,
  w 5555256, z 4,
  w 0, z 4,
  l $sldata.6, l 2, l 2,
}

export function section ".text.main" "ax" $main() {
@start.0
	%binding.4 =l alloc8 8
@body.1
	storel $typeinfo.5, %binding.4
@.2
	ret
}
```

This has the unfortunate effect of re-generating all of these typeinfo
structures every time someone uses  `type(struct { x: int, y: int })` . We still
have one trick up our sleeve, though: type aliases! Most people don’t actually
use anonymous structs like this often, preferring to use a type alias to give
them a name like “coords”. When they do this, the situation improves:

```
type coords = struct { x: int, y: int };

export fn main() void = {
	let x = type(coords);
};
```

```
data $strdata.1 = section ".data.strdata.1" { b "coords" }

data $sldata.0 = section ".data.sldata.0" { l $strdata.1, l 6, l 6 }

data $strdata.4 = section ".data.strdata.4" { b "x" }

data $strdata.5 = section ".data.strdata.5" { b "y" }

data $sldata.3 = section ".data.sldata.3" {
  l $strdata.4, l 1, l 1, l 0, l $rt.builtin_int,
  l $strdata.5, l 1, l 1, l 4, l $rt.builtin_int,
}

data $typeinfo.2 = section ".data.typeinfo.2" {
  w 2617358403, z 4,
  l 8,
  l 4,
  w 0, z 4,
  w 5555256, z 4,
  w 0, z 4,
  l $sldata.3, l 2, l 2,
}

data $type.1491593906 = section ".data.type.1491593906" {
  w 1491593906, z 4,
  l 8,
  l 4,
  w 0, z 4,
  w 3241765159, z 4,
  l $sldata.0, l 1, l 1,
  l $typeinfo.2
}

export function section ".text.main" "ax" $main() {
@start.6
	%binding.10 =l alloc8 8
@body.7
	storel $type.1491593906, %binding.10
@.8
	ret
}
```

The declaration of a type alias provides us with the perfect opportunity to
statically allocate a typeinfo singleton for it. Any of these which go unused by
the program are automatically stripped out by the linker thanks to the
 `--gc-sections`  flag. Also note that a type alias is considered a distinct
representation from the underlying struct type:

```
type alias = struct {
	ident: []str,
	secondary: type,
};
```

This explains the differences in the structure of the “type.1491593906” global.
The  `struct { x: int, y: int }`  type is
the “secondary” field of this type.

## Future improvements

This is just the first half of the equation. The next half is to provide useful
functions to work with this data. One such example is “types::strenum”:

```
// Returns the value of the enum at "val" as a string. Aborts if the value is
// not present. Note that this does not work with enums being used as a flag
// type, see [[strflag]] instead.
export fn strenum(ty: type, val: *void) str = {
	const ty = unwrap(ty);
	const en = ty.repr as enumerated;
	const value: u64 = switch (en.storage) {
	case builtin::CHAR, builtin::I8, builtin::U8 =>
		yield *(val: *u8);
	case builtin::I16, builtin::U16 =>
		yield *(val: *u16);
	case builtin::I32, builtin::U32 =>
		yield *(val: *u32);
	case builtin::I64, builtin::U64 =>
		yield *(val: *u64);
	case builtin::INT, builtin::UINT =>
		yield switch (size(int)) {
		case 4 =>
			yield *(val: *u32);
		case 8 =>
			yield *(val: *u64);
		case => abort();
		};
	case builtin::SIZE =>
		yield switch (size(size)) {
		case 4 =>
			yield *(val: *u32);
		case 8 =>
			yield *(val: *u64);
		case => abort();
		};
	case => abort();
	};

	for (let i = 0z; i < len(en.values); i += 1) {
		if (en.values[i].1.u == value) {
			return en.values[i].0;
		};
	};

	abort("enum has invalid value");
};
```

This is used like so:

```
use types;
use fmt;

type watchmen = enum {
	VIMES,
	CARROT,
	ANGUA,
	COLON,
	NOBBY = -1,
};

export fn main() void = {
	let officer = watchmen::ANGUA;
	fmt::println(types::strenum(type(watchmen), &officer))!; // Prints ANGUA
};
```

Additional work is required to make more useful tools like this. We will
probably want to introduce a “value” abstraction which can store an arbitrary
value for an arbitrary type, and helper functions to assign to or read from
those values. A particularly complex case is likely to be some kind of helper
for calling a function pointer via reflection, which we I may cover in a later
article. There will also be some work to bring the “types” (reflection) module
closer to the  xxxx ::* namespace, which already
features  xxxx ::ast,  xxxx ::parse, and  xxxx ::types, so that the parser, type checker, and
reflection systems are interopable and work together to implement the  xxxx  type system.

*Want to help us build this language? We are primarily looking for help in the
following domains:*

* *Architectures or operating systems, to help with ports*
* *Compilers & language design*
* *Cryptography implementations*
* *Date & time implementations*
* *Unix*

*If you’re an expert in a domain which is not listed, but that you think we
should know about, then feel free to reach out. Experts are perferred, motivated
enthusiasts are acceptable. [Send me an email](mailto:sir@cmpwn.com) if you want to help!*
