# ReviewSense - Back End Repository
This repository hosts the backend Python flask and Machine Learning for ReviewSense.

### License and Copyright

We are working and discussing the merits of several open-source license structures right now, so please stay tuned. Until a decision is made, however, everything found in this repository is owned by Dalton Senseman, John Maurer and Carrie West and cannot be reproduced, edited or distributed without our express written permission. 

### Abstract

In this senior project, we were tasked with developing a web-based solution that incorporates machine learning on a set of movie reviews to organize them by sentiment. The stakeholders of our project expressed frustrations with the lack of overall analytics for movie reviews provided by existing services. Our team examined the different potential models and decided to use a Naïve Bayes model for our approach. We gathered our data from two Kaggle datasets, one containing labelled data used to train our model, and the other containing unlabelled data to apply labels to using our trained model. Additionally, we established a back-end server with Python Flask to communicate to our SQLite database and send data using HTTP endpoints. This data is then displayed on a front-end website, built with the Angular framework. We present the resulting website as a minimum viable solution to our stakeholder's concerns.

### Back End Requirements
Our application was built with the following high-level requirements in mind:
* Build and train a custom non-library dependant algorithm to sentimentalize movie reviews.
* Store reveiws after being sentimetalized for querying from the front end to then display
* Have a API between the front end and the backend to handle requests.

### Constraints
Our application was built under the following constraints:
* The project must be completed within 32 weeks.
* The machine learning algorithm must be implemented without the use of external libraries.
* The project must be hosted online.
* Due to inaccessability of review APIs, the project utilizes two Kaggle datasets for the sentiment analysis.


## Front End Documentation

You can find the front end documentation in [this repository](https://github.com/john-t-maurer/ReviewSenseFrontEnd).

## Back End Documentation

### [ReviewSense API Documentation](https://github.com/DaltonSenseman/movie-sentiment-seniorproject/blob/main/Flask%20Server/APIDocs.md#reviewsense-api)   

### [NaiveBayes Documentation](https://github.com/DaltonSenseman/movie-sentiment-seniorproject/blob/main/NaiveBayes%20Machine%20Learning/NaiveBayes_Doc.md#reviewsense-naivebayes-doc)

### Data Sources
* [Kaggle](https://www.kaggle.com/)

## Authors
* Carrie West - Back End Developer / Database Architect
* Dalton Senseman - Machine Learning / Front End Developer
* John Maurer - Front End Developer / Angular Architect

## Acknowledgements
We would like to thank the following people for making this project possible:
* Tyler Dalbora - CallMiner Representative / Project Manager
* Anna Koufakou - Ph.D. Computer Engineering - Machine Learning Expertise
* Fernando Gonzalez - Ph.D. Electrical Engineering - Course Instructor
* Huzefa Kagdi - Ph.D. Software Engineering - Interim Dean / Course Instructor

### Stakeholders
* CallMiner
* Florida Gulf Coast University
