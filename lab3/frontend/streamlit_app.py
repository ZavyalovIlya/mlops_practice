import streamlit as st
import requests

st.title('California housing')
st.write('''This application allows you to predict the house price in different block groups of California.
Linear regression model is used for prediction. The model was trained on the California housing dataset provided by scikit-learn ([link](https://inria.github.io/scikit-learn-mooc/python_scripts/datasets_california_housing.html)).

Please, select desired characteristics and press "Calculate" button to estimate the house price.
''')

col1, col2 = st.columns(2)
with col1:
    MedInc = st.slider('Median income in block group', 0.5, 12.0, value=3.5, step=0.1)
    HouseAge = st.slider('Median house age in block group', 1.0, 52.0, value=29.0, step=0.1)
    AveRooms = st.slider('Average number of rooms per household', 1.0, 12.0, value=5.2, step=0.1)
    AveBedrms = st.slider('Average number of bedrooms per household', 0.1, 5.0, value=1.0, step=0.1)
with col2:
    Population = st.slider('Block group population', 3.0, 5000.0, value=1166.0, step=0.1)
    AveOccup = st.slider('Average number of household members', 0.5, 8.0, value=2.8, step=0.1)
    Latitude = st.slider('Block group latitude', 32.54, 41.95, value=34.3, step=0.1)
    Longitude = st.slider('Block group longitude', -124.35, -114.31, value=-118.5, step=0.1)

# Convert to float
data = {
    'X': [float(MedInc),
         float(HouseAge),
         float(AveRooms),
         float(AveBedrms),
         float(Population),
         float(AveOccup),
         float(Latitude),
         float(Longitude)
    ]
}

if st.button('Calculate'):

    # pretty loading spinner
    with st.spinner('Please wait...'):

        # sending request to fastapi
        response = requests.post(url="http://backend:8000/predict/",
                                 json=data)

        prediction = response.json()['prediction']
        st.write(f"Predicted price: {prediction}")