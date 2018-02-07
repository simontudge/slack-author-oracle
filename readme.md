# Guess the slack author

This project was completed mostly as an end of class excersise for the [introduction to machine learning](https://eu.udacity.com/course/intro-to-machine-learning--ud120) course on udacity.

The series of scripts attemts to guess the author of a slack post, based only on the metadata and the contents of that post.

For context slack is a messaging app, popular with developers and teams.

It is possible to download the entire archive of a team from slack in json format. In order to run this software you will need to download a slack archive in this format. I did this with my team, but the archive is not included here because it contains comercially sensitive information.

Of course the author of the message is visible from the post, so the software is not useful, instead it is intended as a fun educational tool. Written mostly as a proof of concept.

I do this here and try to build an algorithm that guesses the author of the post.
It does this with a random forest classifier, using both message metadata and the conents of the message.

Firstly it filters down the meassages to only those users of interest. It then collects some meta-data of the message, such as the time of day, the length of the message, the average word length and the channel in which this was posted.

The notebook: summary/summary.ipynb summarises some of this metadata. It's a series of descriptive statistics which acts as a feasability study of how probable a machinelearning approach is to work.

It also looks at all of the text of the data and counts the word frequency useage in each document. It performs a principle component analysis to reduce the dimentionality of the word frequency table.

Finally, it runs the random forest classifier on the meta-data and the word data and guesses who was the author. It gets it right about 65% of the time. It may be possible to get this higher by messing with the features or settings, or changing the classifier.

Run the whole thing with `./main.sh 25` where here 25 is the number of PCAs to include. The order of the commands in that file should tell you about the logic of the algorithm. You can potentially change other settings inside each of these files.

Try to beat the score of around 65%.

The file ./code/pre_process.py is the file to fidle with to change what is included. Here you can set which authors to include in you analysis and which chanels to include. The file ./code/add_features.py has a list of features that are included. You can adapt this file to add or remove features and write custom features.

The file .notes.txt has more detailed notes on what each script is doing and what the outputs should look like.

Note that these set of scripts are in no-way meant to demostrate good coding standards. Most of the settings are hard coded, there are no tests, and little in the way of error checking or adaptibility.