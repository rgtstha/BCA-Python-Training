# Packages In Python

- A package is a collection of modules
- A module is a single Python file
- A package is a directory of Python modules containing an additional __init__.py file
- A package can have sub-packages

## Python Standard Library
- Python comes with a standard library of modules
- The standard library is a set of modules that are part of the Python distribution
- The standard library is installed with Python
- The standard library is always 

- Examples of standard library modules:
    - os
    - sys
    - math
    - random
    - datetime
    

## Third Party Packages

- Third party packages are packages that are not part of the Python standard library
- These are are created by other developers
- These are installed using a package manager

- We can use `pip` to install packages

Link to [pip](https://pypi.org/project/pip/)

## PiP commands
- `pip install <package_name>` - installs a package
- `pip uninstall <package_name>` - uninstalls a package
- `pip list` - lists all installed packages
- `pip freeze` - lists all installed packages and their versions
- `pip show <package_name>` - shows information about a package
- `pip search <package_name>` - searches for a package



## Python Example Using package

```python
import requests

def get_random_advice():
    url = "https://api.adviceslip.com/advice"
    response: requests.Request = requests.get(url)

    if response.status_code == 200:
        advice_data = response.json()

        print(type(advice_data))
        return advice_data["slip"]["advice"]
    else:
        print("Error fetching advice")
        return None

if __name__ == "__main__":
    random_advice = get_random_advice()

    if random_advice:
        print("Random Advice:")
        print(random_advice)

```

We can use `dataclasses` to create a class that represents the data we get back from the API