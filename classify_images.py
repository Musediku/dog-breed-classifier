#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                 
# REVISED DATE: 
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier 

# TODO 3: Define classify_images function below, specifically replace the None
#       below by the function definition of the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 

def classify_images(images_dir, results_dic, model):
    for filename, value in results_dic.items():
        # Get the pet image label
        pet_label = value[0]

        # Classify the image using the specified model
        classifier_label = classifier(f"{images_dir}/{filename}", model)

        # Clean up the classifier label: lowercase and strip whitespace
        classifier_label = classifier_label.lower().strip()

        # Determine if pet label is in classifier label
        # Using 'in' to handle multiple names separated by commas
        match = 1 if pet_label in classifier_label else 0

        # Append classifier label and match result to the list in results_dic
        value.extend([classifier_label, match])