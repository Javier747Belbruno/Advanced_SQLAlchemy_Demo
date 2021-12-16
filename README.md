# Advanced Implementation of SQLAlchemy with Flask

* Flask is a microframework for Python based on Werkzeug. [page](https://flask.palletsprojects.com/).
* SQLAlchemy is a Python ORM and provides a simple way to create and manage databases. [page](https://www.sqlalchemy.org/).

Data model defined in this implementation:
![](https://javier747belbruno.github.io/car-control-simulation/assets/database1.png)


## Create Environment
Create an environment to not work with global python libraries installed on your system.

  ```python -m venv .venv```


Once the environment is created, you can activate it by running the following command:
* Linux:
   ``` source .venv/bin/activate```
* Windows:
   ```.\.venv\Scripts\activate.bat```


## Install Requirements.txt (dependencies)
```pip install -r requirements.txt```

## Run the application
```python run.py```


When you are done, you can deactivate the environment by running the following command
to comeback to the OS environment:
* Linux
   ```source .venv/bin/activate```
* Windows
   ```.\.venv\Scripts\deactivate.bat```

Code source original is from [here](https://github.com/corpsgeek/flask-sqlalchemy/)