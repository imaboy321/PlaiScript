import os
gui_main = ['PlaiScript_Main.ui', 'gui_main.py']
select = ['PlaiScript_Select.ui', 'select.py']
parsed = ['PlaiScript_Parsed.ui', 'parsed.py']

os.remove(gui_main[1])
os.remove(select[1])
os.remove(parsed[1])

os.system('pyuic4 {0} >> {1}'.format(gui_main[0], gui_main[1]))
os.system('pyuic4 {0} >> {1}'.format(select[0], select[1]))
os.system('pyuic4 {0} >> {1}'.format(parsed[0], parsed[1]))
print "gui Generated"