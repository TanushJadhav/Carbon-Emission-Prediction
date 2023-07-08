import streamlit as st
import pickle

pickle_in = open('carbon_model.pkl', 'rb') 
classifier = pickle.load(pickle_in)


def prediction(year):
    pred = classifier.predict([[year]])
    return pred

def main():
    html_temp = """ 
    <div style ="background-color:#96e072;padding:13px"> 
    <h1 style =font-family:Montserrat;color:yelloq;text-align:center;">Carbon Footprint Prediction</h1> 
    </div> 
    """
    
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
    year = int(st.number_input("Enter A Year"))
    
    if st.button("Predict"): 
        result = prediction(year)
        st.success(f"The Predicted Carbon Emission for {year} is: {result}")
        
if __name__=='__main__': 
    main()  