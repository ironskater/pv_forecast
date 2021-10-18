import utility.logger as logger
import configparser
import sys
import subprocess
import os

def update_stage_ini(   pipeline_config_dir,
                        ini_file):
    config = configparser.ConfigParser()
    config_stage = configparser.ConfigParser()
    config.read(os.path.join(pipeline_config_dir, ini_file))

    for section in config.sections():
        stage_ini_file = os.path.join(pipeline_config_dir, 'tmp', section+'.ini')
        config_stage.read(stage_ini_file)
        change_flg = False

        for key in config_stage.options(section):
            if config_stage[section][key] != config[section][key]:
                config_stage.set(section, key, config[section][key])
                change_flg = True

        if change_flg == True:
            with open(stage_ini_file, 'w') as f:
                config_stage.write(f)

            print(section + ' is updated')

    return

def main():
    pipeline = sys.argv[1] # pipeline name
    pipeline_config_dir = sys.argv[2]
    target = sys.argv[3]

    LOGGER.info('start %s pipeline',
                pipeline)

    if target == 'clean':
        subprocess.call(['make', '-C', pipeline_config_dir, '-f', 'Makefile', 'clean'])
        return

    for file in os.listdir(pipeline_config_dir):
        if not file[-3:] == 'ini':
            continue

        update_stage_ini(   pipeline_config_dir,
                            file)
        # make -C $(pipeline_config_dir) -f Makefile $(target)
        rtn = subprocess.call(['make', '-C', pipeline_config_dir, '-f', 'Makefile', target])

        print('pipeline rtn:', rtn)
        print('-----------------------------------------------------------done')

if __name__ == '__main__':
    LOGGER = logger.init_logger('pipeline_manager.log')
    main()