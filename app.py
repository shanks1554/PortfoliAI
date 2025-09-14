import streamlit as st
import tempfile
from manager import PortfolioWorkflow
from utils.input_converter import InputConverter

# Initialize manager and converter
manager = PortfolioWorkflow()
converter = InputConverter()

st.set_page_config(page_title="Portfolio AI Assistant", layout="wide")
st.title("📊 PortfoliAI Assistant")

st.markdown("""
Upload your **portfolio CSV or PDF file**. 
The system will analyze your portfolio, assess risks, perform research, and generate recommendations.
""")

# File uploader
uploaded_file = st.file_uploader("Upload your Portfolio (CSV or PDF)", type=["csv", "pdf"])

if uploaded_file:
    # Save file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp:
        tmp.write(uploaded_file.getvalue())
        tmp_path = tmp.name

    # Convert the file into Markdown / table text
    try:
        portfolio_data = converter.convert(tmp_path)
    except Exception as e:
        st.error(f"Error converting file: {e}")
        st.stop()

    st.success("✅ File converted successfully!")

    # Run the workflow (sync wrapper)
    with st.spinner("Analyzing portfolio..."):
        results = manager.run_sync(portfolio_data)

    # Display results in tabs
    tabs = st.tabs([
        "📈 Portfolio Analysis",
        "⚠️ Risks",
        "🔍 Research",
        "🔎 Risk Research",
        "✅ Recommendations"
    ])

    with tabs[0]:
        st.markdown(results["Portfolio Analysis"])

    with tabs[1]:
        st.markdown(results["Portfolio Risk"])

    with tabs[2]:
        st.markdown(results["Portfolio Research"])

    with tabs[3]:
        st.markdown(results["Risk Research"])

    with tabs[4]:
        st.markdown(results["Recommendation"])

    # Optional: allow user to download results as text file
    if st.button("💾 Download All Results"):
        output_text = ""
        for section, value in results.items():
            output_text += f"--- {section} ---\n{value}\n\n"

        st.download_button(
            label="Download Results",
            data=output_text,
            file_name="portfolio_analysis.txt",
            mime="text/plain"
        )
