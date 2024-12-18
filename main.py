import streamlit as st
import pandas as pd


contributions = pd.DataFrame (
    [
        {"Name": "Jimmy", "Contributions": "Random Forest Model and Write-Up"},
        {"Name": "Carlos", "Contributions": "Linear SVM Model and Write-Up"},
        {"Name": "Omo", "Contributions": "Put Slides Together"},
        {"Name": "Shrenik", "Contributions": "Conclusion Write-Up and Video Recordign"},
        {"Name": "Jerry", "Contributions": "Put Slides Together"}
    ]
)
st.set_page_config(page_title='Star Classification Project', page_icon ="🌟", layout = "centered")
# Display text
st.title('Star Classification Project [(Github)](https://github.com/Skoppaka9/ML-2024-Group-58)')
st.header('CS 4641 - Fall 2024 - Group 58')

st.subheader('Introduction/Background')
st.write(":heavy_minus_sign:"*14)
st.write("Stellar classification is used by scientists to categorize stars based on their spectral characteristics (temperature, size, composition, color, brightness, etc.). By classifying these stars, scientists can better understand them by analyzing their patterns and trends, which will provide us with more knowledge and insight into the universe.")
st.write('**Literature Review:**')
st.write("""
- Armstrong et al. utilized a combination of Kohonen Self-Organizing Maps (SOMs) and Random Forest as a new method for variable star classification [1]. SOMs were used to effectively parameterize light curve shapes while Random Forest were useful for their classification schemes, especially for larger data sets [1].   

- Zhang et al. focused on improving Guide Star Catalogues (GSCs) used in star identification on star sensors in satellites [2]. Zhang et al. evaluated the performance of GSCs generated by various machine learning classification algorithms [2]. K-Nearest Neighbours (KNN) produced the best GSC [2].   

- Qi classified celestial bodies into stars, galaxies, and quasars using Decision Tree, Random Forest, and SVM models [3]. SMOTE, normalization, and data splitting were used for preprocessing [3]. Random Forest had the best computing performance and accuracy [3].

""")
st.write('**Dataset:**')
st.write("""
This [Star Dataset](https://www.kaggle.com/datasets/vinesmsuic/star-categorization-giants-and-dwarfs?select=Star9999_raw.csv) uses spectral data to distinguish whether a star is a dwarf or giant. 

- The features are visual apparent magnitude, distance between star and earth, standard error of the distance, spectral type, absolute magnitude, and the target class (0 - Dwarf, 1- Giant)
- The dataset has either 9,999/99,999 rows of raw data or 3642/39552 rows of preprocessed data. We can choose the type and how many data points we want.
""")



st.subheader('Problem Definition')
st.write(":heavy_minus_sign:"*11)
st.write("Given that technology is advancing, more data on stellar bodies will become available. Instead of manually categorizing the data everytime, we can automate the process to make it more consistent and efficient with machine learning. Our problem is a binary classification; we will classify whether a star is dwarf or giant using our ML models.")

st.subheader('Methods')
st.write(":heavy_minus_sign:"*6)
st.write("""
**Preprocessing methods:**

Our dataset was already preprocessed and pre-balanced. 
  
We still checked to see if there were any null or duplicated data in the dataset so that we could remove them, but we got zero for both. We also tried to check and remove outliers in our dataset by visualizing the features with box plots. Our attempt to remove outliers was by using the IQR method, 
         which can be seen in the code below:""")
st.image('Images/Data Check.png')
st.image('Images/Box Plot.png', caption="Box plot of the features in the dataset")
st.image('Images/Removing Outliers.png', caption="Removing outliers using the IQR method")
st.image('Images/Box Plot No Outliers.png', caption="Box Plot without outliers")
st.write("""
    We also plotted the graphs of each feature to see the correlations between them. The 'Plx' and 'e_Plx' features had what seems to be outliers and weird patterns, so we conducted PCA to see if we could reduce the dimensionality of the dataset.
        """)
st.image('Images/pairplot.png', caption="Feature Plots")
st.write("""
    Conducting PCA, we were able to see the variance of each component, and as expected, 'Vmag', 'B-V', and 'Amag', comprised most of the variance, but 'Plx' and 'e_Plx' still had about 20% of the variance together.
         """)
st.image('Images/PCA.png', caption="PCA Variance")
st.write("""
    We also plotted a heatmap of feature correlations and saw that e_Plx and Plx had a high correlations with Vmag and Amag, respectively, so we wanted to see how our model's accuracy would be affected by removing these two features (e_Plx and Plx).
        """)
st.image('Images/Feature Correlation.png', caption="Heatmap of Feature Correlations")
st.write("""
         Finally, we used a label encoder to encode the spectral type feature, which was a string, into a numerical value so that our model can train on it properly. We saw there was no significant difference between using a label encoder or a one hot encoder, so we went with one hot encoder because it is used for categorical features that are not ordinal or don't have an inheret ordering.
            """)
st.image('Images/Encoding.png', caption="Label Encoding")
st.write("""
         We then dropped the 'Target Class' feature from our training data, otherwise we would be cheating, and assigned 'Target Class' values to our testing data. We then split our data into training and testing data with a 80/20 split, and we normalized the data using Standard Scaler so that we can identify true effects.
         
         Normalizing the data is important because it allows the model to converge faster and prevents the model from being biased towards features with larger scales, and it helped improve the performance and stability of our model. 
            """)
st.image('Images/Split-Normalize.png', caption="Splitting Data")
st.write(""" 
**ML Models:**

We used logistic regression for our first model because it is a relatively simple model that is good for binary classification. The model assumes that the data is linearly separable and that there is a linear relationship, so it serves as a simple, interpretable model for binary classification. 

Logistic regression uses the sigmoid functions which handles the decision boundary, so that is why it is good for binary classification. Also, logistic regression is good for a dataset with fewer features and can be combined with regularization to prevent overfitting. 

Since this is a relatively simple model to implement, we decided it would be good to use as our first model because it is simple to understand and will serve as a benchmark for future models.   
""")
st.image('Images/Model.png', caption="Logistic Regression")

st.write("""
The second model used was random forest classification. As an extension of the decision tree model, it consists of branching nodes separated via thresholds of certain feature values. Randomness is introduced from using random subsets of data to evaluate which features to partition from. 

While this model is suitable for highly accurate binary classifications, it can also be very computationally intensive to run. It also has many hyperparameters that can be tuned to alter its efficiency. The ones we have chosen to callibrate are the number of estimators, the maximum depth, and the max percentage of features to pull from. 
""")
st.image('Images/RF_Model.png', caption="Random Forest Classification")

st.write("""
The third and final model we used to solve the classification problem is a Support Vector Machine (SVM). The idea is that this model can project the data into a higher-dimensional space where the classes become linearly separable.

Other advantages of using SVM are the ability to tune various hyperparameters to improve the model's performance (such as choosing different kernel types and kernel coefficients), and the option to include a regularization term so that we don't overfit the data.

However, since the optimization problem for this model grows quadratically with the dataset size, tuning and running SVM can be very expensive computationally and take a relatively long time compared to other simpler models.

Nonetheless, for our first attempt at SVM, we decided to use the simple linear kernel to see how well it would perform before tuning the hyperparameters.
""")
st.image('Images/SVM_Model.png', caption="SVM Classifier")

st.subheader('Results and Discussion')
st.write(":heavy_minus_sign:"*19)
st.write("""
**Logistic Regression:**

In our proposal, we wanted each metric to be at least 85% for our models, and we achieved that with logistic regression. For our initial results, we tested not removing outliers, using all features, and using a label encoder. 
As can be seen in the figure, we achieved:""") 
st.write("- 88.36% Accuracy")
st.write("- 87.02% Precision")
st.write("- 90.17% Recall")
st.write("- 88.57% F1 Score")
st.write("""
Our confusion matrix can be seen below, as well, and it shows that our model did a relatively good job identifying true positive and false negatives, around 3500 in both cases. 
             
Our model performed well because we used a balanced dataset, encoded the categorical features, and split and normalized the data. Logistic regression does well with binary classification, which is why we saw good results since that is what our dataset and problem is. 
          
We didn't see amazing results because logistic regression is one of the simpler models, and we only used the default parameters.
""")
st.image("Images/Normal Results.png", caption = "Basline Results")
st.write("""
         When we tried to remove the outliers in our dataset, we saw that our accuracy, precision, recall, and F1 all decreased. There are many possible explanations for this; one being that we might have removed outliers in the wrong way, especially for our specific data set.

         Our dataset can be considered as relatively small, so removing outliers results in less data points and training data for our model to use. Additionally, the outliers may have been informative data points that reflect important variability in the data, which could have influenced the decision boundary as well.

         Outliers also represent edge cases or rare cases that are present in the real world, so removing them might make the model less generalizable to unseen data, especially if the outliers were meaningful data points.
         """)
st.image("Images/Removing Outlier Results.png", caption = "Outlier Results")
st.write("""
        Going off of the results of PCA, if we removed the 'Plx', 'e_Plx', and Spectral Type features from the dataset, we found that the our performance metrics only slightly decreased. Although there are slight changes in performance, we are decreaseing the dimensionality of our dataset by removing three features, and we are getting basically the same accuracy, precision, and recall.
        
        This is good because it shows that our model is not relying on these features to make predictions, and it can still make accurate predictions without them.
         """)
st.image("Images/Top 3 Components.png", caption = "PCA Results")
st.write("""
        Finally, we wanted to see the differences in performance if we used label encoding compared to one hot encoding. We found that one hot encoding had a slightly lower precision score, but slightly higher f1 and recall score.
        
        However, using one hot encoding makes the most sense because it is used for categorical features that are not ordinal or don't have an inheret ordering, and it is better for our model to train on. Therefore, moving forward, we will use a one-hot encoder for our data for other models to train on.
         """)
st.image("Images/One Hot Encoder.png", caption = "One Hot Encoding Results")

st.write("""
        Overall, our model performed well as every metric was above 85%, and we were able to see how different preprocessing methods affected our model's performance. 
         
        We can attribute the model's success to the nature of the classification and the data pre-processing. We only used the default parameters for logistic regression, so the results may not have been the best they could've been. 
         
         """)

st.write("""
**Random Forest Classification:**

For our random forest classification model produced fairly accurate results, as seen below. This model was tested with the default hyperparameters provided by sklearn and one hot encoding. It crosses over the 85% threshold sought after.
""")
st.image("Images/RF_Results_Default.png", caption = "Random Forest Base Results")


st.write("""
There are more values we can adjust to further increase the efficiency of the model. For one, we found that swapping back to label encoding over one hot encoding resulted in an increase in performace across the board, as seen below. This increase in performace is still apparent in future changes made to the model's values.

This could be perhaps due to random forest tree's model fitting better to label encoding's categorical values rather than one hot encodings feature values.
""")
st.image("Images/RF_Results_LE.png", caption = "Random Forest w/ Label Encoding")


st.write("""
The model can be further improved by finding specific hyperparameter values that better fit the given dataset. As mentioned before, the hyperparameters we will be attempting to tune are the number of estimators, maximum depth, and the percentage of features to use.

Given the range and amount of hyperparameters to determine, finding the optimal combination can be an tedious and extraneous process. As such, we will be utilizing sklearn's RandomizedSearchCV model to search for it. It runs via testing random sets of hyperparameter values, and returns the combination with the highest accuracy.

We then used the hyperparameters provided by the search to set intial values for the random forest model.
""")
st.image("Images/RF_RandomizedSearch.png", caption = "RandomizedSearchCV")
st.image("Images/RF_Hyperparameters.png", caption = "RandomizedSearchCV Results")


st.write("""
When running the model with these new hyperparameters, we see a substantial increase in performance in accuracy, precision, recall, and F1 scores. This is likely due to the new hyperparameters scaling better with larger values and ranges. Compared to the default values, with values relatively smaller, the new values fit better for larger datasets.

""")
st.image("Images/RF_Results_Tuned.png", caption = "Random Forest w/ Hyperparameter Tuning")

st.write("""
**SVM Classifier:**

The default linear SVM classifier produced similar initial results as the random forest model, which is a decent result for this version of SVM which runs the fastest.
""")
st.image("Images/SVM_Model_Results.png", caption = "Linear SVM Results")
st.image("Images/SVM_Model_CM.png", caption = "Linear SVM Confusion Matrix")

st.write("""
We can rely on the results from previous models as evidence that Label Encoding is better than One-Hot Encoding, so we can immediately try to tune the parameters to attempt to gain even better performance.

Shown below is the entire hyperparameter space that was tested to see which combination performed better.
""")
st.image("Images/SVM_Tuned.png", caption = "SVM Hyperparameter Tuning")

st.write("""
After finding the best SVM parameters, we trained a new model to see how it compared to the previous linear SVM.
""")
st.image("Images/SVM_Tuned_Results.png", caption = "Tuned SVM Results")
st.image("Images/SVM_Tuned_CM.png", caption = "Tuned SVM Confusion Matrix")

st.write("""
As you might observe, in this situation, tuning the hyperparameters from the ones we chose only improved performance by a near-negligible amount.

Furthermore, the time that it took to tune the hyperparameters and then train the model was too long for the results we obtained.

In terms of binary star classification, we would be better of using a different model.
""")

st.subheader('Conclusion')
st.write(":heavy_minus_sign:"*7)
st.write("We have incorporated GridSearchCV and RandomizedSearchCV to tune the hyperparameters of our models, which has helped us achieve better results.")
st.write("The Random Forest model has higher performance metrics and more concentrated true positive/negatives in the confusion matrix")
st.write("One reason that the Random Forest performed the best could be that the classification involved more complex, non-linear boundaries. Random Forests are known to be good at handling more complex, non-linear data since they are a collection of decision trees.")
st.write("Random Forests are also good at handling outliers and extreme values because the individual trees help average out the noise.")
st.write("Another reason could be that the Random Forest model was able to capture the interactions between the features better than the other models.")
st.write("The Logistic Regression and SVM Models may have assumed a linear decision boundary or separability which may not be ideal for this calssification. These models were sensitive to outliers and could not capture the complex, non-linear feature relationship as well as random forest.")
st.write("Although the random forest model performed the best, it is important to note that it is less interpretable, uses more memory and computational reosources, and the time to predict increases with the number of trees. Overall, it is more complex and computationally intensive compared to the other models.")
st.write("Logistic Regression and SVM are relatively simple to implement and explain, especially from scratch. They are less computationally expensive, require lower memory, and have relatively faster prediction times, compared to Random Forest.")
st.write("However, as we have seen, they don't proide the best results for this classification problem, which was expected as we predicted Random Forest to perform the best, initially.")

st.subheader('References')
st.write(":heavy_minus_sign:"*6)
st.write("""
[1] D. G. Armstrong et al., “K2 variable catalogue – II. Machine learning classification of variable stars and eclipsing binaries in K2 fields 0–4,” Monthly Notices of the Royal Astronomical Society, vol. 456, no. 2, pp. 2260–2272, Feb. 2016, doi: https://doi.org/10.1093/mnras/stv2836. 

‌[2] J. Zhang et al., “High-Accuracy Guide Star Catalogue Generation with a Machine Learning Classification Algorithm,” Sensors, vol. 21, no. 8, p. 2647, Apr. 2021, doi: https://doi.org/10.3390/s21082647. 

[3] Z. Qi, “Stellar Classification by Machine Learning,” SHS Web of Conferences, vol. 144, p. 03006, 2022, doi: https://doi.org/10.1051/shsconf/202214403006.


""")

st.subheader('Gantt Chart')
st.image("gantt.png", caption="There is a zoom in feature when you hover over the image.")


st.subheader('Contribution Table')
st.data_editor(contributions, hide_index=True)
st.divider()
st.caption("Jimmy Vu, Shrenik Koppaka, Carlos Aponte, Omikhosen Unuigboje, Jerry Song | © 2024 Star Classification Project")


