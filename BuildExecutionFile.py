import sys

# Use the sys package to grab command line arguments for the web test name and result location
web_test_name = str(sys.argv[1])
test_suite = str(sys.argv[2])

# TODO: Might need 3rd parameter for the environment if we can't pull from
# TODO: the plugin that Gordon was using for that for the gVar in QTP

# Open our file in write mode and begin writing the QTP execution script
file = open("QTP_Run_Script.vbs",'w')

file.write("'Create QTP object\n")
file.write("Set QTP = CreateObject(\"QuickTest.Application\")\n")
file.write("QTP.Launch\n")
file.write("QTP.Visible = TRUE\n")
file.write('\n')

file.write("'Open QTP Test\n")
file.write('QTP.Open "'+web_test_name+'", TRUE \'Set the QTP test path\n')
file.write('\n')

file.write("'Set Result location\n")
file.write("Set qtpResultsOpt = CreateObject(\"QuickTest.RunResultsOptions\")\n")

file.write('qtpResultsOpt.ResultsLocation = "'+web_test_name+'\Report" \'Set the results location\n')

file.write("'Set the Test Parameters\n")
file.write("Set pDefColl = QTP.Test.ParameterDefinitions\n")
file.write("Set qtpParams = pDefColl.GetParameters()\n")
file.write('\n')

file.write("'Set the value for test environment through command line\n")
file.write("On Error Resume Next\n")
file.write("qtpParams.Item(\"TestSuite\").Value = LCase("+test_suite+")\n")
file.write("On Error GoTo 0\n")
file.write('\n')

file.write("'Attach the vbs files to the test\n")
file.write("'QTP.Test.Settings.Resources.Libraries.RemoveAll   'Remove everything\n")
file.write("'QTP.Test.Settings.Resources.Libraries.Add(\"..\functions\TestInitialize.vbs\")\n")
file.write("\n")

file.write("'Run QTP test\n")
file.write("QTP.Test.Run qtpResultsOpt, FALSE, qtpParams\n")
file.write("\n")

file.write("'Close QTP\n")
file.write("'QTP.Test.Close\n")
file.write("'QTP.Quit\n")

file.close()