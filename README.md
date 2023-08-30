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


## Data
The project utilized two main datasets: [site data](https://drive.google.com/file/d/1TNmOPc1K3zm3faejW9APzXfX5cRUrsGx/view?usp=sharing) and [user data](https://drive.google.com/file/d/1A4LDc3EsBbre0XdROTVjKt47PorT-L93/view?usp=sharing).

The site data encompassed hourly readings from AirQo and non-AirQo devices for the early months of 2023. 
It included attributes such as site names, pm values, and geographic coordinates. A selection of columns including site name, site latitude, site longitude, and pm2.5 values was made for further analysis.

The user data was synthesized, encompassing attributes like age, health conditions, and activities. This data was merged with the site data, forming the foundation for personalized recommendations.

To obtain the target feature column, a custom python script was written which considered the quality category of air and the age of the user to assign a recommendation.



## Methodology



## Results
Upon evaluating the models, the Decision Tree model achieved an accuracy of 0.88. Its classification report exhibited varying precision, recall, and f1-score values, reflecting a range of 0.40 to 1.00 for different classes. 

The tuned Random Forest Classifier attained an accuracy of 0.8911, demonstrating the efficacy of the machine learning approach.



## Conclusion
The project successfully developed a machine learning model to provide personalized air quality recommendations to users based on their health status, age, activities, and pm2.5 values.




## References
- [AirQo](https://airqo.net/)




## Acknowledgements

