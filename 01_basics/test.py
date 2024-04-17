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