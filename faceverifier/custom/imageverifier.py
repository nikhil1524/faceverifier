from keras_facenet import FaceNet

embedder = FaceNet()

def verifyImage(image, uploadedimage):
    em1 = embedder.extract(image, threshold=0.95)
    em1 = em1[0]['embedding']
    em2 = embedder.extract(uploadedimage, threshold=0.95)
    if len(em2) > 1:
        print("More than one face detected")
        return False
    elif len(em2) < 1:
        print("No face detected")
        return False
    else:
        print("This is done good")
        em2 = em2[0]['embedding']
        distance = embedder.compute_distance(em1, em2)
        if distance < 0.32:
            return True
        else:
            return False
