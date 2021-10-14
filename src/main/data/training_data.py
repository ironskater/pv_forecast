import configparser
import sys
import os

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config_dir = sys.argv[1]
    config.read(config_dir)

    print('do training_data......................................')

    output_dir = os.path.join(sys.argv[3], 'training_data')

    with open(output_dir, 'w') as f:
        f.write(config['training_data']['time_step'] + ',')
        f.write(config['training_data']['normalization_method'] + '\n')

    print('============================================================')