import streamlit as st
import subprocess
import time

# Set up the page with a custom logo and layout
st.set_page_config(
    page_title="Automation Launcher",
    layout="centered"
)

# 🔼 Display Logo (replace with your own file or URL)
st.image("Billgosling.png", width=200)  # Make sure logo.png is in the same folder
# App Title
st.title("⚙️ Automation Runner Web App")

# ▶️ Button to Run Automation
if st.button("▶️ Run Automation"):
    st.info("🚀 Running your automation script...")

    # Show a spinner and progress bar
    with st.spinner("Processing... Please wait"):
        progress_bar = st.progress(0)

        # Simulate progress while the script runs
        for percent in range(0, 100, 10):
            time.sleep(0.2)  # You can adjust this or tie it to subprocess
            progress_bar.progress(percent + 10)

        try:
            result = subprocess.run(
                ["python", "TLC_ADT_Automation.py"],
                capture_output=True,
                text=True
            )
            st.success("✅ Script finished running!")
            st.text(result.stdout)
        except Exception as e:
            st.error("❌ Something went wrong!")
            st.text(str(e))

    progress_bar.empty()  # remove progress bar after completion