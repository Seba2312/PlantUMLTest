# PY2PUML instructions

- Install py2puml with pip `pip install py2puml`
- Run py2puml on project folder `py2puml container container`

There needs to be a `__init__.py` file in the project root for py2puml to work
<br>
<br>
Imports need to specify project root 
- `from Class2 import ...` **WRONG**
- `from container.Class2 import ...` **CORRECT**

