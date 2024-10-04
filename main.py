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

st.subheader('Introduction/Background')
st.write(":heavy_minus_sign:"*14)
st.write("Stellar classification is used by scientists to categorize stars based on their spectral characteristics (temperature, size, composition, color, brightness, and more). By classifying these stars, scientists can better understand them by analyzing their patterns and trends, which will provide us with more knowledge and insight into the universe.")
st.write('**Literature Review:**')
st.write("""
- Armstrong et al. utilize a combination of Kohonen Self-Organizing Maps (SOMs) and Random Forest as a new method for variable star classification [1]. SOMs were used to effectively parameterize light curve shapes while Random Forest were useful for their classification schemes, especially for larger data sets [1].   

- Zhang et al. focus on improving Guide Star Catalogues (GSCs) used in star identification on star sensors in satellites [2]. Zhang et al. evaluate the performance of GSCs generated by various machine learning classification algorithms [2]. K-Nearest Neighbours (KNN) produces the best GSC [2].   

- Qi classified celestial bodies into stars, galaxies, and quasars using Decision Tree, Random Forest, and SVM models [3]. SMOTE, normalization, and data splitting were used for preprocessing [3]. Random Forest had the best computing performance and accuracy [3].

""")
st.write('**Dataset:**')
st.write("""
This [Star Dataset](https://www.kaggle.com/datasets/vinesmsuic/star-categorization-giants-and-dwarfs?select=Star9999_raw.csv) uses spectral data to distinguish whether a star is a dwarf or giant. 

- The features are visual apparent magnitude, distance between star and earth, standard error of the distance, spectral type, absolute magnitude, and the target class (0 - Dwarf, 1- Giant)
- The dataset has either 9,999/99,999 rows of raw data or 3642/39552 rows of preprocessed data. We can choose whether to use raw or preprocessed and more or less data points
""")



st.subheader('Problem Definition')
st.write(":heavy_minus_sign:"*11)
st.write("Given that technology is advancing, more data and features of stellar bodies will become available. Instead of manually categorizing the data everytime, we can automate the process to make it more consistent and efficient with machine learning. Our problem is a binary classification; we will classify whether a star is dwarf or giant using our ML models.")

st.subheader('Methods')
st.write(":heavy_minus_sign:"*6)
st.write("""
**Preprocessing methods:**
- Data Cleaning: Check for missing values/empty rows, remove duplicate rows, remove high-error rows, formatting, and splitting data into training and testing sets
- Data Normalization (StandardScalar): Needed given that features can range from small to large value ranges, improves model's performance, accuracy, and stability
- Data Transformation: Encoding categorical data into numerical values; we will use one-hot encoding because spectral types have roman numerals
    """)
st.write(""" 
**ML Models:**
- Random Forest: Strong classification model shown by literature review; we want to test it with our dataset
    \n**import RandomForestClassifier from sklearn.ensemble**
- KNN: A simple and good classification model for a low dimensionality, well-defined dataset
    \n**import KNeighborsClassifier from sklearn.neighbors**
- Logistic Regression: Useful for binary classification as it predicts whether a data point belongs to a category 
    \n**import LogisticRegression from sklearn.linear_model**        
""")

st.subheader('(Potential) Results and Discussion')
st.write(":heavy_minus_sign:"*19)
st.write("""
We plan to use accuracy, precision, and recall as our metrics to evaluate our model.

- Accuracy is one of the most important and useful metrics for a classification model, given that a data set is balanced, as it provides a quick, simple evaluation of the overall performance

- Precision refers to the proportion of true positive classified given what was classified as positive (true positives and false positives)

- Recall shows whether a model correctly identifies true positive instances given all the actual positive instances, which are true positives and false negatives.

Recall and precision work well together to ensure that a model is able to identify and classify try positive instances. 
         Accuracy is a helpful, standard metric, so a combination of these three metrics will reliably evaluate the performance of our models given our dataset.

Each metric is expected to be at least 85% for our models, and we expect the random forest model to perform the best [3].

""")

st.subheader('References')
st.write(":heavy_minus_sign:"*6)
st.write("""
[1] D. G. Armstrong et al., “K2 variable catalogue – II. Machine learning classification of variable stars and eclipsing binaries in K2 fields 0–4,” Monthly Notices of the Royal Astronomical Society, vol. 456, no. 2, pp. 2260–2272, Feb. 2016, doi: https://doi.org/10.1093/mnras/stv2836. 

‌[2] J. Zhang et al., “High-Accuracy Guide Star Catalogue Generation with a Machine Learning Classification Algorithm,” Sensors, vol. 21, no. 8, p. 2647, Apr. 2021, doi: https://doi.org/10.3390/s21082647. 

[3] Z. Qi, “Stellar Classification by Machine Learning,” SHS Web of Conferences, vol. 144, p. 03006, 2022, doi: https://doi.org/10.1051/shsconf/202214403006.


""")

st.subheader('Gantt Chart')
st.subheader('Contribution Table')
st.data_editor(contributions, hide_index=True)
st.divider()
st.caption("Jimmy Vu, Shrenik Koppaka, Carlos Aponte, Omikhosen Unuigboje, Jerry Song | © 2024 Star Classification Project")


