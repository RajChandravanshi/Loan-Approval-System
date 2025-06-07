import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Loan Approval Prediction System - Home",
    page_icon="🏦",
    layout="wide"
)

# Custom CSS for enhanced styling
st.markdown(
    """
    <style>
        /* Page background and global text color */
        .stApp {
            background-color: #E6F7F5;
            color: #000000;
        }
        /* Main header styling */
        .main-header {
            text-align: center;
            color: #2E8B57;
            font-size: 48px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        /* Sub-header (optional, currently unused) */
        .sub-header {
            text-align: center;
            color: gray;
            font-size: 20px;
            margin-bottom: 30px;
        }
        /* Feature section container */
        .features-section {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        .features-title {
            color: #2E8B57;
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 15px;
        }
        /* Footer styling */
        .footer {
            text-align: center;
            color: gray;
            margin-top: 40px;
        }
    </style>
    """, unsafe_allow_html=True
)

# Application Header
st.markdown("<div class='main-header'>🏦 Loan Approval Prediction System</div>", unsafe_allow_html=True)

st.write("---")

# About the Application
st.markdown(
    """
    ### 🌟 About the Application

    The **Loan Approval Prediction System** leverages advanced machine learning techniques to assess applicant data and predict loan approval outcomes with accuracy and efficiency.
    """
)

# Features Section Introduction
st.markdown(
    """
    <div class='features-section'>
        <div class='features-title'>🔍 Features Used in Prediction</div>
        <p style="color: red; font-size: 18px;">Here are the characteristics that determine whether your loan gets approved or not:</p>
    </div>
    """, unsafe_allow_html=True
)

# Feature Columns Explanation
features = [
    {"name": "Age of the Applicant", "description": "The age of the individual applying for the loan."},
    {"name": "Gender of the Applicant", "description": "The gender of the applicant (e.g., Male, Female)."},
    {"name": "Person Education", "description": "The highest education level attained by the applicant."},
    {"name": "Person income", "description": "The monthly or annual income of the applicant."},
    {"name": "Person Emp Exp", "description": "The total years of employment experience."},
    {"name": "Person Home Ownership", "description": "Indicates whether the applicant owns a home, rents, or lives with others."},
    {"name": "Loan Amount", "description": "The amount of money the applicant is requesting."},
    {"name": "Loan Intent", "description": "The purpose or intent of the loan (e.g., Education, Medical, Personal, etc.)."},
    {"name": "Loan Int_rate", "description": "The interest rate applied to the loan."},
    {"name": "Loan Percent Income", "description": "The percentage of the applicant’s income that will go toward loan repayment."},
    {"name": "Credit History", "description": "The length of the applicant’s credit history in years."},
    {"name": "Credit Score", "description": "A numerical score representing the applicant’s creditworthiness."},
    {"name": "Previous loan defaults on file", "description": "Indicates if the applicant has any prior loan defaults on record (Yes/No)."}
]

# Display features in two columns
col1, col2 = st.columns(2)
for idx, feature in enumerate(features):
    col = col1 if idx % 2 == 0 else col2
    col.markdown(
        f"""
        <div style="margin-bottom: 15px;">
            <b>{feature['name']}:</b> <br> {feature['description']}
        </div>
        """, unsafe_allow_html=True
    )

# Key Features of the App
st.markdown(
    """
    <div class='features-section'>
        <div class='features-title'>✨ Key Features of the App</div>
        <ul>
            <li><b style="color: green; font-size: 18px;">Real-Time Loan Approval Prediction:</b> Instantly assess loan eligibility based on user input.</li>
            <li><b style="color: green; font-size: 18px;">User-Friendly Interface:</b> Clean and intuitive layout designed for ease of use.</li>
            <li><b style="color: green; font-size: 18px;">Detailed Input Guidance:</b> Tooltips and explanations for every input field to assist users.</li>
            <li><b style="color: green; font-size: 18px;">Advanced ML Models:</b> Compares ANN and XGBoost for robust, data-driven predictions.</li>
            <li><b style="color: green; font-size: 18px;">Performance Insights:</b> Visual feedback on model performance and prediction confidence.</li>
            <li><b style="color: green; font-size: 18px;">Responsive Design:</b> Works seamlessly across devices—mobile, tablet, and desktop.</li>
            <li><b style="color: green; font-size: 18px;">Educational Value:</b> Learn how each feature influences loan approval decisions.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True
)

# Footer
st.markdown("---")
st.markdown(
    """
    <div class='footer' style='text-align: center; font-size: 14px; color: gray;'>
        <p>🔍 Powered by <b>Streamlit</b> | Created with by <b>Raj Chandravanshi</b></p>
    </div>
    """, unsafe_allow_html=True
)
