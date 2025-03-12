import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
from PIL import Image

Caption_templates = [
            "Can you provide a caption consists of findings for this medical image?",
            "Describe the findings of the medical image you see.",
            "Please caption this medical scan with findings.",
            "What is the findings of this image?",
            "Describe this medical scan with findings.",
            "Please write a caption consists of findings for this image.",
            "Can you summarize with findings the images presented?",
            "Please caption this scan with findings.",
            "Please provide a caption consists of findings for this medical image.",
            "Can you provide a summary consists of findings of this radiograph?",
            "What are the findings presented in this medical scan?",
            "Please write a caption consists of findings for this scan.",
            "Can you provide a description consists of findings of this medical scan?",
            "Please caption this medical scan with findings.",
            "Can you provide a caption consists of findings for this medical scan?",
            "Please generate a medical report based on this image.",
            "Can you generate a diagnose report from this image.",
            "Could you analyze and provide a caption for the findings in this medical image?",
            "Please describe the observations depicted in this medical scan.",
            "Can you summarize the findings of this image in a caption?",
            "What are the significant findings in this medical image?",
            "Please provide a detailed caption outlining the findings of this image.",
            "Could you interpret and describe the findings shown in this medical scan?",
            "What conclusions can you draw from the observations in this image?",
            "Please write a descriptive caption based on the findings in this scan.",
            "What key findings can you identify from examining this medical image?",
            "Could you generate a detailed report based on the observations in this image?",
            "Can you provide a diagnosis based on the findings in this image?",
            "Please generate a comprehensive report summarizing the findings in this image.",
            "Caption the findings in this medical image?",
            "Describe the findings you see.",
            "Caption this medical scan's findings.",
            "What are the findings here?",
            "Describe these findings.",
            "Summarize the findings in these images.",
            "Caption this scan's findings.",
            "Provide a caption for this medical image's findings.",
            "Summarize the findings of this radiograph.",
            "What findings are presented in this scan?",
            "Describe this scan's findings.",
            "Generate a medical report based on this image.",
            "Can you provide a diagnosis based on this image?",
]

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