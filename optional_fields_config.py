#####################################
##    PARSES THE OPTIONAL OUTPUT    #
#####################################

from configparser import ConfigParser
cf=ConfigParser(allow_no_value=True)
cf.read('node_device.conf')


# VALID SECTIONS
existing_sections = []
for item in cf.sections():

    # CHECKS IF THE SECTION EXISTS, 
    if item != "optional_output" and cf.has_section(item):  
        existing_sections.append(item)

print('existing_sections:')    
print(existing_sections)
print('\n')

# CHECKS IF THE DATA HAS TO BE PRINTED OUT
displayed_fields = []

for item in existing_sections:
    if cf.get("optional_output",item)== 'true':
        print(item)



