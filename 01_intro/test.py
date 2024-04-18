from hello import printString

printString("Function imported from another file")

# Python's Inner Working

# python hello.py -> Byte Code (mostly hidden) -> Python VM runs the code

# 1) Compile to Byte Code (low level & platform independent (not a machine code))

# 2) Now low level code is platform independent can run on Windows, Mac 0r Linex it just need Python VM

# 3) .pyc -> Compiled Python (Frozen Binaries)

# __pycache__
# -> works only for imported files
# -> not for top levels files

# Python Virtual Machine PVM
# Code loop to iterate byte code
# Run time Engine
# Also known as Python Interpreter
# Byte Code is NOT machine code
# Byte Code here is Python Specific Interpretation
# Here we uses Standard Implementation which is cPython
# other types are -> jython, IronPython, Stackless, PyPy