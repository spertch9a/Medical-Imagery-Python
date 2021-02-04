# Starting off with imports
# Hoping I can keep up with commenting and remembering every bit of code
import imageio as image
import matplotlib.pyplot as plt


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


# Draw the image in grayscale
plt.imshow(im, cmap="gray")

# Render the image
plt.show()
# //custom
# Draw the image with greater contrast
plt.imshow(im, cmap='gray', vmin=-200, vmax=200)

# turn off the axis and ticks
plt.axis('off')

# Render the image
plt.show()
