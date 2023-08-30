# Personalizing Air Quality Recommendations using Machine Learning

## Introduction
This project will use machine learning to develop personalized air quality recommendations for users based on their personal information, such as location, age, health conditions, and activities. The goal of this project is to help users make informed decisions about their exposure to air pollution.

This project was geared towards utilizing machine learning techniques to provide personalized air quality recommendations to users based on their health status, age, activities, and pm2.5 values.


## Scope
The project used a machine learning approach to develop personalized air quality recommendations. The following steps were taken:
- Collect data on air quality, user current location (we can use coordinates), and use personal information (age, gender, “health conditions'', and activities). We can think of what health conditions that are most affected by air quality e.g., respiratory diseases, mental health, cardiovascular diseases to mention but a few. 
- Clean and prepare the data
- Personalize air quality recommendations for users based on their personal information
- Evaluate the effectiveness of the personalized air quality recommendations

By leveraging user data and real-time pm2.5 readings, the aim was to empower individuals with actionable insights to make informed decisions regarding their outdoor activities and exposure to air pollutants.


## Methodology
### Data and Preprocessing
The project utilized two main datasets: [site data](https://drive.google.com/file/d/1TNmOPc1K3zm3faejW9APzXfX5cRUrsGx/view?usp=sharing) and [user data](https://drive.google.com/file/d/1A4LDc3EsBbre0XdROTVjKt47PorT-L93/view?usp=sharing).

The site data encompassed hourly readings from AirQo and non-AirQo devices for the early months of 2023. 
It included attributes such as site names, pm values, and geographic coordinates. A selection of columns including site name, site latitude, site longitude, and pm2.5 values was made for further analysis.

The user data was synthesized, encompassing attributes like age, health conditions, and activities. This data was merged with the site data, forming the foundation for personalized recommendations.

To obtain the target feature column, a custom python script was written which considered the quality category of air and the age of the user to assign a recommendation. More can be found in the [notebook](https://colab.research.google.com/drive/1iKuH7mPeid2bq7V7U4c9Dx2HGGyloOtS?usp=sharing)

Age distribution of users

![age distribution](https://github.com/bruceMug/airquality_recommender/blob/main/static/images/age%20distribution.png)

Counts of pm categories

![Air quality categories counts](https://github.com/bruceMug/airquality_recommender/blob/main/static/images/download%20(1).png)

## Model Development
To create an effective recommendation system, different machine learning algorithms were explored, and these include logistic regression, support vector machine, decision tree, random forest and xgboost classifier.

The model training process involved steps, such as feature selection, encoding categorical features, and splitting the dataset into training (70%) and testing sets (30%). 

After the training, the models didn’t quite perform well. So, in-order to improve the accuracy, techniques like hyperparameter tuning and optimization had to be employed for the high performing algorithms.

Hyperparameter tuning for the Random Forest Classifier was performed using the Random Search CV method, resulting in optimal parameters of 156 estimators and a maximum depth of 15.
For the decision tree tuning, we used the gridsearchCV with two sets of hyperparameters in which case the best parameters were ‘entropy’ as criterion, max depth of 30 and min samples split as 15. 


## Results
Upon evaluating the models, the Decision Tree model achieved an accuracy of 0.88. Its classification report exhibited varying precision, recall, and f1-score values, reflecting a range of 0.40 to 1.00 for different classes. 
The tuned Random Forest Classifier attained an accuracy of 0.8911, demonstrating the efficacy of the machine learning approach.

The confusion matrices for the models are shown below:

Decision Tree Classifier Confusion Matrix
![decision tree confusion matrix](https://github.com/bruceMug/airquality_recommender/blob/main/static/images/decision%20tree.png)

Random Forest Classifier Confusion Matrix

![random forest confusion matrix](https://github.com/bruceMug/airquality_recommender/blob/main/static/images/randomforest.png)


The table showing the accuracy of the models used is shown below:
![model accuracy](https://github.com/bruceMug/airquality_recommender/blob/main/static/images/table_accuracy.png)


## Conclusion
The project successfully developed a machine learning model to provide personalized air quality recommendations to users based on their health status, age, activities, and pm2.5 values.

For other information, take a look at the [model card](https://docs.google.com/document/d/1Oxor2V4Yaw5SCR__KXTVcectO95SjayVmwq4pBr9ag0/edit?usp=sharing) designed by [@Nakacwa Olivia](https://github.com/NakacwaOlivia) which was designed to provide a summary of the model's performance and limitations.
The model card can also be found [here](https://github.com/NakacwaOlivia/AirQuality-Personal-Recommendation)

Detailed information about the project can be found in the [notebook](https://colab.research.google.com/drive/1iKuH7mPeid2bq7V7U4c9Dx2HGGyloOtS?usp=sharing).



## Contact
Created by Bruce Mugizi - [@bruceMug](https://twitter/brucemug) - [mugizi@duck.com](mugizi@duck.com) - feel free to contact me!

Project Link: [https://github.com/bruceMug/airquality_recommender](https://github.com/bruceMug/airquality_recommender)

## Contributors ✨
Thanks to the following people who have contributed to this project:

<table>
<tbody>
<tr>
<td align="center" valign="top" width="14.28%"><a href="https://github.com/NakacwaOlivia"><img src="https://avatars.githubusercontent.com/u/69842870?v=4" width="100px;" alt="Olivia Nakacwa"/><br /><sub><b>Nakacwa Olivia</b></sub></a><br /><a title="Answering Questions">💬</a> <a title="Documentation">📖</a><a title="Reviewed Pull Requests">👀</a> <a title="Talks">📢</a></td>

<td align="center" valign="top" width="14.28%"><a href="https://github.com/mar-vyn23"><img src="https://avatars.githubusercontent.com/u/101456450?v=4" width="100px;" alt="Marvin Satulo"/><br /><sub><b>Marvin Satulo</b></sub></a><br /><a title="Answering Questions">💬</a> <a title="Documentation">📖</a><a title="Reviewed Pull Requests">👀</a> <a title="Talks">📢</a></td>
</tr>
</tbody>
</table>


## Acknowledgements
- [AirQo](https://airqo.net/)
- [Template](https://github.com/othneildrew/Best-README-Template/blob/master/README.md)


