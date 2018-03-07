import re
import csv
import os.path
import time, datetime
from fabric.api import *
import fabric_executor

def return_message_formatter(message):
    ansi_escape_regex = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    new_message = ansi_escape_regex.sub('', message)
    newline_escape = re.compile(r'\r\n')
    new_message = newline_escape.sub(', ', new_message)
    return new_message	

def command_output_formatter(message):
    ansi_escape_regex = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    new_message = ansi_escape_regex.sub('', message)
    new_message = new_message.strip()
    newline_escape = re.compile(r'\r\n')
    new_message = newline_escape.sub('', new_message)
    return new_message

def run_command_with_warn_only_true(cmd):
    with settings(warn_only=True):
        return run(cmd)

# Writing test_result into csv file
def write_test_result_into_csv(result_csv_file_name, test_name, test_result, message):
    with open(result_csv_file_name, 'a') as csvfile:
        fieldnames = ['Test_Name', 'Test_Result', 'Comments or Errors']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'Test_Name': test_name, 'Test_Result': test_result, 'Comments or Errors': message})

def run_test(test_method_name):
    test_result = test_method_name()
    print "test_result is******************", test_result
    print "result_csv_file_name is: ", fabric_executor.result_csv_file_name
    write_test_result_into_csv(fabric_executor.result_csv_file_name, test_result[0], test_result[1], test_result[2])
