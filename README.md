# noughts-and-crosses

Projects for playing noughts and crosses. The repository contains a data file of all 958 possible noughts and crosses games 
(sourced from http://archive.ics.uci.edu/ml/datasets/Tic-Tac-Toe+Endgame), where X is assumed to have played first,
and "positive" is a win for X

The script "noughts_and_crosses_classification.py" uses machine learning to classify the games, and can be run via:

python noughts_and_crosses_classification.py

It is trained on a subset of the data, and then predicts whether or not a game is a win for X.
It uses a variety of scikit-learn routines (LinearSVC, KNearest Neighbours, SVC, and BaggingClassifier), and outputs
their accuracy (the ratio of correct predictions to total predictions).


The script "noughts_and_crosses_analysis.py" is a simple analysis script, run via:

python noughts_and_crosses_analysis.py

This takes the games where X wins, and shows the distribution of Xs, Os and blanks on each square. 
The distributions are shown as pie charts. 

