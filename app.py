import streamlit as st

st.set_page_config(
    page_title="LegalEase",
    page_icon="⚖️",
    layout="centered"
)

st.markdown(
    """
    <style>

    .stApp {
        background: linear-gradient(135deg, #0b1220 0%, #111827 50%, #0f172a 100%);
    }

    .block-container {
        max-width: 900px;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }

    .main-title {
        text-align: center;
        font-size: 52px;
        font-weight: 800;
        letter-spacing: -1px;
        margin-bottom: 5px;
        color: #f8fafc;
    }

    .subtitle {
    text-align: center;
    font-size: 18px;
    color: #94a3b8;
    margin-top: 0;
    margin-bottom: 45px;
    width: 100%;
    position: relative;
    left: 15px;
}

    .section-title {
        font-size: 28px;
        font-weight: 700;
        color: #f8fafc;
        margin-bottom: 20px;
    }

    .legal-card {
        background: rgba(30, 41, 59, 0.75);
        border: 1px solid rgba(148, 163, 184, 0.18);
        border-radius: 18px;
        padding: 30px;
        margin-bottom: 25px;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.25);
    }

    .stButton > button {
        width: 100%;
        border-radius: 12px;
        height: 52px;
        font-size: 16px;
        font-weight: 700;
        border: none;
        background: #2563eb;
        color: white;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        background: #1d4ed8;
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(37, 99, 235, 0.35);
    }

    .stDownloadButton > button {
        width: 100%;
        border-radius: 12px;
        height: 50px;
        font-size: 15px;
        font-weight: 700;
    }

    .footer {
        text-align: center;
        color: #64748b;
        font-size: 13px;
        margin-top: 40px;
        padding-top: 20px;
        border-top: 1px solid rgba(148, 163, 184, 0.12);
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main-title">⚖️ LegalEase</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">AI-Powered Legal Document Generator</div>',
    unsafe_allow_html=True
)

st.subheader("Create Your Legal Document")

document_type = st.selectbox(
    "Select Document Type",
    [
        "Rental Agreement",
        "Leave Letter",
        "Legal Notice"
    ]
)

st.write("You selected:", document_type)

name = st.text_input("Enter your name")
address = st.text_area("Enter your address")
date = st.date_input("Select date")

if document_type == "Leave Letter":
    reason = st.text_area("Enter reason for leave")

elif document_type == "Legal Notice":
    issue = st.text_area("Enter the legal issue")

if st.button("Generate Document"):

    if document_type == "Rental Agreement":

        document = f"""
        RENTAL AGREEMENT

        Name: {name}
        Address: {address}
        Date: {date}

        This agreement is made between the concerned parties
        for the purpose of renting the mentioned property.

        Both parties agree to follow the terms and conditions
        of the rental agreement.

        Signature: ______________
        """

    elif document_type == "Leave Letter":

        document = f"""
        LEAVE LETTER

        From: {name}
        Address: {address}
        Date: {date}

        Subject: Leave Request

        I, {name}, request leave due to {reason}.

        Kindly consider my request.

        Thank you.

        Signature: ______________
        """

    else:

        document = f"""
        LEGAL NOTICE

        Name: {name}
        Address: {address}
        Date: {date}

        Subject: Legal Notice

        This notice is regarding the following legal issue:

        {issue}

        The concerned person is requested to take
        appropriate action.

        Signature: ______________
        """

    st.subheader("Generated Document")
    st.text_area("Document Preview", document, height=400)

    st.download_button(
    label="⬇️ Download Document",
    data=document,
    file_name=f"{document_type.replace(' ', '_')}.txt",
    mime="text/plain"
)