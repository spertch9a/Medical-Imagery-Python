# Starting off with imports
# Hoping I can keep up with commenting and remembering every bit of code
import imageio as image

# Load "chest-220.dcm"
im = image.imread("./data/tcia-chest-ct/chest-220.dcm")

# Print image attributes
print('Image type:', type(im))
print('Shape of image array:', im.shape)

# Print the available metadata fields
print(im.meta.keys())

# Print the available metadata fields
print(im.meta)

# printing the sex of the patient (accessing a metadata

print("Patient sex is : " + im.meta['PatientSex'])
