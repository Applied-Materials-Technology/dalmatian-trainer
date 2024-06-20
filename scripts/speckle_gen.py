import numpy as np
import matplotlib.pyplot as plt
import argparse

# inputs are:
# image dimensions
# feature size
# black/white balance
# amount of blur
# filename
# file bits

def specklegen (Filename: str,XDim:int,YDim:int,feat_size:int,BWBal:float,Gaussian_value:float,reverse:bool,is16:bool)->None:
#filename = file to save to
#XDim = X Dimensions of output
#YDim = Y Dimensions of output
#feat_size = size of dots
#BWBal = ideal balck-white balance - doesn't count for dot overlap at high values
#reverse = do we flip black and white
#is16 = do we save in 16-bit instead of 8-bit
    im_size = (XDim, YDim)
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
    try:
       plt.savefig(Filename)
    except:
        print("invalid filename")
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            prog = 'Speckle pattern generator',
            description = 'This creates a speckle patter',
            epilog = '')
    parser.add_argument('filename', type = str)
    parser.add_argument('XSize', type = int)
    parser.add_argument('YSize', type = int)
    parser.add_argument('-s',  '--size', type = int, default = 10)
    parser.add_argument('-b', '--blur', type = float, default = 0.)
    parser.add_argument('-w', '--balance', type = float, default = 0.25)
    parser.add_argument('-i', '--bits', action = 'store_true')
    parser.add_argument('-k', '--background', action = 'store_true')
    args = parser.parse_args()
    print(args)
    specklegen (args.filename,args.XSize,args.YSize,args.size,args.balance,args.blur,args.background,args.bits)