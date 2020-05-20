from UnetShorterModel import unet_short
from Generator import DataGenerator
import os


from keras.callbacks import CSVLogger
from keras.callbacks import TensorBoard
from keras.callbacks import ModelCheckpoint,EarlyStopping,ReduceLROnPlateau


DATASET_PATH = 'processed_data'

ids = os.listdir(DATASET_PATH)

train_ids = ids[0:int(len(ids)*0.7)]
test_ids  = ids[int(len(ids)*0.7):]

train_generator = DataGenerator(DATASET_PATH,train_ids)
test_generator  = DataGenerator(DATASET_PATH,test_ids)

model = unet_short()
model.summary()

csv_logger = CSVLogger('log_unet.csv', append=True, separator=';')
tensorboard = TensorBoard(log_dir='./tensorboard_unet/', write_graph=True, write_images=True)
model.fit_generator(train_generator, epochs=1,
                  verbose=2, shuffle=True,
                  #callbacks=[csv_logger, tensorboard],
                  validation_data=test_generator)

