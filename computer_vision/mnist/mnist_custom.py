# Import datasets, classifiers and performance metrics
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split


class MnistCustomDigits:
    def run(self):
        import matplotlib.pyplot as plt
        
        # Create a classifier: a support vector classifier
        classifier = svm.SVC(gamma=0.001)

        # initialize test subsets with images of digits from digits_test folder
        pixels_train, labels_train, train_imgs = self.load_digits('digits_8x8')

        # initialize test subsets with images of digits from digits_test folder
        pixels_test, labels_test, test_imgs = self.load_digits('zeros_8x8')
        
        # We learn the digits on the first half of the digits
        classifier.fit(pixels_train, labels_train)

        # Now predict the value of the digit on the second half:
        predicted = classifier.predict(pixels_test)

        _, axes = plt.subplots(2, 4)
        images_and_labels = list(zip(train_imgs[:len(train_imgs) // 2], labels_train))
        for ax, (image, label) in zip(axes[0, :], images_and_labels[:4]):
            ax.set_axis_off()
            ax.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
            ax.set_title('Training: %i' % label)
        
        images_and_predictions = list(zip(test_imgs[len(test_imgs) // 2:], predicted))
        for ax, (image, prediction) in zip(axes[1, :], images_and_predictions[:4]):
            ax.set_axis_off()
            ax.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
            ax.set_title('Prediction: %i' % prediction)

        print("Classification report for classifier %s:\n%s\n"
            % (classifier, metrics.classification_report(labels_test, predicted)))
        
        disp = metrics.plot_confusion_matrix(classifier, pixels_test, 
                                            labels_test)
        
        disp.figure_.suptitle("Confusion Matrix")
        print("Confusion matrix:\n%s" % disp.confusion_matrix)

        plt.show()
    

    # Load digits for test
    def load_digits(self, path):
        """
        Pass name of folder as path variable. 
        """

        import os
        import numpy as np 
        from PIL import Image, ImageOps
        from scipy.ndimage.measurements import center_of_mass

        # folders: digits_test, digits_8x8, zeros, zeros_8x8
        os.chdir('../computer_vision/MNIST/' + path)
        
        # Create empty numpy array for 10 digits with size 8x8px
        pixels = np.empty((10, 64))

        # Create an empty list for labels of the pictures
        labels = []
        imgs = []

        indexImgFlatten = 0

        # Read the png images and flatten them into array of pixels 
        for f in os.listdir('.'): 
            if f.endswith('.png'): 
                img = Image.open(f)
                imgs.append(img)

                # convert image to single channel and invert
                #inverted_img = ImageOps.invert(img.convert('L')) # inverted
                
                # crop image to match the bounding box
                #cropped_img = inverted_img.crop(inverted_img.getbbox()) # inverted
                cropped_img = img.crop(img.getbbox()) # non-inverted

                # scale image to fit in 8x8px box
                cropped_img.thumbnail((8, 8))
                
                # convert image to numpy array
                np_img = np.array(cropped_img)
                mass_center = center_of_mass(np_img)

                # create final 28x28 image and paste centered digit
                final_img = Image.new(mode='L', size=(8, 8))
                final_img = ImageOps.invert(final_img.convert('L')) # non-inverted

                point = (4 - int(round(mass_center[1])), 4 - int((round(mass_center[0]))))
                final_img.paste(cropped_img, point)

                #final_img.show()

                # convert image to numpy array and reshape it
                result = np.array(final_img).reshape((64, ))
                
                pixels[indexImgFlatten] = self.add_brightness(result)

                indexImgFlatten += 1
        
        # Define labels_test
        if path == 'digits_8x8': 
            for i in range(10): 
                labels.append(i)
        
        # if we use folder zeros_8x8:
        if path == 'zeros_8x8': 
            for i in range(len(pixels)):
                labels.append(0)
        
        
        #pictures_test = np.asarray(pictures_test)
        labels = np.asarray(labels)
        
        os.chdir('../../../console')
        
        return pixels, labels, imgs
    

    def add_brightness(self, np_img):
        # inverted images
        for index, px in enumerate(np_img): 
            if px > 55:
                np_img[index] = 255
        
        """
        # non-inverted images
        for index, px in enumerate(np_img): 
            if px < 200:
                np_img[index] = 0
        """
        
        return np_img
