# PY2PUML instructions

- create virtual enviroment:
  - (on pycharm -> Settings->Project:<Name> -> Python interpreter->Add Interpreter-> New (enviroment)-> choose python as base interpreter for virtual)
  - I recommned for the location of virtual the following: C:\..\PlantUMLTest  **\venv**  - you have to write the bold part
- Install py2puml with pip `pip install py2puml` after creating virtual open up terminal on pycharm should be (<interpretername>) PS C:\..
- Generate puml two ways:  
  - Run py2puml on project folder `py2puml container container`
  - If you wish to automatically generate diagram not have it in terminal :
  `py2puml container container | Out-File -FilePath diagram.puml -Encoding UTF8`
  - Also in Settings, go to plugins and install PlantUML integration (to visualize)

There needs to be a `__init__.py` file in the project root for py2puml to work
<br>
<br>
Imports need to specify project root 
- `from Class2 import ...` **WRONG**
- `from container.Class2 import ...` **CORRECT**

