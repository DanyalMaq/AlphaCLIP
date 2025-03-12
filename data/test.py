import pandas as pd
import numpy as np
import os
import shutil
import matplotlib.pyplot as plt

images_folder = "/mnt/DGXUserData/dxm060/Zach_Analysis/petlymph_image_data/final_2.5d_images_and_labels/output_coronal_images_v2"
labels_folder = "/mnt/DGXUserData/dxm060/Zach_Analysis/petlymph_image_data/final_2.5d_images_and_labels/output_coronal_labels_v2"
train_folder = "/mnt/DGXUserData/dxm060/Zach_Analysis/uw_lymphoma_pet_3d/dataframes/training.xlsx"
val_folder = "/mnt/DGXUserData/dxm060/Zach_Analysis/uw_lymphoma_pet_3d/dataframes/validation.xlsx"
test_folder = "/mnt/DGXUserData/dxm060/Zach_Analysis/uw_lymphoma_pet_3d/dataframes/testing.xlsx"
heap = "./heap"

if os.path.exists(heap):
    shutil.rmtree(heap)
os.makedirs(heap)

df = pd.read_excel(train_folder)
df = df.sort_values(by="label_name")
df.set_index("label_name", inplace=True)

# for i, (k, v) in enumerate(df.iterrows()):
#     v['label_name']
#     if i == 5: break

# for i, image in enumerate(sorted(os.listdir(labels_folder))):
#     image = os.path.join(labels_folder, image)
#     img = plt.imread(image)
#     print(img.sum())
#     shutil.copy(image, heap)
#     if i == 10: break

for i, ((k, v), image) in enumerate(zip(df.iterrows(), sorted(os.listdir(images_folder)))):

    pet_scan_data_nifti = load_nifti_image(nifti)
    mip_image_nifti = create_mip(pet_scan_data_nifti, ax=ax)
    save_image_as_jpeg(mip_image_nifti, 'nifti.jpeg', rot=rot)
    print("MIP saved as nifti.jpeg")