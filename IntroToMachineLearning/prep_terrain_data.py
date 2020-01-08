import random


def makeTerrainData(n_points=1000):

    # seed the random class
    random.seed(42)

    # create three lists of 1000 random values 0.0 - 1.0
    grade = [random.random() for ii in range(0,n_points)]
    bumpy = [random.random() for ii in range(0,n_points)]
    error = [random.random() for ii in range(0,n_points)]

    # create a list of 1000 random values 0.0 - 1.0
    y = [round(grade[ii]*bumpy[ii]+0.3+0.1*error[ii]) for ii in range(0,n_points)]

    # if high grade or bumpy, set corresponding value in y to 1.0
    for ii in range(0, len(y)):
        if grade[ii]>0.8 or bumpy[ii]>0.8:
            y[ii] = 1.0

    # create list of lists containing corresponding grades and bumpy values
    X = [[gg, ss] for gg, ss in zip(grade, bumpy)]

    split = int(0.75*n_points)

    # get 750 values of grade/bumpy in a list
    X_train = X[0:split]

    # get 250 values of grade/bumpy in a list
    X_test  = X[split:]

    # get 750 values of grade/bumpy in a list
    y_train = y[0:split]

    # get 250 values of grade/bumpy in a list
    y_test  = y[split:]

    return X_train, y_train, X_test, y_test
