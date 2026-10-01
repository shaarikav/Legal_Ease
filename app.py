import streamlit as st

st.title("LegalEase")
st.write("AI-Powered Legal Document Generator")

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