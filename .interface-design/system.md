# Signal Station interface system

This is a Rich terminal application, with a radio-workbench visual direction. The canonical palette, component registry, spacing, width behavior and plain-output rules are in [docs/TERMINAL_DESIGN.md](../docs/TERMINAL_DESIGN.md). Read that specification before changing presentation code.

Reuse `course/terminal.py` for all styled output. Grading, ownership, tests and saved progress remain in the engine and lesson modules. Web showcase, CSS, font downloads and frontend dependencies are outside this terminal application.
