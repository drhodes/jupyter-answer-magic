from IPython.core.magic import register_line_magic
import pickle
from pathlib import Path

def get_pickledata(fpath):
    if fpath.exists():
        try:
            with open(fpath.name, 'rb') as f:            
                return pickle.load(f)
        except EOFError:
            return {}
    else:
        return {}

def dumpvar(outfile, varname, value):
    fpath = Path(outfile + ".pickle")
    stored_lab_answers = get_pickledata(fpath)
    stored_lab_answers[varname] = value

    with open(fpath.name, 'wb+') as f:
        pickle.dump(stored_lab_answers, f)
        print(f'>> variable {varname} is ready to grade')

        
@register_line_magic
def answer(varname):
    if varname == "":
        print("please supply a variable name to mark as answer")
        return
    
    # import ipyparams
    # 
    notebook_name = "SimpleLab1"

    # needs more checking for the variable name
    # 
    
    try:
        # what kind of security issues can arise here with eval?
        # is there another way to get the value of varname?
        value = eval(varname)
        
        dumpvar(notebook_name, varname, value)
    except NameError as e:
        print(f"Error: {e}")
        
    
    # return outfile

# In an interactive session, we need to delete these to avoid
# name conflicts for automagic to work on line magics.
del answer
