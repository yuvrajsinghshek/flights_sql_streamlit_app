import streamlit as st
from dbhelper import DB
import plotly.graph_objects as go
import plotly.express as px

db = DB()

# 1) sidebar
st.sidebar.title('Flights Analytics')

# 2) sidebar 'menu' dropdown toggle
user_option = st.sidebar.selectbox('Menu', ['About Project', 'Check Flights', 'Flights Analytics'])

# 3) conditions for opening page
if user_option == 'Check Flights':
    st.title('Check Flights')

    col1,col2,col3 = st.columns(3)       # for 2 dropdown side wise

    city = db.fetch_city_names()
    with col1:
        source = st.selectbox('Source',sorted(city))
    with col2:
        destination = st.selectbox('Destination', sorted(city))

    dates = db.date_of_flights()
    date_map = {formatted: original for original, formatted in dates}
    with col3:
        selected_formatted = st.selectbox('Date', sorted(date_map.keys()))

    selected_original = date_map[selected_formatted]

    if st.button('Search'):
        result = db.fetch_all_flights(source, destination, selected_original)
        if result is not None and not result.empty:
            st.dataframe(result)
        else:
            st.warning("No flights available for the selected route and date.")

elif user_option == 'Flights Analytics':
    st.title('Flights Analytics')

    airline, frequency = db.fetch_airline_frequency()

    # 1. Pie chart by using plotly
    fig = go.Figure(
        go.Pie(
            labels = airline,
            values = frequency,
            hoverinfo="label+percent",
            textinfo = "value"
        )
    )
    st.header("Pie Chart")
    st.plotly_chart(fig)

    # 2. Bar Chart for busiest Airport
    city, frequency1 = db.busy_airport()

    fig = px.bar(
        x=city,
        y=frequency1,
        labels={'x': 'Airport City', 'y': 'Total Flights'},
        title='Total Flights by Airport City'
    )
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig, theme = "streamlit", user_container_width = True)

    # 3. Line Chart on basis of date
    date, count = db.daily_frequency()

    fig = px.line(
        x=date,
        y=count,
        labels={'x': 'Date of Flights', 'y': 'Total Flights'},
        title='Total Flights by Date'
    )
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig, theme="streamlit", user_container_width=True)


else:
    st.title('Project Overview')
    st.markdown("""
        ## ✨ About the Project

        This is a **Flight Booking and Analytics Dashboard** built using **Streamlit, Plotly, and MySQL**.  
        It simulates how users can explore flight availability and view flight-related analytics.

        ---

        ## 📂 Dataset Description

        - Data is **historical** and used only for **project/demo purposes**
        - Includes fields like:
            - `Airline`, `Source`, `Destination`
            - `Date of Journey`, `Departure Time`, `Duration`, `Price`

        ⚠️ **Note:** This app does not show future flights, as it uses static past data.

        ---

        ## 💡 Key Features

        ✅ **Check Flights**  
        - Select **Source**, **Destination**, and **Date** to view available flights

        📊 **Flight Analytics**  
        - Pie Chart: Flight distribution by airline  
        - Bar Chart: Busiest airport cities  
        - Line Chart: Total flights per date

        ---

        ## ⚙️ Tech Stack

        - **Frontend**: Streamlit + Plotly
        - **Backend**: MySQL
        - **Language**: Python

        ---

        ## 👨‍💻 Developed by: Yuvraj Singh Shekhawat  
        🔗 [LinkedIn Profile](https://www.linkedin.com/in/yuvraj-singh-shekhawat-155719316)
        """)
