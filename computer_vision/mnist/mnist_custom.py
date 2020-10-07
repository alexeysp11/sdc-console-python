import os
import sys

# Standard scientific Python imports
import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
from PIL import Image

# Import datasets, classifiers and performance metrics
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split


class MnistCustomDigits:
    def run(self):
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
        #pictures_test, lables_test = 
        self.load_custom_test_digits()

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
        """
        # incorrect path to the image! 
        image = Image.open("0.png")
        image.show()
        """
        
        os.chdir('../computer_vision/MNIST/digits_test')
        
        lables_test = []
        
        for f in os.listdir('.'): 
            if f.endswith('.png'): 
                i = Image.open(f)

                """
                # Define lables_test
                fn, fext = os.path.splitext(f)
                lables_test.append(i)
                """

                i.show()
        
        
        for i in range(10): 
            lables_test.append(i)

        #return pictures_test, lables_test