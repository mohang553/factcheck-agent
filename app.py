import streamlit as st
import pandas as pd

from utils.pdf_parser import extract_pdf_text
from utils.claim_extractor import extract_claims
from utils.verifier import verify_claim

st.set_page_config(
    page_title="FactCheck Agent",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 FactCheck Agent")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    pdf_text = extract_pdf_text(uploaded_file)

    st.success("PDF Parsed Successfully")

    if st.button("Start Fact Checking"):

        with st.spinner("Extracting claims..."):

            claims_data = extract_claims(pdf_text)

        if not claims_data:

            st.error("No claims extracted")

        else:

            results = []

            progress = st.progress(0)

            total_claims = len(claims_data)

            for index, item in enumerate(claims_data):

                claim = item["claim"]

                result = verify_claim(claim)

                results.append(result)

                progress.progress(
                    (index + 1) / total_claims
                )

            df = pd.DataFrame(results)

            verified = len(
                df[df["status"] == "VERIFIED"]
            )

            inaccurate = len(
                df[df["status"] == "INACCURATE"]
            )

            false = len(
                df[df["status"] == "FALSE"]
            )

            st.subheader(
                "Executive Summary"
            )

            col1, col2, col3, col4 = st.columns(4)

            col1.metric(
                "Total Claims",
                len(df)
            )

            col2.metric(
                "Verified",
                verified
            )

            col3.metric(
                "Inaccurate",
                inaccurate
            )

            col4.metric(
                "False",
                false
            )

            st.divider()

            st.subheader(
                "Detailed Report"
            )

            for _, row in df.iterrows():

                st.write("---")

                st.write(
                    f"### {row['status']}"
                )

                st.write(
                    f"**Claim:** {row['claim']}"
                )

                st.write(
                    f"**Confidence:** {row['confidence']}%"
                )

                st.progress(
                    min(
                        int(row['confidence']),
                        100
                    )
                )

                st.write(
                    f"**Explanation:** {row['explanation']}"
                )

                st.write(
                    f"**Correct Fact:** {row['correct_fact']}"
                )

                if row["source_url"]:

                    st.markdown(
                        f"🔗 [Source]({row['source_url']})"
                    )

            st.divider()

            st.subheader("Raw Results")

            st.dataframe(
                df,
                use_container_width=True
            )

            csv = df.to_csv(
                index=False
            )

            st.download_button(
                "Download Report",
                csv,
                file_name="factcheck_report.csv",
                mime="text/csv"
            )