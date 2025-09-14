import streamlit as st
import tempfile
from manager import PortfolioWorkflow
from utils.input_converter import InputConverter

# Initialize manager and converter
manager = PortfolioWorkflow()
converter = InputConverter()

# === Page Config ===
st.set_page_config(
    page_title="PortfoliAI",
    layout="wide",
    initial_sidebar_state="expanded"
)

# === Sidebar ===
st.sidebar.image("logo.png", width=150)
st.sidebar.title("PortfoliAI")
st.sidebar.markdown("""
Welcome to **PortfoliAI**, your AI-powered portfolio assistant.  
Upload a CSV or PDF of your portfolio to analyze it, assess risks, and get recommendations.
""")
st.sidebar.markdown("---")
st.sidebar.markdown("Made with ❤️ using Streamlit & AI Agents")

# === Main Title ===
st.title("📊 PortfoliAI: AI Portfolio Assistant")

# File uploader
uploaded_file = st.file_uploader("Upload your Portfolio File (CSV / PDF)", type=["csv", "pdf"])

if uploaded_file:
    if uploaded_file:
        # Save file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp:
            tmp.write(uploaded_file.getvalue())
            tmp_path = tmp.name

        # Convert the file into Markdown / table text
        try:
            portfolio_data = converter.convert(tmp_path)
            st.success("✅ File converted successfully!")
        except Exception as e:
            st.error(f"Error converting file: {e}")
            st.stop()

    # Run the workflow
    with st.spinner("Analyzing portfolio with AI agents..."):
        results = manager.run_sync(portfolio_data)

    # Display results in **expanders** with nice markdown styling
    for section, value in results.items():
        with st.expander(section, expanded=True):
            st.markdown(value if value else "No data available")

# Footer
st.markdown("---")
st.markdown("**PortfoliAI** - AI-powered portfolio assistant. Made with ❤️ by Deep Nagpal")
