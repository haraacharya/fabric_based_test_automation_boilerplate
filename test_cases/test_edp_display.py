from framework_lib import *
import subprocess
import fabric_executor

#test_case: Anything related to edp display can use this method. Idea is to make one method to check all display related scenarios..
#Make sure we have installed edid-decode in our host machine (ubuntu) with below command
#sudo apt-get install edid-decode
@device_check
def edp_display_test():
    test_name = "edp_display_tests"
    return_message = ""
    result = "FAIL"	
    find_edid_file_absolute_path = run_command_with_warn_only_true("find / -name edid | grep -i edp")
    edid_file_absolute_path = command_output_formatter(find_edid_file_absolute_path)
    edid_file_absolute_path = edid_file_absolute_path.strip()
    print edid_file_absolute_path
    edid_cmd = "hexdump " + edid_file_absolute_path + " | tee " + "/tmp/edid_info"
    print "edid_cmd is:******", edid_cmd
    get_edid_info_hexdump = run_command_with_warn_only_true(edid_cmd)
    print "get_edid_info_hexdump is:", get_edid_info_hexdump
    edid_info_host_location = fabric_executor.misc_test_folder_location + "/edid_info"
    print "edid_info_host_location is: ", edid_info_host_location
    get("/tmp/edid_info", edid_info_host_location)
    edid_decode_cmd = 'edid-decode ' + edid_info_host_location
    print "edid_decode_cmd is: ", edid_decode_cmd
    edid_decode_info = subprocess.Popen(['edid-decode', edid_info_host_location]  , stdout=subprocess.PIPE).communicate()[0]
    print "will check pass fail"
    print "edid_decode_info output is: ", edid_decode_info
    
    if edid_decode_info:
        print "edid_decode_info output is: ", edid_decode_info
	result = "PASS"
	print edid_decode_info
        return (test_name, result, "basic edp display")
    else:
        result = "FAIL"
	print "FAIL"
   
    print return_message
    return (test_name, result, "basic edp display")


