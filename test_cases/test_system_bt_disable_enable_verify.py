from framework_lib import *

#test_case: system bt enable disable verify
#use this to explore other commands under bluetoothctl commandline interface and in fact we can
@device_check
def system_bt_enable_disable_verify():
    test_name = "system_bt_enable_disable_verify"
    return_message = ""
    result = "FAIL"	
    bluetooth_enable_cmd = run_command_with_warn_only_true('hciconfig hci0 up')
    hcitool_dev_output = run_command_with_warn_only_true("hcitool dev")
    print "hcitool_dev_output is:", hcitool_dev_output	
    if hcitool_dev_output.failed:
	print "FAIL"        
	result = "FAIL"
	return_message = hcitool_dev_output 
    else:
	print "disabling bt and confirming bt controller is not showing off"
        #bluetooth_disable_cmd = run_command_with_warn_only_true('echo -e "power off\n" | bluetoothctl ') #use this to explore other commands under bluetoothctl commandline interface and in fact we can pair unpair devices based on mac id with this.
	bluetooth_disable_cmd = run_command_with_warn_only_true('hciconfig hci0 down')
        hcitool_dev_output_after_disabling_controller = run_command_with_warn_only_true("hcitool dev")
	if re.match("hci0", hcitool_dev_output_after_disabling_controller):
	    print "bt is not getting disabled"
            result = "FAIL"
	    print "FAIL"
	    hcitool_dev_output_after_disabling_controller = return_message_formatter(hcitool_dev_output_after_disabling_controller)	        
	    return_message = hcitool_dev_output_after_disabling_controller 
	else:
	    print "BT disabled"
	    print "PASS"
	    result = "PASS"
	    print "Enabling BT back for further use"
	    hcitool_dev_output_after_disabling_controller = return_message_formatter(hcitool_dev_output_after_disabling_controller)
            return_message = hcitool_dev_output_after_disabling_controller 
	    bluetooth_disable_cmd = run_command_with_warn_only_true('echo -e "power on\n" | bluetoothctl ')	
    print return_message
    return (test_name, result, return_message)


