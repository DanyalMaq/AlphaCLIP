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

df = pd.DataFrame({
    'label_name': ['997bb945-628d-4724-b370-b84de974a19f', 'another-id'],
    'image': ['part-000001/997bb945-628d-4724-b370-b84de974a19f.jpg', 'part-000001/another-id.jpg'],
    'mask': ['part-000001/997bb945-628d-4724-b370-b84de974a19f_mask.jpg', 'part-000001/another-id_mask.jpg'],
    'label_text': ['A scenic view of a ruined city at sunset.', 'A futuristic robot standing in a neon-lit alley.']
})

df = pd.read_excel(train_folder)
df = df.sort_values(by="label_name")
df.set_index("label_name", inplace=True)

df['image'] = df['iamge'].str.replace('/mnt/bradshaw', '/mnt/PURENFS/bradshaw', regex=False)

# Convert DataFrame to the desired format
formatted_data = [
    {
        "id": str(index),
        "image": row['image'],
        "mask": row['mask'],
        "conversations": [
            {
                "from": "human",
                "value": "Generate captions for this image"
            },
            {
                "from": "gpt",
                "value": row['label_text']
            }
        ]
    }
    for index, row in df.iterrows()
]

# Convert to JSON string
json_output = json.dumps(formatted_data, indent=2)

# Save to a file (optional)
with open("formatted_data.json", "w") as f:
    f.write(json_output)

# Print the output
print(json_output)

for i, ((k, v), image) in enumerate(zip(df.iterrows(), sorted(os.listdir(images_folder)))):

    pet_scan_data_nifti = load_nifti_image(nifti)
    mip_image_nifti = create_mip(pet_scan_data_nifti, ax=ax)
    save_image_as_jpeg(mip_image_nifti, 'nifti.jpeg', rot=rot)
    print("MIP saved as nifti.jpeg")