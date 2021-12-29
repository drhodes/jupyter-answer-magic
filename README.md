
Jupyter notebooks may be extended with something called linemagic
(among other types).  This line magic allows users to dump specified
variables out to a file that can be used for grading.

Each Jupyter user has and directory located at
`~/.ipython/profile_default/startup`.

`custom_magic.py` should be placed in that directory to ensure that it
is loaded when either a jupyter notebook or an ipython interpreter is started.

TODO:

- Check that the ipyparams package is installed so the notebook name
  can be found.

- How to copy `custom_magic.py` to its place when kubernetes is
  installing?

- Is there a better way than `eval` to get at the value of varname
  (see source)
  


