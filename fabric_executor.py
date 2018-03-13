import re
import csv
import os.path
import time, datetime
from fabric.api import *
from framework_lib import *
from test_cases import *


env.hosts = ['192.168.1.30']
# Set the username
env.user   = "root"
# Set the password [NOT RECOMMENDED]
env.password = "test0000"
misc_test_folder_location = os.getcwd() + "/misc"
print "misc_test_folder_location is: ", misc_test_folder_location
result_csv_file_name = os.getcwd() + "/" + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M') +"_result.csv"
#creating result csv file
with open(result_csv_file_name, 'w') as csvfile:
    fieldnames = ['Test_Name', 'Test_Result', 'Comments or Errors']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    if not os.path.isfile("result.csv"):
        writer.writeheader()


def batch_run():
    run_test(test_system_bt_disable_enable_verify.system_bt_enable_disable_verify)
    run_test(test_edp_display.edp_display_test)




    
    

