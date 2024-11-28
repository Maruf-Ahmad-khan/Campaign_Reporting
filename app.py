import streamlit as st
import pandas as pd
import plotly.express as px

# Set up the Streamlit app layout
st.set_page_config(page_title="Campaign Reporting", layout="wide")

# Sidebar for branding/logo
with st.sidebar:
    st.image("pic.png", caption="Campaign Reporting")
    st.write("Upload your data to analyze campaigns.")

# File upload
uploaded_file = st.file_uploader("Upload your data (CSV format)", type=["csv"])

if uploaded_file:
    # Load data
    df = pd.read_csv(uploaded_file)

    # Ensure the necessary columns exist
    required_columns = ["Campaign_Name", "Partner", "Inventory", "Status", 
                        "Payout", "Amount", "Date"]
    if not all(col in df.columns for col in required_columns):
        st.error(f"Your data must contain these columns: {', '.join(required_columns)}")
    else:
        # Convert Date to datetime for proper processing
        df['Date'] = pd.to_datetime(df['Date'])

        # Total Metrics
        total_payout = df['Payout'].sum()
        total_sales = df['Amount'].sum()
        first_currency = "INR"

        # Slicers for filtering data
        st.sidebar.header("Filters")
        selected_partner = st.sidebar.multiselect("Select Partner", df['Partner'].unique(), default=df['Partner'].unique())
        selected_status = st.sidebar.multiselect("Select Status", df['Status'].unique(), default=df['Status'].unique())
        selected_campaign = st.sidebar.multiselect("Select Campaign", df['Campaign_Name'].unique(), default=df['Campaign_Name'].unique())

        # Apply filters
        filtered_data = df[(df['Partner'].isin(selected_partner)) & 
                           (df['Status'].isin(selected_status)) & 
                           (df['Campaign_Name'].isin(selected_campaign))]

        # Metrics Header
        col1, col2, col3 = st.columns(3)
        col1.metric("Sum of Payout", f"{total_payout:,.2f}")
        col2.metric("First Currency", first_currency)
        col3.metric("Total Sales", f"{total_sales:,.2f}")

        # Main Charts
        st.markdown("### Total Payout and Total Sales by Date")
        time_chart_data = filtered_data.groupby('Date').agg({'Payout': 'sum', 'Amount': 'sum'}).reset_index()

        # Line chart
        time_fig = px.line(time_chart_data, x='Date', y=['Payout', 'Amount'], 
                           labels={'value': 'Amount', 'variable': 'Metric'}, 
                           title="Total Payout and Sales by Date",
                           color_discrete_sequence=['#636EFA', '#EF553B'])
        st.plotly_chart(time_fig, use_container_width=True)

        # Horizontal Bar Charts
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Sum of Payout by Partner")
            partner_chart_data = filtered_data.groupby('Partner').agg({'Payout': 'sum'}).reset_index()
            partner_fig = px.bar(partner_chart_data, x='Payout', y='Partner', orientation='h', text='Payout')
            st.plotly_chart(partner_fig, use_container_width=True)

        with col2:
            st.markdown("### Sum of Payout by Campaign_Name")
            campaign_chart_data = filtered_data.groupby('Campaign_Name').agg({'Payout': 'sum'}).reset_index()
            campaign_fig = px.bar(campaign_chart_data, x='Payout', y='Campaign_Name', orientation='h', text='Payout')
            st.plotly_chart(campaign_fig, use_container_width=True)

        # Donut Charts
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Sum of Payout by Status")
            status_chart_data = filtered_data.groupby('Status').agg({'Payout': 'sum'}).reset_index()
            status_fig = px.pie(status_chart_data, values='Payout', names='Status', hole=0.5)
            st.plotly_chart(status_fig, use_container_width=True)

        with col2:
            st.markdown("### Total Payout by Inventory")
            inventory_chart_data = filtered_data.groupby('Inventory').agg({'Payout': 'sum'}).reset_index()
            inventory_fig = px.pie(inventory_chart_data, values='Payout', names='Inventory', hole=0.5)
            st.plotly_chart(inventory_fig, use_container_width=True)

        # Data Table
        st.markdown("### Detailed Data Table")
        st.dataframe(filtered_data)
else:
    st.info("Please upload a CSV file to proceed.")
