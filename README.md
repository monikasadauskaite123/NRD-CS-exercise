# NRD-CS-exercise
The exercise can be found in the exercise.txt file. Solution to the exercise is the exercise.py file written in the pytest framework.
# Application
In the terminal type command line
```
python exercise.py
```
to obtain results for the given exercise. 
> [!WARNING]
> This command line will stop `cron.service`

Moreover, type
```
pytest exercise.py
```
to obtain the results of the pytest for different functions described below.
# Documentation
Functions are defined in the exercise.py file


Non-pytest functions
-
- `exists(file_name, path)`: checks if a given file exists in a specified directory
  - arguments:
    - `file_name` - name of the file, string
    - `path` - directory, in which the file will be searched, string
  - returns:
    - `True` - file exists in the directory
    - `False` - file does not exist in the directory

- `birth_time(file_name, path)`: returns the age of the file, i.e. from creation time if compiled on Windows and birth/change time on Linux
  - arguments:
    - `file_name` - name of the file, string
    - `path` - directory of the file, string
  - returns a tuple, with the first element a float - the age of the file (from birth/creation/change time) in hours, rounded to 0.1. The second element is of a boolean data type. `True` corresponds to a successful application of `st_birthtime` and `False` corresponds to the application of `os.path.getctime(file)`
- `find_parameter(diction, parameter)`: a recursive function that returns the value, i.e. item, in a nested dictionary, given a parameter, i.e. key
  - arguments:
    - `diction` - nested dictionary, dict
    - `parameter` - given key parameter
  - returns:
    - the item (first occurrence) corresponding to the given parameter
    - `None` if there is no such parameter key

- `parameter_value(file_name, path, parameter)`: reads and loads a file and returns the value, i.e. item, of a given a parameter, i.e. key, in a nested dictionary
  - arguments:
    - `file_name` - name of the file, string
    - `path` - directory of the file, string
    - `parameter` - given key parameter
  - returns:
    - a string `"LoadError"` in case the file is neither of the types 'json', 'yaml'
    - the item (first occurrence) corresponding to the given parameter
    - `None` if there is no such parameter key
      
- `size(file_name, path)`: returns the size of the file in bytes in a given directory
  - arguments:
    - `file_name` - name of the file, string
    - `path` - directory of the file, string
  - returns a float corresponding to the size of the file in bytes in a given directory
    
- `service_status(service)`: returns the status of a given service
  - arguments:
    - `service` - name of service, string
  - returns a string corresponding to the status of a given service. Output examples: 'active', 'inactive'

  
- `service_control(service, action)`: stops or starts a given service
  - arguments:
    - `service` - name of service, string
    - `action` - `"start"` starts a service, `"stop"` stops a service
  - returns `None`

- `OS_version()`: 
  - returns OS version as a string

Pytest functions
-
- `test_exists(file_name, path, expect)`: asserts if the existence of the file is according to expectations
  - arguments:
    - `file_name` - name of the file, string
    - `path` - directory, in which the file will be searched, string
    - `expect` - expected output of function `exists`. Possible values are `True` and `False`
- `test_birth_time(file_name, path, expect)`: asserts if the `st_birthtime` was successfully applied
  - arguments:
    - `file_name` - name of the file, string
    - `path` - directory of the file, string
    - `expect` - expected output (second element) of function `birth_time`. Possible values are `True` and `False`
   
    
- `test_parameter_value(file_name, path, parameter, expect_format)`: asserts if the data was successfully loaded from a given file. Asserts if the parameter exists in the file as a key. Asserts if the item corresponding to the given parameter key is of the correct format.
  - arguments:
    - `file_name` - name of the file, string
    - `path` - directory of the file, string
    - `parameter` - given key parameter
    - `expect` - expected format of the output of the function `parameter_value`, tuple: first element corresponding to the number of strings separated by the character given by the second element of the tuple
   

- `test_size(file_name, path, expect)`: asserts if the size of the given file is according to expectations
  - arguments:
    - `file_name` - name of the file, string
    - `path` - directory of the file, string
    - `expect` - expected size of the file in bytes

- `test_service_status(service, expect)`: asserts the status of the service is according to expectations
  - arguments:
    - `service` - name of service, string
    - `expect` - expected status of a service. Example: `"active"`, `"inactive"`

