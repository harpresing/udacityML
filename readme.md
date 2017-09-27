# Intro to Machine learning

## Supervised Classification

Training ML algorithms by experience, i.e. by providing various scenarios and the correct decision to take in each scenario, the algorithm is trainied so that it can make a correct or in a more accurate sense, a fair estimate of what should the answer be (or what needs to be done).

The **features** of a new scenario are used to determine the prediction by a supervised learning algorithm.

Examples where supervised algorithms can be used-

+ From an album of tagged photos, recognize a face. (Facebook)
+ Given someone's music choices and a bunch of features of that music (genre, tempo etc), recommend a song. (Netflix, Spotify)

Examples of Unsupervised learning

+ Spotting a weird looking bank transaction and flagging it as fraud.
+ Clustering bank customers based on their spending habits.

### Features and Label

+ Any given input is broken down into **features**, for instance, an input song could have features such as genre, tempo, gender, language etc.
+ Typically, our brain would **label** or categorise the song as liked or disliked.

A very simplified ML problem can be tackled by using a 2D `scatter plot` when there are two features and a data point represents a possible state of the system. Once known data points have been plotted on a Scatter plot, the job of machine learning is to asertain a **label** for a new data point that hasn't been seen before (`prediction`).
