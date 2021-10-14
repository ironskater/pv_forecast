import configparser
import sys
import os

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config_dir = sys.argv[1]
    config.read(config_dir)

    print('do aggregate_data ..............................................')

    output_dir = os.path.join(sys.argv[3], 'aggregate_data')

    with open(output_dir, 'w') as f:
        f.write(config['aggregate_data']['resample_rule'] + '\n')

    print('============================================================')