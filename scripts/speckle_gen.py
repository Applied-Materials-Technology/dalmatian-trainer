import numpy as np
#import matplotlib.pyplot as plt
import argparse
from math import sqrt, pi
import scipy as sp
from PIL import Image
# inputs are:
# image dimensions
# feature size
# black/white balance
# amount of blur
# filename
# file bits


def specklegen (Filename: str,XDim:int,YDim:int,feat_size:int,BWBal:float,Gaussian_value:float,reverse:bool,is16:bool, noise:int)->None:
#filename = file to save to
#XDim = X Dimensions of output
#YDim = Y Dimensions of output
#feat_size = size of dots
#BWBal = ideal balck-white balance - doesn't count for dot overlap at high values
#reverse = do we flip black and white
#is16 = do we save in 16-bit instead of 8-bit
    feature_area = pi*(feat_size/2)**2
    square_area = feature_area/BWBal
    square_size = sqrt(square_area)
    spacing = square_size-feat_size
    print (spacing)
    im_size = (XDim, YDim)
    noise_size = noise
    
    
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
    #so we need to create larger than the image and them trim to avoid issuesd with calculations
    #alternative way of doing it 
    #for every pixel on the image, calculated the distance to all the dots. if it is within feature size of any of them the colour the point
    image = np.zeros(im_size)
    grid_points = grid_points.transpose()
    for i in range(0,im_size[0]):
        for j in range(0,im_size[1]):
            if np.any(np.sqrt(((i-grid_points[0] - feat_size/2)**2 + (j-grid_points[1]-feat_size/2)**2)) < (feat_size/2+0.5)):
                image[i][j] = 1  
    if not reverse:
        image = 1-image
    if noise>0:
        image = sp.ndimage.gaussian_filter(image,Gaussian_value)
    if is16:
        image =image*np.iinfo('uint16').max
        image = image.astype('uint16')
    else:
        image = image*np.iinfo('uint8').max
        image = image.astype('uint8')
    im = Image.fromarray(image)
    
    #plt.axis('off')
    try:
       im.save(Filename)
    except Exception as e:
        print("invalid filename")
        raise e
    
    
    #try:
    #   plt.savefig(Filename)
    #except Exception as e:
    #    print("invalid filename")
    #    raise e
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            prog = 'Speckle pattern generator',
            description = 'This creates a speckle pattern',
            epilog = '')
    parser.add_argument('filename', type = str, help = "the name of the file to save to - must include extension as Pillow uses this to idetify file types")
    parser.add_argument('XSize', type = int, help = "The x dimension of the image, in pixels")
    parser.add_argument('YSize', type = int, help = "The y dimension of the image, in pixels")
    parser.add_argument('-s',  '--size', type = int, default = 4, help = "The size of the features in pixels")
    parser.add_argument('-b', '--blur', type = float, default = 0.6, help = "The scale of the gaussian blur (measurement is the standard deviation of the gaussian, in pixels)")
    parser.add_argument('-w', '--balance', type = float, default = 0.25, help = "The faction of the image that is occupied by features")
    parser.add_argument('-n', '--noise', type = int, default = 3, help = "The maximum puturbation of the features, in pixels")
    parser.add_argument('-i', '--bits', action = 'store_true', help = "Is the image saved with 16-bit depth instead of 8-bit")
    parser.add_argument('-k', '--background', action = 'store_true', help = "Flip the image to white features on a black background")
    args = parser.parse_args()
    print(args)
    specklegen (args.filename,args.XSize,args.YSize,args.size,args.balance,args.blur,args.background,args.bits,args.noise)
