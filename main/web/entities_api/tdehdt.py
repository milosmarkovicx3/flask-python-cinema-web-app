import importlib
pkg = importlib.import_module(__package__)
print(pkg.a)