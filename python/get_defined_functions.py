import inspect

# Get all functions defined in a module, and only those that are directly defined (not the imported functions)
# Can be used to run all functions defined in a module, such as a test module.
def get_defined_functions(module):
    all_members = inspect.getmembers(module)
    defined_functions = [obj for name, obj in all_members if inspect.isfunction(obj) and inspect.getmodule(obj) == module]
    return defined_functions