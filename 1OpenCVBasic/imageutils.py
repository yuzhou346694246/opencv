import matplotlib.pyplot as plt
import cv2

def imshow(opencv_img, engine='matplotlib'):
    if engine == 'matplotlib':
        img = cv2.cvtColor(opencv_img, cv2.COLOR_BGR2RGB)
        plt.imshow(img)
        plt.xticks([]),plt.yticks([])
        plt.show()

    if engine == 'opencv':
        cv2.imshow(engine,opencv_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
