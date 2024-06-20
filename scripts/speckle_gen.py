import numpy as np
import matplotlib.pyplot as plt

im_size = (500, 500)
feat_size = 10
spacing = 5
noise_size = 10

# Create feature mask
i, j = np.meshgrid(np.arange(feat_size), np.arange(feat_size))
feature = np.sqrt((i-feat_size/2)**2 + (j-feat_size/2)**2) < feat_size/2 -1

# Create grid points
grid_size = tuple(int(x / (feat_size + spacing)) for x in im_size)
grid_points = np.meshgrid(
    *(np.linspace(spacing, im_size[i]-feat_size-spacing, grid_size[i]) for i in range(2))
)
grid_points = np.array(
    list(zip(*(gp.round().flat for gp in grid_points)))
)
grid_points += np.random.uniform(
    -noise_size/2, 
    noise_size/2, 
    grid_size[0]*grid_size[1]*2
).reshape(grid_size[0]*grid_size[1], 2)
grid_points = grid_points.astype(int)


# Insert masks into image at grid points
image = np.zeros(im_size)
for gp in grid_points:
    image[gp[0]:gp[0]+feat_size, gp[1]:gp[1]+feat_size] = feature


plt.imshow(image, cmap='grey')
plt.axis('off')
plt.savefig('blah.png')