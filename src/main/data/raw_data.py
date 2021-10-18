import configparser
import sys
import os
from pathlib import Path

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config_dir = sys.argv[1]
    config.read(config_dir)

    print('do raw_data ..............................................')

    Path(sys.argv[2]).mkdir(parents=True, exist_ok=True)

    output_dir = os.path.join(sys.argv[2], 'raw_data')

    with open(output_dir, 'a') as f:
        f.write(config['raw_data']['start_dt'] + ',')
        f.write(config['raw_data']['end_dt'] + ',')
        f.write(config['raw_data']['site_id'] + '\n')

    print('============================================================')