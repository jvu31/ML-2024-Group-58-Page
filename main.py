import streamlit as st
import pandas as pd


contributions = pd.DataFrame (
    [
        {"Name": "Jimmy", "Contributions": "gfnkjlgdf"},
    ]
)

# Display text
st.title('Star Classification Model')
st.header('CS 4641 - Fall 2024')
st.subheader('Introduction/Background')
st.text("Stellar classification is used by scientists to categorize stars based on their spectral characteristics (temperature, size, composition, color, brightness, and more). By classifying these stars, scientists can better understand them by analyzing their patterns and trends, which will hopefully provide us with more knowledge and insight into the universe.")

st.text("This Star Dataset uses spectral data to distinguish whether a star is a dwarf or giant.")

st.text("The features are visual apparent magnitude, distance between star and earth, the standard error of the distance, the spectral type, the absolute magnitude, and the target class (0 - Dwarf, 1- Giant)")

st.text("The dataset has either 9,999/99,999 rows of raw data or 3642/39552 rows of preprocessed data. We can choose whether to use raw or preprocessed and more or less data points.")
st.subheader('Problem Definition')
st.text("Given that technology is advancing, more data and features of stellar bodies will become available. Instead of manually categorizing the data, we can automate the process and make it more consistent and efficient with machine learning methods. The problem is a binary classification: either a dwarf or giant star. Using various ML models related to binary classification, we will categorize the stars based on the relevant features in the dataset.")
st.subheader('Methods')
st.text("To have the dataset in a state where we can analysis it, we propose the following preprocessing methods:")
st.text("Data Cleaning: Formatting, handling duplicate rows, missing or empty rows")
st.text("Remove rows with too much error, make sure there are no indices in our data and split the data properly")
st.text("Data Normalization (StandardScalar): needed given that features can range from small to large ranges")
st.text("Data Transformation: some features are classified with labels rather than numeric values, which need to be converted to appropriate integer id values (encoding categorical data)")
st.text("ML Models: ")
st.text("HDBScan: model that is able to scale with large datasets")
st.text("KNN: good classification model for low dimensionality dataset")
st.text("SVM: optimal for binary classification")
st.subheader('(Potential) Results and Discussion')
st.text("We plan to use accuracy, precision, and recall as our metrics to evaluate our model.

st.text("Accuracy is one of the most important and useful metrics for a classification model, given that a data set is balanced, as it provides a quick and simple evaluation of the overall performance")

st.text("Precision refers to the proportion of true positive classified given what was classified as positive (true positives and false positives)")

st.text("3. Recall shows whether a model correctly identifies true positive instances given all the actual positive instances, which are true positives and false negatives. Recall and precision work well together to ensure that a model is able to identify positive instances and are precise in doing so.")

st.text("Our goal is to implement various models so that we can find the least computationally expensive one, if significantly different, with the highest accuracy, precision, and recall.")

st.text("Each metric is expected to be at least 85% for our models, and we expect the random forest model to perform the best, disregarding computational power.")
st.subheader('References')

st.subheader('Gantt Chart')
st.subheader('Contribution Table')
st.data_editor(contributions, hide_index=True)


