#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    from operator import itemgetter
    def calculate_error(x,y): #<-- function to calculate error given a single prediction and an actual value
        z = x-y
        return z**2
    errors = map(calculate_error, predictions, net_worths) #<-- apply the calculate error function to all the points
    data = zip(ages, net_worths,errors) #<--- combine the data into a list of tuples
    data.sort(key=itemgetter(2), reverse=True) #<-- sort the data from the biggest error to the smallest
    to_remove = int(round(len(predictions)*0.1)) #<-- calculate the 10% of the total data
    del data[0:to_remove+1] #<-- remove the top 10% of the data

    return data
