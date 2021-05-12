import configargparse
import yaml




# GET SENSOR LIST
def get_sensor_list():
    p = configargparse.ArgParser( 
        
    default_config_files=['./configargparse.yaml'],
    config_file_parser_class=configargparse.ConfigparserConfigFileParser,
    # delimiters=("=",":"),
    )   

    p.add('-c', '--config-file', required=False, is_config_file=True, help='config file path')

    p.add('-s','--sensors',required=False, help="enter the list of sensors")

    p.add('optional_output', nargs='+', help='variant file(s)')

    options = p.parse_args()

    # print(type(options))
    print(options)
    # print((options.sensors))
    sensors =str(options.sensors).replace(" ","").replace("{","").replace("}","").split(',')
    return options, sensors

#GET CONFIGURATION FOR EACH SENSOR:
def parse_settings(sensor,sensor_conf_dict):
    
    sensor_config_fields = sensor_conf_dict

    # sensor_conf_dict[sensor]
    
    config_dict = {}
    for config_field in sensor_config_fields:
        key = config_field[0]
        value = config_field[1]

        if value.lower() == "false":
            config_dict[key] = False
        else:
            config_dict[key] = True 


if __name__ == "__main__":
    sensor_conf, sensors = get_sensor_list()
    sensor_conf_dict = {}

    # print(type(sensor_conf.optional_output))
    print('\n')

    for item in sensor_conf.optional_output:
        sensor_conf = (item.replace("'","")
                .replace('{','[{"')
                .replace('}','"}]')
                .replace(' ',"")
                .replace('--',"")
                .replace(':','":"')
                .replace('=','":"')
                .replace(',','"},{"')
                .replace('"[{','[{')
                .replace('}]"','}]'))

        s = '{"' + sensor_conf + '}'

        sensor_conf_dict.append(eval(s))
        print(eval(s))
        # print(s)