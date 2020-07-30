import forgery_detect

"""
Main Code
"""

# example
image_file = input("Enter image file name:")

forgery_detect.detect('../test_images/', image_file, '../output_images/', blockSize=32)
