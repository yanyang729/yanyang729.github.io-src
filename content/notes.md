Title: Useful syntax/command
Date: 2017-04-14 19:20
Modified: 2017-04-14 19:30
Category: Notes
Tags: python, jupyter
Slug: 

### jupyter notebook
display multiple outputs
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
```
cell with larger width
```python
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:90% !important; }</style>"))
```


