# Import datasets, classifiers and performance metrics
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split


class MnistCustomDigits:
    def run(self):
        import matplotlib.pyplot as plt

        # The digits dataset
        digits = datasets.load_digits()

        # The data that we are interested in is made of 8x8 images of digits, let's
        # have a look at the first 4 images, stored in the `images` attribute of the
        # dataset.  If we were working from image files, we could load them using
        # matplotlib.pyplot.imread.  Note that each image must have the same size. For these
        # images, we know which digit they represent: it is given in the 'target' of
        # the dataset.
        _, axes = plt.subplots(2, 4)
        images_and_labels = list(zip(digits.images, digits.target))
        for ax, (image, label) in zip(axes[0, :], images_and_labels[:4]):
            ax.set_axis_off()
            ax.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
            ax.set_title('Training: %i' % label)

        # In order to apply a classifier on this data, we need to flatten the image, 
        # to turn the data in a (samples, feature) matrix:
        n_samples = len(digits.images)
        data = digits.images.reshape((n_samples, -1))

        # Create a classifier: a support vector classifier
        classifier = svm.SVC(gamma=0.001)

        # Split data into train and test subsets
        pictures_train, pictures_test, labels_train, labels_test = train_test_split(
            data, digits.target, train_size=0.8, shuffle=False)
        
        # initialize test subsets with images of digits from digits_test folder
        pictures_test, labels_test = self.load_custom_test_digits()
        
        print(f'pictures_train[{ len(pictures_train[0]) }] = { pictures_train }')
        print(f'pictures_test[{ len(pictures_test[0]) }] = { pictures_test }')
        print(f'labels_train = { labels_train }')
        print(f'labels_test = { labels_test }')
        
        # We learn the digits on the first half of the digits
        classifier.fit(pictures_train, labels_train)

        # Now predict the value of the digit on the second half:
        predicted = classifier.predict(pictures_test)

        images_and_predictions = list(zip(digits.images[n_samples // 2:], predicted))
        for ax, (image, prediction) in zip(axes[1, :], images_and_predictions[:4]):
            ax.set_axis_off()
            ax.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
            ax.set_title('Prediction: %i' % prediction)

        print("Classification report for classifier %s:\n%s\n"
            % (classifier, metrics.classification_report(labels_test, predicted)))
        
        disp = metrics.plot_confusion_matrix(classifier, pictures_test, 
                                            labels_test)
        
        disp.figure_.suptitle("Confusion Matrix")
        print("Confusion matrix:\n%s" % disp.confusion_matrix)

        plt.show()
    

    # Load digits for test
    def load_custom_test_digits(self):
        import os
        import numpy as np 
        from PIL import Image, ImageOps
        from scipy.ndimage.measurements import center_of_mass

        os.chdir('../computer_vision/MNIST/digits_test')
        
        # Create empty numpy array for 10 digits with size 8x8px
        pictures_test = np.empty((10, 64))

        # Create an empty list for labels of the pictures
        labels_test = []

        indexImgFlatten = 0

        # Read the png images and flatten them into array of pixels 
        for f in os.listdir('.'): 
            if f.endswith('.png'): 
                img = Image.open(f)

                # convert image to single channel and invert
                #inverted_img = ImageOps.invert(img.convert('L'))
                
                # crop image to match the bounding box
                #cropped_img = inverted_img.crop(inverted_img.getbbox())
                cropped_img = img.crop(img.getbbox())

                # scale image to fit in 8x8px box
                cropped_img.thumbnail((8, 8))
                
                # convert image to numpy array
                np_img = np.array(cropped_img)
                print(f'np_img[{ np_img.shape }] = { np_img }')
                mass_center = center_of_mass(np_img)

                # create final 28x28 image and paste centered digit
                final_img = Image.new(mode='L', size=(8, 8))
                final_img = ImageOps.invert(final_img.convert('L'))
                
                point = (4 - int(round(mass_center[1])), 4 - int((round(mass_center[0]))))
                final_img.paste(cropped_img, point)

                final_img.show()

                # convert image to numpy array and reshape it
                result = np.array(final_img).reshape((64, ))
                
                print(f'result[{ indexImgFlatten }] = { result }')
                
                pictures_test[indexImgFlatten] = result

                indexImgFlatten += 1
        
        # Define labels_test
        for i in range(10): 
            labels_test.append(i)

        #pictures_test = np.asarray(pictures_test)
        labels_test = np.asarray(labels_test)

        return pictures_test, labels_test