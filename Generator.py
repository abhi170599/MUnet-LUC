import keras
import numpy as np 
import os 


class DataGenerator(keras.utils.Sequence):

    def __init__(self,data_path,ids,batch_size=32,shuffle=True):

        self.ids = ids
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.data_path = data_path

        self.on_epoch_end()

    def __len__(self):
        return int(np.floor(len(self.ids)/self.batch_size))
    
    def __getitem__(self,index):

        indexes = self.indexes[index*self.batch_size:(index+1)*self.batch_size]

        ids_temp = [self.ids[k] for k in indexes]

        X,Y = self.__data_generation(ids_temp)

        return X,Y

    def on_epoch_end(self):

        self.indexes = np.arange(len(self.ids))
        if self.shuffle==True:
            np.random.shuffle(self.indexes)

    def __data_generation(self,ids):

        X = []
        Y = []

        for id in ids:

            img_path  = self.data_path+"/{}/img.npy".format(id)
            mask_path = self.data_path+"/{}/mask.npy".format(id)

            img  = np.load(img_path)
            mask = np.load(mask_path)

            X.append(img)
            Y.append(mask)
        X = np.array(X)
        Y = np.array(Y)
        
        return X,Y    








