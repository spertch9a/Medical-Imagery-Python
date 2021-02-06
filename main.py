# Starting off with imports
# Hoping I can keep up with commenting and remembering every bit of code
import imageio as image
import matplotlib.pyplot as plt
import numpy as np

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


# Read in each 2D image
im1 = imageio.imread('chest-220.dcm')
im2 = imageio.imread('chest-221.dcm')
im1 = image.imread('chest-220.dcm')
im2 = image.imread('chest-221.dcm')
im3 = image.imread('chest-222.dcm')

# Stack images into a volume
vol = np.stack([im1, im2, im3], axis=0)
print('Volume dimensions:', vol.shape)

#loading a stack

# Load the "tcia-chest-ct" directory
vol = image.volread("tcia-chest-ct")

# Print image attributes
print('Available metadata:', vol.meta.keys())
print('Shape of image array:', vol.shape)

"""
Field of view
The amount of physical space covered by an image is its field of view, which is calculated from two properties:

Array shape, the number of data elements on each axis. Can be accessed with the shape attribute.
Sampling resolution, the amount of physical space covered by each pixel. Sometimes available in metadata (e.g., meta['sampling']).
For this exercise, multiply the array shape and sampling resolution along each axis to calculate the field of view of vol. All values are in millimeters.
"""
#for this i used 
vol.shape
vol.meta['sampling']



#generate subplots : 
# Initialize figure and axes grid
fig, axes = plt.subplots(nrows= 2, ncols = 1)

# Draw an image on each subplot
axes[0].imshow(im1, cmap = "gray")
axes[1].imshow(im2, cmap = "gray")

# Remove ticks/labels and render
axes[0].axis('off')
axes[1].axis('off')

plt.show()

#slice 3d images 
# Plot the images on a subplots array 
fig, axes = plt.subplots(nrows=1, ncols=4)

# Loop through subplots and draw image
for ii in range(4):
    im = vol[ii * 40, :, :]
    axes[ii].imshow(im, cmap='gray')
    axes[ii].axis('off')

# Render the figure
plt.show()

#plot other views
# Select frame from "vol"
im1 = vol[:, 256, :]
im2 = vol[:, :, 256]

# Compute aspect ratios
d0, d1, d2 = vol.meta['sampling']
asp1 = d0 / d2
asp2 = d0 / d1

# Plot the images on a subplots array 
fig, axes = plt.subplots(nrows=2, ncols=1)
axes[0].imshow(im1, cmap='gray', aspect=asp1)
axes[1].imshow(im2, cmap='gray', aspect=asp2)
plt.show()