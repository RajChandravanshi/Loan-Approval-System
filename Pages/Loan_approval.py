import streamlit as st
import pickle
import pandas as pd
from joblib import load

# Configure page settings
st.set_page_config(
    page_title="Loan Approval Prediction",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
        .stNumberInput, .stSelectbox {
            margin-bottom: 20px;
        }
        .stButton button {
            width: 100%;
            background-color: #2E8B57;
            color: white;
            font-weight: bold;
            padding: 0.5rem;
            border-radius: 5px;
        }
        .stButton button:hover {
            background-color: #3CB371;
        }
        .prediction-result {
            text-align: center;
            font-size: 1.5rem;
            padding: 1rem;
            border-radius: 5px;
            margin-top: 1rem;
        }
        .approved {
            background-color: #DFF2DF;
            color: #2E8B57;
        }
        .rejected {
            background-color: #FFE8E8;
            color: #D8000C;
        }
    </style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_data():
    """Load data and pipeline with caching"""
    try:
        with open("df.pkl", 'rb') as file:
            df = pickle.load(file)
        with open("Loan_approval_pipeline.pkl", 'rb') as file:
            pipeline = load(file)
        return df, pipeline
    except Exception as e:
        st.error(f"Error loading data or pipeline: {e}")
        return None, None

df, pipeline = load_data()

# Application header
st.markdown(
    """
    <h1 style="text-align: center; color: #2E8B57;">🏦 Loan Approval Prediction</h1>
    <p style="text-align: center; color: gray;">Fill in the applicant details to predict loan approval status</p>
    """, 
    unsafe_allow_html=True
)

st.write("---")

# Create input layout
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Personal Details")
    Age = st.number_input('Age of Applicant', min_value=18, max_value=100, step=1, value=25)
    Gender = st.selectbox("Gender", sorted(df['person_gender'].unique().tolist()))
    Education = st.selectbox("Education Level", sorted(df['person_education'].unique().tolist()))
    Income = st.number_input("Yearly Income (₹)", min_value=80000, step=10000, value=250000) // 12

with col2:
    st.subheader("Employment & Housing")
    Emp_exp = st.number_input("Employment Experience (Years)", min_value=0, max_value=50, step=1, value=2)
    Home_Ownership = st.selectbox('Home Ownership', sorted(df['person_home_ownership'].dropna().unique().tolist()))
    Previous_Default = st.selectbox('Previous Loan Default', ['No', 'Yes'])
    Credit_History_Length = st.number_input('Credit History Length (Years)', min_value=0.0, max_value=50.0, step=1.0, value=5.0)

with col3:
    st.subheader("Loan Details")
    Loan_Amount = st.number_input('Loan Amount Requested (₹)', min_value=50000.0, step=1000.0, value=100000.0) // 12
    Reason = st.selectbox('Loan Purpose', sorted(df['loan_intent'].unique().tolist()))
    Int_rate = st.slider('Interest Rate (%)', min_value=1.0, max_value=30.0, step=0.5, value=10.0)
    Credit_Score = st.slider('Credit Score', min_value=300, max_value=850, step=10, value=650)

# Calculate derived field
Percent_Income = round((Loan_Amount / Income) * 100, 2) if Income > 0 else 0
st.caption(f"Loan amount represents {Percent_Income}% of monthly income")

# Create DataFrame for prediction with explicit type conversion
input_data = pd.DataFrame({
    'person_age': [int(Age)],
    'person_gender': [Gender],
    'person_education': [Education],
    'person_income': [float(Income)],
    'person_emp_exp': [int(Emp_exp)],
    'person_home_ownership': [Home_Ownership],
    'loan_amnt': [float(Loan_Amount)],
    'loan_intent': [Reason],
    'loan_int_rate': [float(Int_rate)],
    'loan_percent_income': [float(Percent_Income)],
    'cb_person_cred_hist_length': [float(Credit_History_Length)],
    'credit_score': [float(Credit_Score)],
    'previous_loan_defaults_on_file': [Previous_Default]
})

# Prediction logic with input validation
if st.button('Predict Loan Approval', key="predict_btn", type="primary"):
    try:
        # Validate inputs
        if Age <= 0 or Income <= 0 or Loan_Amount <= 0:
            st.warning("Please enter valid positive values for all fields")
            st.stop()
            
        if Loan_Amount > Income * 50:  # Simple sanity check
            st.warning("Loan amount seems unusually high compared to income")
            
        # Show input summary for review
        with st.expander("🔍 Review Input Details"):
            st.dataframe(input_data.style.format({
                'person_income': '{:,.0f} ₹',
                'loan_amnt': '{:,.0f} ₹',
                'loan_int_rate': '{:.1f}%',
                'loan_percent_income': '{:.1f}%'
            }))

        # Make prediction
        prediction_proba = pipeline.predict_proba(input_data)[0]
        result = pipeline.predict(input_data)[0]
        
        # Display result with confidence
        if result == 1:
            st.markdown(
                f'<div class="prediction-result approved">'
                f'✅ Loan Approved (Confidence: {prediction_proba[1]*100:.1f}%)'
                f'</div>', 
                unsafe_allow_html=True
            )
            st.balloons()
        else:
            st.markdown(
                f'<div class="prediction-result rejected">'
                f'❌ Loan Rejected (Confidence: {prediction_proba[0]*100:.1f}%)'
                f'</div>', 
                unsafe_allow_html=True
            )
            
        # Show feature importance if available
        try:
            if hasattr(pipeline, 'feature_importances_'):
                importances = pipeline.feature_importances_
                features = pipeline.feature_names_in_
                importance_df = pd.DataFrame({'Feature': features, 'Importance': importances})
                importance_df = importance_df.sort_values('Importance', ascending=False)
                
                with st.expander("📊 See Feature Importance"):
                    st.bar_chart(importance_df.set_index('Feature'))
        except:
            pass

    except Exception as e:
        st.error(f"❌ Prediction failed: {str(e)}")

st.write("---")

# Footer
st.markdown(
    """
    <footer style="text-align: center; color: gray; margin-top: 20px;">
        <p>Powered by <b>Streamlit</b> | Created by <b>RAJ CHANDRAVANSHI</b></p>
    </footer>
    """, 
    unsafe_allow_html=True
)