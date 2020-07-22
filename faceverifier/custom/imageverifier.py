from keras_facenet import FaceNet

embedder = FaceNet()

# image is the table saveed image
#uploadimage is api's uploaded image
def verifyImage(image, uploadedimage):
    return True