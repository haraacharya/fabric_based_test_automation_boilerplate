from framework_lib import *

#test_case: Anything related to edp display can use this method. Idea is to make one method to check all display related scenarios..
#Make sure we have installed edid-decode in our host machine (ubuntu) with below command
#sudo apt-get install edid-decode
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
    #get_edid_info_hexdump = run_command_with_warn_only_true('hexdump ' + os.path.normpath("/sys/devices/pci0000:00/0000:00:02.0/drm/card0/card0-eDP-1/edid") + " | tee " + "/tmp/edid_info")
    get_edid_info_hexdump = run_command_with_warn_only_true(edid_cmd)
    print "get_edid_info_hexdump is:", get_edid_info_hexdump
    get("/tmp/edid_info", "./edid_info")
    edid_decode_info = local("edid-decode edid_info", capture=True)
    print "will check pass fail"
    print edid_decode_info
    
    if edid_decode_info:
	result = "PASS"
	print edid_decode_info
        return (test_name, result, "basic edp display")
    else:
        result = "FAIL"
	print "FAIL"
   
    print return_message
    return (test_name, result, "basic edp display")


