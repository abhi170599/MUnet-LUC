import os
import numpy as np
import random 
import tifffile as tiff
import matplotlib.pyplot as plt
import tqdm


PROCESSED_DATA_PATH = 'processed_data'

if not os.path.exists(PROCESSED_DATA_PATH):
    os.mkdir(PROCESSED_DATA_PATH)


def normalize(img):

    min = img.min()
    max = img.max()

    x = 2.0 *(img-min)/(max-min)-1.0
    return x 

""" generate random patches from the image """
def get_rand_patch(img,mask,sz=160):

    """
    @param: img  => ndarray with shape(x_sz,y_sz,num_channels)
            mask => binary ndarray with shape(x_sz,y_sz,num_channels)
            sz   => size of random patch
    @return: patch with shape (sz,sz,num_channels)
    """
    assert len(img.shape)==3 and img.shape[0]>sz and img.shape[1]>sz and img.shape[0:2] == mask.shape[0:2]
    xc = random.randint(0,img.shape[0]-sz)
    yc = random.randint(0,img.shape[1]-sz)

    patch_img  = img[xc:(xc+sz),yc:(yc+sz)]
    patch_mask = mask[xc:(xc+sz),yc:(yc+sz)]

    #Apply some random transformation
    random_transformation = np.random.randint(1,8)
    if random_transformation == 1:  # reverse first dimension
        patch_img = patch_img[::-1,:,:]
        patch_mask = patch_mask[::-1,:,:]
    elif random_transformation == 2:    # reverse second dimension
        patch_img = patch_img[:,::-1,:]
        patch_mask = patch_mask[:,::-1,:]
    elif random_transformation == 3:    # transpose(interchange) first and second dimensions
        patch_img = patch_img.transpose([1,0,2])
        patch_mask = patch_mask.transpose([1,0,2])
    elif random_transformation == 4:
        patch_img = np.rot90(patch_img, 1)
        patch_mask = np.rot90(patch_mask, 1)
    elif random_transformation == 5:
        patch_img = np.rot90(patch_img, 2)
        patch_mask = np.rot90(patch_mask, 2)
    elif random_transformation == 6:
        patch_img = np.rot90(patch_img, 3)
        patch_mask = np.rot90(patch_mask, 3)
    else:
        pass

    return patch_img,patch_mask


def generate_processed_data(n_patches,sz=160):

    
    img_ids = [str(i).zfill(2) for i in range(1,25)]

    X_dict = dict()
    Y_dict = dict()

    for img_id in img_ids:

        img_m = normalize(tiff.imread('./data/mband/{}.tif'.format(img_id)).transpose([1, 2, 0]))
        mask = tiff.imread('./data/gt_mband/{}.tif'.format(img_id)).transpose([1, 2, 0]) / 255
        X_dict[img_id] = img_m
        Y_dict[img_id] = mask 

    for count in range(1,n_patches):
        
        if not os.path.exists(PROCESSED_DATA_PATH+'/{}'.format(count)):
            os.mkdir(PROCESSED_DATA_PATH+"/{}".format(count))
        save_path_img  = PROCESSED_DATA_PATH+'/{}/img.npy'.format(count)
        save_path_mask = PROCESSED_DATA_PATH+'/{}/mask.npy'.format(count)
        img_id = random.sample(X_dict.keys(),1)[0]
        img  = X_dict[img_id]
        mask = Y_dict[img_id]
        img_patch,mask_patch = get_rand_patch(img,mask,sz)

        np.save(save_path_img,img_patch)
        np.save(save_path_mask,mask_patch)









