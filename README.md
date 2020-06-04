# lown

**lown** is a lightweight markup language inspired by BBCode and LISP.

## Features

* LISP inline syntax and BBCode block syntax
* Maths and emoji support
* Parse to HTML

See the [syntax reference](reference.md) for more information.

## Installation (macOS and Linux)

```
$ git clone https://github.com/oileurre/lown/
$ ln -s /usr/local/lown/src/lown.py /usr/local/bin
```

## Usage

```
$ lown file.lown > file.html
$ lown file.lown -s > file.html
```

`-s` stands for *standalone*.
