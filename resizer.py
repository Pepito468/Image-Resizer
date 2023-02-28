import argparse
from PIL import Image

#Terminal Arguments
arguments = argparse.ArgumentParser(description='Resize an image')
arguments.add_argument('Image_Name', type=str, help='Name of the input image')
arguments.add_argument('NewImage_Height', type=str, help='New height')
arguments.add_argument('NewImage_Width', type=str, help='New width')
args = arguments.parse_args()

try:
    args.NewImage_Height=int(args.NewImage_Height)
    args.NewImage_Width=int(args.NewImage_Width)

    #Input
    input_image = Image.open(args.Image_Name)

    #Resize
    output_image = input_image.resize((args.NewImage_Width, args.NewImage_Height))

    #Save
    output_image.save('NEW_' + args.Image_Name)
except ValueError:
    print("Invalid dimensions")
except FileNotFoundError:
    print("No such image")
