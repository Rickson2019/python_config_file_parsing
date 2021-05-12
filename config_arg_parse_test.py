# in your configargparse setup
import configargparse
import yaml

parser = configargparse.ArgParser(
    config_file_parser_class=configargparse.ConfigparserConfigFileParser
)

parser.add_argument('--system1_settings', type=yaml.safe_load)

args = parser.parse_args() # now args.system1 is a valid python dict

print(args)