import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
from PIL import 

def load_nifti_image(file_path):
    nifti_img = nib.load(file_path)
    img_data = nifti_img.get_fdata()
    print("Loading nifti data of shape: ", img_data.shape)
    print("Unique values", np.unique(img_data))
    print("Sum", np.sum(img_data))
    return img_data

def load_npy_image(file_path):
    img_data = np.load(file_path)[0].transpose(2, 1, 0)
    # for i in range(16):
    #     plt.imsave(f"temp/temp{i}.png",img_data[:, :, i])
    print("Loading npy data of shape: ", img_data.shape)
    return img_data

def create_mip(pet_scan_data, ax=2):
    # print(np/.unique(pet_scan_data))
    mip_image = np.max(pet_scan_data, axis=ax)  # Adjust the axis as needed
    return mip_image

def save_image_as_jpeg(image_data, filename, rot=None):
    # Normalize the image to the range 0-255
    if rot is not None:
        image_data = np.rot90(image_data, k=rot)
    normalized_image = (image_data - np.min(image_data)) / (np.max(image_data)) * 255
    normalized_image = normalized_image.astype(np.uint8)
    # print("Unique values", np.unique(normalized_image))
    # print("Sum", np.sum(normalized_image))

    # Create a PIL Image and save it as JPEG
    img = Image.fromarray(normalized_image)
    img.save(filename)