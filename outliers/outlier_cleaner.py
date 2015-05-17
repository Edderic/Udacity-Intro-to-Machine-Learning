#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error)
    """

    diff = predictions - net_worths
    diff_squared = diff*diff
    indices_diff = {}
    for index in range(0,len(predictions)):
        indices_diff[str(index)] = diff_squared[index]

    sorted_keys = sorted(indices_diff, key=indices_diff.get)

    cleaned_data = []
    count = 0
    for key in sorted_keys:
        if count < 81:
            age = ages[int(key)]
            net_worth = net_worths[int(key)]
            error = net_worth - predictions[int(key)]
            error = error * error
            cleaned_data.append((age, net_worth, error))
            count += 1

    ### your code goes here

    return cleaned_data

