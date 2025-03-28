# Aircraft Accident Aanalysis
**Author:** [David Mburu](www.linkedin.com/in/david-g-mburu-b1268a1b7) 


## Overview

This project is an anlysis of airplane accidents with the goal of identifying the lowest risk aircraft and recommend them for purchase to a company looking to get into the aviation industry. I used a dataset detailing aircraft accidents in the United States to perform my analysis. I checked for airplane makes and models that are involved in a lot of accidents in the dataset in order to view the fatalities, aircraft damage versus survivals and minor injuries. This helped me to filter down to three makes and nine models with two types of engines that showed the best results.


## Business Problem

The company wants to diversify its portfolio and has decided to venture into aviation. However, they know nothing about aircraft and have sought my expertise to guide them in making a decision to purchase low risk aircraft. 

Some analysis questions I considered were which aircraft are most involved in accidents and thereby filter from the best of them.

This is because aircraft types that have had too few accidents do not have enough data to analyse to assess their viability.


## Data Understanding and Analysis

### Data
I used this [Aviation Accident Dataset](https://www.kaggle.com/datasets/khsamaha/aviation-accident-database-synopses) from Kaggle to perform analysis. 

The data represents total aircraft accidents in the United States and international waters in the past 50 years. Some variables in the dataset include the **category of aircraft**, **aircraft model**,**accident date**,**Weather conditions**,**types of injuries sustained** among others.

My target variables are **aircraft categories** specifically airplanes since that is what the company wants to purchase, **model**, **make**, **injuries** and **aircraft damage**

All these variables are categorical except for the injuries which are numerical.

### Methods

I performed dropping and imputing for any null values in the dataset as well as replacing for extraneous data. I also converted all columns into the same data type to help in easy plotting and visualization.


### Results

Boeing, Lockheed and Mcdonnell Douglas stand out as less risky during accidents
![Accidents by Aircraft Make](Images/Accidents%20by%20Aircraft%20Make.png)


Amonge the aircraft makes these models stand out as the safest:
![Accidents by Aircraft Model](Images/Accidents%20by%20Aircraft%20Model.png)


Turbo jet and Turbo Fan engines are the safest during accidents as they contain their explosions hence less damage to aircraft
![Aircraft damage by Engine Type](Images/Aircraft%20Damage%20by%20Engine%20Type.png)



## Conclusion

The analysis yields three recommendations resulting in 11 options for the company to choose from when purchasing airplanes:

1. Make:
    - Boeing
    - Lockheed
    - Mcdonnell Douglas

2. Model:
    - Boeing
        - 747-200
        - 737-300
        - 727
    - Lockheed
        - L-1011
        - L-1011-385-3
        - L-1011-385
    - Mcdonnell Douglas
        - MD-88
        - DC-10-30
        - DC-9-51.

3. Engine Type:
    - Turbo Fan
    - Turbo Jet


## Next Steps

From the 11 options the analysis yields, one can now make further filtering based on their specific needs.

I could work on a machine learning model that could take in more variables than those in the datset to give a better recommendation on safe aircraft.


## For More Information

See the full analysis on the [jupyter notebook](aircraft-accident-analysis.ipynb)

Reach out to me on [LinkedIn](www.linkedin.com/in/david-g-mburu-b1268a1b7) or shoot me an [Email](mailto:daveygmbur@gmail.com)

