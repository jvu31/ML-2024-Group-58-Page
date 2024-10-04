import streamlit as st
import pandas as pd


contributions = pd.DataFrame (
    [
        {"Name": "Jimmy", "Contributions": "Methods, Streamlit setup"},
        {"Name": "Carlos", "Contributions": "Introduction, Problem Definition"},
        {"Name": "Omo", "Contributions": "Literature Review"},
        {"Name": "Shrenik", "Contributions": "Results & Discussion, Video"},
        {"Name": "Jerry", "Contributions": "Gantt Chart"}

    ]
)
st.set_page_config(page_title='Star Classification Model', page_icon ="🌟", layout = "centered")
# Display text
st.title('Star Classification Model')
st.header('CS 4641 - Fall 2024 - Group 58')

st.header("[Project Github](https://github.com/Skoppaka9/ML-2024-Group-58)")

st.header('Introduction/Background')
st.write(":heavy_minus_sign:"*17)
st.write("Stellar classification is used by scientists to categorize stars based on their spectral characteristics (temperature, size, composition, color, brightness, and more). By classifying these stars, scientists can better understand them by analyzing their patterns and trends, which will hopefully provide us with more knowledge and insight into the universe.")
st.subheader('Literature Review')
st.write("""
- Armstrong et al., “K2 variable catalogue – II. Machine learning classification of variable stars and eclipsing binaries in K2 fields 0–4”
Armstrong et al. utilize a combination of Kohonen Self-Organizing Maps (SOMs an unsupervised machine learning algorithm) and Random Forest as a new method for variable star classification [1]. SOMs were used to effectively parameterize light curve shapes while Random Forest were useful for their classification schemes especially for larger data sets [1].   

- J. Zhang et al., “High-Accuracy Guide Star Catalogue Generation with a Machine Learning Classification Algorithm”
This paper focuses on improving Guide Star Catalogues (GSCs) used in star identification on star sensors in satellites [2]. Zhang et al evaluate the performance of GSCs generated by various machine learning classification algorithms [2]. The results show that the K-Nearest Neighbours (KNN) algorithm produces the best GSC [2].   

- Z. Qi, "Stellar Classification by Machine Learning"
Qi uses three machine learning algorithms, Decision Tree, Random Forest and Support Vector Machine, to build prediction models for stellar classification [3]. The results show that random forest reaches highest accuracy with greatest computing efficiency [3]. 

""")
st.subheader('Dataset')
st.write("""
This [Star Dataset](https://www.kaggle.com/datasets/vinesmsuic/star-categorization-giants-and-dwarfs?select=Star9999_raw.csv) uses spectral data to distinguish whether a star is a dwarf or giant. 

- The features are visual apparent magnitude, distance between star and earth, the standard error of the distance, the spectral type, the absolute magnitude, and the target class (0 - Dwarf, 1- Giant)
- The dataset has either 9,999/99,999 rows of raw data or 3642/39552 rows of preprocessed data. We can choose whether to use raw or preprocessed and more or less data points.
""")



st.header('Problem Definition')
st.write(":heavy_minus_sign:"*18)
st.write("Given that technology is advancing, more data and features of stellar bodies will become available. Instead of manually categorizing the data, we can automate the process and make it more consistent and efficient with machine learning methods. The problem is a binary classification: either a dwarf or giant star. Using various ML models related to binary classification, we will categorize the stars based on the relevant features in the dataset.")

st.header('Methods')
st.write(":heavy_minus_sign:"*6)
st.write("""
**Preprocessing methods:**
- Data Cleaning: Check for missing values/empty rows, remove duplicate rows, remove rows with high standard error, formatting, and splitting data into training and testing sets
- Data Normalization (StandardScalar): Needed given that features can range from small to large value ranges; improves model's performance, accuracy, and stability
- Data Transformation: Encoding categorical data into numeric values, one-hot encoding because spectral types have roman numerals
    """)
st.write(""" 
**ML Models:**
- Random Forest: Effective for star classification problems as can be seen in the literature review, import RandomForestClassifier from sklearn.ensemble
- KNN: A simple and good classification model for a low dimensionality, well-defined dataset, import KNeighborsClassifier from sklearn.neighbors
- Logistic Regression: Useful for binary classification as it predicts whether a data point belongs to a category, import LogisticRegression from sklearn.linear_model        
""")

st.header('(Potential) Results and Discussion')
st.write(":heavy_minus_sign:"*17)
st.write("""
We plan to use accuracy, precision, and recall as our metrics to evaluate our model.

Accuracy is one of the most important and useful metrics for a classification model, given that a data set is balanced, as it provides a quick and simple evaluation of the overall performance 

Precision refers to the proportion of true positive classified given what was classified as positive (true positives and false positives)

Recall shows whether a model correctly identifies true positive instances given all the actual positive instances, which are true positives and false negatives. Recall and precision work well together to ensure that a model is able to identify positive instances and are precise in doing so.

Our goal is to implement various models so that we can find the least computationally expensive one, if significantly different, with the highest accuracy, precision, and recall. 

Each metric is expected to be at least 85% for our models, and we expect the random forest model to perform the best, disregarding computational power.

""")

st.header('References')
st.write("""
[1] D. G. Armstrong et al., “K2 variable catalogue – II. Machine learning classification of variable stars and eclipsing binaries in K2 fields 0–4,” Monthly Notices of the Royal Astronomical Society, vol. 456, no. 2, pp. 2260–2272, Feb. 2016, doi: https://doi.org/10.1093/mnras/stv2836. 

‌[2] J. Zhang et al., “High-Accuracy Guide Star Catalogue Generation with a Machine Learning Classification Algorithm,” Sensors, vol. 21, no. 8, p. 2647, Apr. 2021, doi: https://doi.org/10.3390/s21082647. 

[3] Z. Qi, "Stellar Classification by Machine Learning," SHS Web of Conferences, vol. 144, 2022. Available: https://www.proquest.com/conference-papers-proceedings/stellar-classification-machine-learning/docview/2823491252/se-2. DOI: https://doi.org/10.1051/shsconf/202214403006.

""")

st.header('Gantt Chart')
st.header('Contribution Table')
st.data_editor(contributions, hide_index=True)
st.divider()
st.caption("Jimmy Vu, Shrenik Koppaka, Carlos Aponte, Omikhosen Unuigboje, Jerry Song | © 2024 Star Classification Project")


