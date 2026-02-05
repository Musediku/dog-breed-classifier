#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                 
# REVISED DATE: 
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. We recommend reading all the
#          dog names in dognames.txt into a dictionary where the 'key' is the 
#          dog name (from dognames.txt) and the 'value' is one. If a label is 
#          found to exist within this dictionary of dog names then the label 
#          is of-a-dog, otherwise the label isn't of a dog. Alternatively one 
#          could also read all the dog names into a list and then if the label
#          is found to exist within this list - the label is of-a-dog, otherwise
#          the label isn't of a dog. 
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog 
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           whether or not the pet image label is of-a-dog as the item at index
#           3 of the list and whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list. Note we recommend setting the values
#           at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the 
#           label isn't a dog.
#
##
# TODO 4: Define adjust_results4_isadog function below, specifically replace the None
#       below by the function definition of the adjust_results4_isadog function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match.
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List: 
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int)  where 1 = match, 0 = no match
                NEW:
                 index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog, 0 = not
                 index 4 = 1/0 (int)  where 1 = classifier labels 'as-a' dog, 0 = not
     dogfile - text file containing all dog names (one per line, lowercase)
    Returns:
           None - results_dic is mutable
    """
    
    # Step 1: Load all dog names into a set for quick lookup
    dog_names = set()
    with open(dogfile, 'r') as f:
        for line in f:
            name = line.strip().lower()
            if name != "":
                dog_names.add(name)
    
    # Step 2: Iterate through results_dic and determine dog status
    for key, value in results_dic.items():
        pet_label = value[0].lower().strip()
        classifier_label = value[1].lower().strip()
        
        # Pet image is a dog?
        if pet_label in dog_names:
            is_pet_dog = 1
        else:
            is_pet_dog = 0
        
        # Classifier labels as a dog? Check if any label in classifier (split by commas) is a dog
        classifier_dog = 0
        for label in classifier_label.split(','):
            label = label.strip()
            if label in dog_names:
                classifier_dog = 1
                break
        
        # Append results to results_dic
        value.append(is_pet_dog)      # index 3
        value.append(classifier_dog)  # index 4
