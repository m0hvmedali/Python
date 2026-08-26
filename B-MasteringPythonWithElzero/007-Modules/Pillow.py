from PIL import Image
print(dir(Image))
# open image
esraa = Image.open(r"C:\Users\moham\Documents\dev\Python\image.png")
# show image
esraa.show()
# crop image
esraa = esraa.crop((1500, 500, 1900, 900))
esraa.show()
# for more information please visit => :)
# https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
