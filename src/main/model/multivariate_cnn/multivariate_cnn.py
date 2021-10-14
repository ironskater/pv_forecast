import configparser
import sys
import tensorflow as tf
import os
import numpy as np
from contextlib import redirect_stdout
from datetime import datetime
from pathlib import Path

time_steps = 3
feature_dim = 1

def create_model(model_name):
    input = tf.keras.Input(shape=(  time_steps,
                                    feature_dim))

    x = tf.keras.layers.Conv1D( filters=63,
                                kernel_size=2,
                                padding='valid',
                                activation='relu',
                                strides=1)(input)

    x = tf.keras.layers.MaxPooling1D(pool_size=2)(x)
    x = tf.keras.layers.Flatten()(x)
    x = tf.keras.layers.Dense(  50,
                                activation='relu')(x)
    output = tf.keras.layers.Dense( 1,
                                    activation='relu')(x)

    model = tf.keras.Model( inputs=input,
                            outputs=output,
                            name=model_name)

    model.compile(  loss='mse',
                    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001))

    return model

# def write_to_file(model):
#     with open('report/multivariate_cnn/arch', 'a') as f:
#         with redirect_stdout(f):
#             model.summary()

#         f.write('#'*80 + '\n')
#         f.write('#'*80 + '\n')

def write_metrics(model_name, metrics, path):
    if not os.path.exists(path):
        with open(path, 'w') as f:
            f.write('model_name,mae,rmse,mape,r2\n')

    with open(path, 'a') as f:
        f.write(model_name + ',' + metrics + '\n')

if __name__ == '__main__':

    print('start training model....................................')

    config = configparser.ConfigParser()
    config_dir = sys.argv[1]
    config.read(config_dir)

    print('epoch:', config['hyperparam']['epoch'])
    print('learning rate:', config['hyperparam']['learning_rate'])

    now_dt = datetime.now()
    model_name = 'multivariate_cnn_' + now_dt.strftime('%Y%m%d%H%M%S')
    model = create_model(model_name)
    model.save(os.path.join(sys.argv[3], model_name + '.h5'))

    # fit model

    # record metrics
    Path(sys.argv[4]).mkdir(parents=True, exist_ok=True)
    write_metrics(  model_name,
                    ','.join(str(round(element, 2)) for element in np.random.rand(4)),
                    os.path.join(   sys.argv[4],
                                    'multivariate_cnn_metrics'))

    # write_to_file(model)
    model.summary()