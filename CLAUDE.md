# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

A personal study folder for learning object-oriented programming in Python. Code, identifiers, comments and user-facing strings are in Portuguese (pt-BR); keep new code in Portuguese to match. There are no dependencies (standard library only), no packaging, no test suite, no linter config, and no git repository.

## Running

Each file is an independent script run directly:

```
python calculadora.py
```

`calculadora.py` and `clateste.py` are interactive (they block on `input()`); to exercise them non-interactively, pipe input, e.g. `printf "1\n2\n3\n0\n" | python calculadora.py`. To test the calculator classes without the menu, import them: `python -c "from calculadora import CalculadoraCientifica as C; print(C().dividir(1, 3))"` (safe because `main()` is behind `if __name__ == "__main__"`).

`classe.py` and `encapsulamento.py` run their examples at module level, so importing them prints output.

## Files

- `calculadora.py` — the most complete example. `Calculadora` implements the four operations and records each one through the protected `_registrar(expressao, resultado)` helper into `_historico`; every new operation should go through `_registrar` so it shows up in the history. `CalculadoraCientifica` inherits from it, adds `potencia`/`raiz`/`porcentagem`, and overrides `dividir` via `super()` to round results. Errors are raised as `ValueError` and caught by `main()`. The menu in `main()` is driven by the `opcoes` dict mapping a key to `(nome, método, quantidade de números)`, so adding an operation means adding a method plus a dict entry (option `"7"` has special prompt text handled in the loop). `ler_numeros(mensagem, qtd)` reads all of an operation's numbers from a single line separated by spaces (e.g. `10 5`), re-prompting until exactly `qtd` valid numbers are typed; `converter_numero` accepts commas as decimal separators and returns `int` when the value is whole.
- `classe.py` — basic classes, inheritance, method overriding, `super()`, default arguments.
- `encapsulamento.py` — `_protegido` vs `__privado` (name mangling) attributes, getters/setters, `__str__`/`__repr__`.
- `clateste.py` — input loop collecting people into a list of dicts (no classes).

The older study files use lowercase class names (`pessoa`, `animal`, `carro`); `calculadora.py` uses PascalCase and is the style reference for new code.
