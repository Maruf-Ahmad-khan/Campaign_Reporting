import streamlit as st
import streamlit.components.v1 as components  # Explicit import for components.v1

# Set page title
st.set_page_config(
    page_title="Power BI Dashboard",
    layout="wide",  # Use the wide layout for better utilization of screen space
)

# Add title
st.title("Power BI Reports")

# Define Power BI report URLs
reports = {
    "September Report": "https://app.powerbi.com/reportEmbed?reportId=58b4b286-da86-44f6-979e-14efc19b7212&autoAuth=true&ctid=4a36bb2f-1c55-49e0-9a23-6281dfd38c6b",
    "August Report": "https://app.powerbi.com/reportEmbed?reportId=57a1cc5f-5d11-4400-a391-82f1f3d352d5&autoAuth=true&ctid=4a36bb2f-1c55-49e0-9a23-6281dfd38c6b",
    "Yearly Summary": "https://app.powerbi.com/reportEmbed?reportId=763b29b9-4f76-48da-a780-f47e63d3fc46&autoAuth=true&ctid=4a36bb2f-1c55-49e0-9a23-6281dfd38c6b",
    "June Report" : "https://app.powerbi.com/reportEmbed?reportId=e609513b-7811-4f36-bf3d-bf191f67c5c0&autoAuth=true&ctid=4a36bb2f-1c55-49e0-9a23-6281dfd38c6b"
}

# Create tabs for each report
tab1, tab2, tab3, tab4 = st.tabs(["September Report", "August Report", "Yearly Summary", "June Report"])

# Embed each report in its respective tab
with tab1:
    st.subheader("September Report")
    html_code = f"""
    <iframe 
        title="September Report" 
        width="100%" 
        height="600" 
        src="{reports['September Report']}" 
        frameborder="0" 
        allowFullScreen="true">
    </iframe>
    """
    components.html(html_code, height=600)

with tab2:
    st.subheader("August Report")
    html_code = f"""
    <iframe 
        title="August Report" 
        width="100%" 
        height="600" 
        src="{reports['August Report']}" 
        frameborder="0" 
        allowFullScreen="true">
    </iframe>
    """
    components.html(html_code, height=600)

with tab3:
    st.subheader("Yearly Summary")
    html_code = f"""
    <iframe 
        title="Yearly Summary" 
        width="100%" 
        height="600" 
        src="{reports['Yearly Summary']}" 
        frameborder="0" 
        allowFullScreen="true">
    </iframe>
    """
    components.html(html_code, height=600)
    
    
with tab4:
    st.subheader("June Report")
    html_code = f"""
    <iframe 
        title="June Report" 
        width="100%" 
        height="600" 
        src="{reports['June Report']}" 
        frameborder="0" 
        allowFullScreen="true">
    </iframe>
    """
    components.html(html_code, height=600)
