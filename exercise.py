import pytest
import os
import time
import pathlib
import json
import yaml
import subprocess
import platform

cwd = os.getcwd()

def exists(file_name, path):
    return os.path.exists(path)
    
@pytest.mark.parametrize("file_name, path, expect", [
    ("file_1", cwd, True),("file_2", cwd, True),])
def test_exists(file_name, path, expect):
    result = exists(file_name, path)
    assert expect == result, f"{file_name} exists: {result}. Existance was expected: {expect}"

def birth_time(file_name, path):
    #Linux does not store the creation time of files. We can try to obtain the birth time
    try:
        path = pathlib.Path(cwd+'/'+file_name)
        stats = path.stat()
        birth_t = stats.st_birthtime
        birth = True
    except AttributeError:
        birth_t = os.path.getctime(cwd+'/'+file_name) #this gets 'change' time instead of creation/birth time because some Unix systems do not have the attribute st_birthtime
        birth = False
    curr_t = time.time()
    return round((curr_t-birth_t)/3600,1), birth

@pytest.mark.xfail(reason="Some Unix systems do not have the attribute 'st_birthtime', the function then returns 'Change' time instead of 'Birth' time")
@pytest.mark.parametrize("file_name, path, expect", [
    ("file_1", cwd, True),])
def test_birth_time(file_name, path, expect):
    assert birth_time(file_name, path)[1], "Some Unix systems do not have the attribute 'st_birthtime', the function then returns 'Change' time instead of 'Birth' time"

def find_parameter(diction, parameter):
    for key in list(diction.keys()):
        try: return diction[parameter]
        except: 
            if isinstance(diction[key], dict):
                return find_parameter(diction[key], parameter)
            elif isinstance(diction[key], list):
                for element in diction[key]:
                    return find_parameter(element, parameter)
            
def parameter_value(file_name, path, parameter):
    with open(path+'/'+file_name, 'r') as file:
        try: data = yaml.safe_load(file)
        except:
            try: data = json.load(file)
            except: return 'LoadError'
    return find_parameter(data, parameter)   
    
@pytest.mark.parametrize("file_name, path, parameter, expect_format", [
    ("file_1", cwd, 'hnmanager', (3,',')),("file_2", cwd, 'updated', (3,':')),])
def test_parameter_value(file_name, path, parameter, expect_format):
    value = parameter_value(file_name, path, parameter)
    
    assert value != 'LoadError', f"Error in loading the file {file_name}" #in case the data was not loaded
    
    assert value != None, f"No parameter '{parameter}' in '{file_name}'" #in case the parameter is not in the file
        
    #in case the format of the value of the parameter is not as expected
    split_value = value.split(expect_format[1])
    assert len(split_value) == expect_format[0], f"Format of parameter '{parameter}' value in '{file_name}' is incorrect. Expected {expect_format[0]} strings separated by '{expect_format[1]}', got '{value}'"     

def size(file_name, path):
    return os.path.getsize(path+'/'+file_name)

@pytest.mark.parametrize("file_name, path, expect", [("file_2", cwd, 572),])
def test_size(file_name, path, expect):
    file_size = size(file_name, path)
    assert file_size == expect, f'Expected size: {expect} bytes, actual size: {file_size} bytes'

def service_status(service):
    command = 'systemctl status cron.service | grep Active: | cut -d" " -f7'
    return subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode().strip()

@pytest.mark.parametrize("service, expect", [('cron.service', 'inactive'),])
def test_service_status(service, expect):
    status = service_status(service)
    assert status == expect, f"Expected '{service}' status: {expect}. Actual '{service}' status: {status}"

def service_control(service, action):
    command = f'sudo systemctl {action} {service}'
    subprocess.run(command, shell=True)

def OS_version():
    return platform.platform()

print("Displaying results:")
print(f"1. 'file_1' exists: {exists('file_1', cwd)}")
print(f"2. 'file_1' created {birth_time('file_1', cwd)[0]} hrs ago")
print(f"3. 'hnmanager' parameter value: {parameter_value('file_1', cwd, 'hnmanager')}")
print(f"4. 'file_2' exists: {exists('file_2', cwd)}")
print(f"5. 'file_2' size: {size('file_2', cwd)} bytes")
print(f"6. 'updated' parameter value: {parameter_value('file_2', cwd, 'updated')}")
print(f"7. Status of 'cron.service': {service_status('cron.service')}")
service_control('cron.service', 'stop')
print(f"8. Status of 'cron.service' after stopping: {service_status('cron.service')}")
print(f"9. OS version: {OS_version()}")


