# Computer_Vision_Project
## What does Project Contain and what are the requirements 
### Data Preparation
    1. We need A large amount of image dataset
    2. We need to lern How Can we fetch these data and increase our dataset size so that we can Have a lots of data
    3. Then We need to split them into train and Validation data
    4. We can Use Data Augmentation and make a custom Function through which each Image goes and it creates more data
### Model Preparation
    1. We need to first use Feature extraction to bring one Pretrained Model
    2. Then We need to prepare a small model of ours and fine tune the prefetched model 
    3. Then we need to compile it and do lots of experiment on the model
### Creating Callbacks 
    1. We can have 3  of the callbacks in our model
    2. Then add them in our fitting
### Function to convert all the image into the desireed form as required by the model
    1. Most probably I need to convert it into shape of (256,256,3)
    2. And as we are working with batches So i need to convert them using `expand_dims` 
### Now i have to prepare a function which Accept any Image of that kind and Gives The prediction of it with the Probability also
