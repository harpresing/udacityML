from sklearn.naive_bayes import GaussianNB


def classify(features_train, labels_train):
    classifier = GaussianNB()
    classifier.fit(features_train, labels_train)
    return classifier