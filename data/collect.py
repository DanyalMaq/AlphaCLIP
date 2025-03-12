import pandas as pd
import numpy as np
import os
import shutil
import matplotlib.pyplot as plt
import json
from utils import *

images_folder = "/mnt/DGXUserData/dxm060/Zach_Analysis/petlymph_image_data/final_2.5d_images_and_labels/output_coronal_images_v2"
labels_folder = "/mnt/DGXUserData/dxm060/Zach_Analysis/petlymph_image_data/final_2.5d_images_and_labels/output_coronal_labels_v2"
train_folder = "/mnt/DGXUserData/dxm060/Zach_Analysis/uw_lymphoma_pet_3d/dataframes/training.xlsx"
val_folder = "/mnt/DGXUserData/dxm060/Zach_Analysis/uw_lymphoma_pet_3d/dataframes/validation.xlsx"
test_folder = "/mnt/DGXUserData/dxm060/Zach_Analysis/uw_lymphoma_pet_3d/dataframes/testing.xlsx"
heap = "./heap"

# Sample DataFrame (Replace this with your actual DataFrame)
df = pd.DataFrame({
    'label_name': ['997bb945-628d-4724-b370-b84de974a19f', 'another-id'],
    'image': ['part-000001/997bb945-628d-4724-b370-b84de974a19f.jpg', 'part-000001/another-id.jpg'],
    'mask': ['part-000001/997bb945-628d-4724-b370-b84de974a19f_mask.jpg', 'part-000001/another-id_mask.jpg'],
    'label_text': ['A scenic view of a ruined city at sunset.', 'A futuristic robot standing in a neon-lit alley.']
})

df['image'] = df['image'].str.replace('/mnt/Bradshaw', '/mnt/PURENFS/Bradshaw', regex=False)
df['label'] = df['label'].str.replace('/mnt/Bradshaw', '/mnt/PURENFS/Bradshaw', regex=False)

# Convert DataFrame to the desired format
formatted_data = [
    {
        "id": str(index),
        "image": row['image'],
        "mask": row['label'],
        "conversations": [
            {
                "from": "human",
                "value": "Generate captions for this image"
            },
            {
                "from": "gpt",
                "value": row['report']
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
