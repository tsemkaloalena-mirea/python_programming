# from module_for_task3 import GLOBAL_VAR
# import additional_module_for_task3
#
# GLOBAL_VAR = 42
#
# print(GLOBAL_VAR)
# print(additional_module_for_task3.get_global_var())


import module_for_task3
import additional_module_for_task3

module_for_task3.GLOBAL_VAR = 42

print(module_for_task3.GLOBAL_VAR)
print(additional_module_for_task3.get_global_var())
