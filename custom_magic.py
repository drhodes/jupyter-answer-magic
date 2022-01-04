from IPython.core.magic import register_line_magic
import pickle
from pathlib import Path

def get_pickle_data(fpath):
    if fpath.exists():
        try:
            with open(fpath.name, 'rb') as f:            
                return pickle.load(f)
        except EOFError:            
            return {}
    else:
        return {}
    
def dumpvar(varname, value):
    # should be serialized to json instead of pickle for security
    # reasons.
    
    fpath = Path(pickle_name())
    stored_lab_answers = get_pickle_data(fpath)
    stored_lab_answers[varname] = value

    with open(fpath.name, 'wb+') as f:
        pickle.dump(stored_lab_answers, f)
        print(f'>> variable {varname} is ready to grade')

#-----------------------------------------------------------------------------
# Yes, this is a little weird. 

__NOTEBOOK_NAME__ = None
        
@register_line_magic
def set_notebook_name(name):
    global __NOTEBOOK_NAME__
    __NOTEBOOK_NAME__ = name

def notebook_name():
    if __NOTEBOOK_NAME__:
        return __NOTEBOOK_NAME__
    raise NameError("notebook name not defined, please use %set_notebook_name")

def pickle_name():
    return notebook_name() + ".pickle"

#-----------------------------------------------------------------------------

@register_line_magic
def show_answers(*args):
    ''' output the current answers '''
    fpath = Path(pickle_name())
    stored_lab_answers = get_pickle_data(fpath)
    print((stored_lab_answers, fpath))

        
@register_line_magic
def answer(varname):
    if varname == "":
        print("please supply a variable name to mark as answer")
        return

    # needs more checking for the variable name
    try:
        # what kind of security issues can arise here with eval?
        # is there another way to get the value of varname?
        value = eval(varname)
        
        dumpvar(varname, value)
    except NameError as e:
        print(f"Error: {e}, please check that it is defined")
    
    # return outfile

    
# In an interactive session, we need to delete these to avoid
# name conflicts for automagic to work on line magics.
del answer
