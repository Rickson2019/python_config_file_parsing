#####################################
##    PARSES THE OPTIONAL OUTPUT    #
#####################################

from configparser import ConfigParser
from utils import mock_data as md
cf=ConfigParser(allow_no_value=True)



# GET SENSOR LIST
def get_sensor_list():
    sections = cf.sections()
    sensors = []
    for section in sections:
        # FIXME: quite weird that the configParser converts all fields to lowercase
        # print("original",section)
        # print("cf.options",cf.options(section))
        # temp = section
        # lower_temp = temp.lower()
        if section.lower() == 'sensors':
            sensors = cf.options(section)
            print(sensors)
    return sensors


#GET CONFIGURATION FOR EACH SENSOR:
def parse_settings(sensor,sensor_conf_dict):
    
    sensor_config_fields = cf.items(sensor.upper())
    # sensor_conf_dict[sensor]
    
    config_dict = {}
    for config_field in sensor_config_fields:
        key = config_field[0]
        value = config_field[1]

        if value.lower() == "false":
            config_dict[key] = False
        else:
            config_dict[key] = True 


    sensor_conf_dict[sensor] = config_dict

    print(sensor_conf_dict[sensor])




 
    





def mock_sensor_push(sensor,sensor_conf_dict):
    
    # FIXME: it has to be in lowercase
    output_items = sensor_conf_dict[sensor.lower()]

    for item in output_items:

        if(item == "temperature" and output_items[item] == True):
            print(item,": 10 degrees")
        elif(item == "humidity" and output_items[item] == True):
            print(item,": 50%")
        elif(item == "timestamp" and output_items[item] == True):
            print(item,": 999999699999")

if __name__ == "__main__":

    cf.read('node_device.conf')
    sensors = get_sensor_list()

    # global config object
    sensor_conf_dict = {}
    
    # parsing for each sensor
    print('parsing: \n')
    for sensor in sensors:
        parse_settings(sensor, sensor_conf_dict)

    mock_sensor_push("DHT11", sensor_conf_dict)

