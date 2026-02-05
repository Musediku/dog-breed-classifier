#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    
    # Print summary statistics
    print("\n\n*** Results Summary for CNN Model Architecture:", model.upper(), "***")
    print("{:20}: {:3d}".format("Total Images", results_stats_dic['n_images']))
    print("{:20}: {:3d}".format("Total Dog Images", results_stats_dic['n_dogs_img']))
    print("{:20}: {:3d}".format("Total Not-a-Dog Images", results_stats_dic['n_notdogs_img']))

    # Print percentages
    print("\n*** Percentage Statistics ***")
    for key in results_stats_dic:
        if key.startswith('pct'):
            print("{:20}: {:.2f}%".format(key, results_stats_dic[key]))

    # Print incorrectly classified dogs, if requested
    if print_incorrect_dogs:
        print("\n*** Incorrect Dog/Not Dog Assignments ***")
        for filename, values in results_dic.items():
            # Check if pet label and classifier disagree on dog/not-dog
            if values[3] != values[4]:
                print(f"Image: {filename}  Pet Label: {values[0]}  Classifier Label: {values[1]}")

    # Print incorrectly classified dog breeds, if requested
    if print_incorrect_breed:
        print("\n*** Incorrect Dog Breed Assignments ***")
        for filename, values in results_dic.items():
            # Only consider images that are actually dogs and classified as dogs
            if values[3] == 1 and values[4] == 1 and values[2] == 0:
                print(f"Image: {filename}  Pet Label: {values[0]}  Classifier Label: {values[1]}")

                
