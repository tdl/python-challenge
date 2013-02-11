from PIL import Image

im = Image.open("C:/flipme.jpg")

imHor = im.transpose(Image.FLIP_LEFT_RIGHT)
imHor.save("C:/flipLR.jpg")

imVer = im.transpose(Image.FLIP_TOP_BOTTOM)
imVer.save("C:/flipTB.jpg")

imRot = im.transpose(Image.ROTATE_180)
imRot.save("C:/flip_rot.jpg")

imRot90 = im.transpose(Image.ROTATE_90)
imRot90.save("C:/flip_rot90.jpg")

imRot270 = im.transpose(Image.ROTATE_270)
imRot270.save("C:/flip_rot270.jpg")

