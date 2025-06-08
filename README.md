# 🛬 Flights SQL Analytics App

A Streamlit-based web app for exploring and analyzing flight data. Users can filter flights by source, destination, and date, view airline trends, and visualize data using charts. The backend is powered by MySQL.

---

## ✨ Features

* Search available flights by source, destination, and date.
* Visualize airline frequency using a pie chart.
* Analyze busiest airports using a bar chart.
* Track daily flight trends with a line chart.

---

## ⚙️ Installation

Follow these steps to set up and run the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/yuvrajsinghshek/flights_sql_streamlit_app.git
cd flights_sql_streamlit_app
```

### 2. Set up Python Environment

Ensure Python 3.12.5 is installed. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
DB_HOST=127.0.0.1
DB_PORT=3307
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=flights
```

> **Note:** Keep your `.env` file private. Don't upload it to GitHub.

### 5. Set Up the Database

* Create a MySQL database named `flights`
* Import the flights dataset using a provided `.sql` file (if available)

### 6. Run the App

```bash
streamlit run C:\Users\yuvra\PycharmProjects\firstProject\flights_sql_app\app.py
```

---

## 🔍 Project Structure

```bash
flights_sql_app/
├── app.py              # Main Streamlit app
├── dbhelper.py         # Database helper class for queries
├── .env                # Environment variables (not uploaded)
├── requirements.txt    # Python dependencies
└── README.md           # Project overview
```

---

## 🔗 Connect with Me

**Yuvraj Singh Shekhawat**
[LinkedIn](https://www.linkedin.com/in/yuvraj-singh-shekhawat-155719316)

---

## 🚀 Future Improvements

* User login system
* Export data as CSV
* Advanced filters (time range, price range)

---

## ✉️ License

This project is for learning/demo purposes and is not intended for production use.

