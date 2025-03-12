import numpy as np 
from PIL import Image

with Image.open('images/birds.jpg') as img:
    img_arr = np.array(img)
def flip_image(img_ar):
    """flip the image"""
    #flip the image vetically and save
    flipped_vertically = np.flipud(img_arr)
    img_ver=Image.fromarray(flipped_vertically)
    img_ver.save("Vertical.jpeg")
    #flip the image horizontally and save
    flipped_horizontally=np.fliplr(img_arr)
    img_hor=Image.fromarray(flipped_horizontally)
    img_hor.save("Horizontal.jpeg")

def add_noise(img_ar):
    """Add noise to the image"""
    mean=0
    std=20
    noise=np.random.normal(mean,std, img_ar.shape)
    noisy_img=noise+img_ar
    noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)
    # Convert back to an image
    noisy_image = Image.fromarray(noisy_img)
    noisy_image.save("noisy_image.jpg")

def brighten_channel(img_ar):
    """Increase brighness of the channel"""
    increased_val=40
    img_ar[:,:,0]=np.clip(img_ar[:,:,0]+increased_val,0,255)
    brightened_img=Image.fromarray(img_ar)
    brightened_img.save("Brightened.jpeg")





def apply_mask(img_arr):
    width,height,_=img_arr.shape

    x,y=width//2,height//2
    mask_size=100

    x_s=x-mask_size//2
    y_s=y-mask_size//2
    x_e=x_s+mask_size
    y_e=y_s+mask_size

    img_arr[x_s:x_e,y_s:y_e]=[0,0,0]
    mask_image=Image.fromarray(img_arr)
    mask_image.save("Mask.jpeg")




    
flip_image(img_arr)
add_noise(img_arr)
brighten_channel(img_arr)
apply_mask(img_arr)
    




