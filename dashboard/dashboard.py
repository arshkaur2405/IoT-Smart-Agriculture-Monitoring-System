import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_autorefresh import st_autorefresh

import sys
import os

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.append(project_root)

from src.analytics import Analytics

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="Smart Agriculture Monitoring",
    page_icon="🌾",
    layout="wide"
)

# Auto Refresh Every 5 Seconds
st_autorefresh(interval=5000, key="dashboard_refresh")

# -----------------------------
# LOAD DATA
# -----------------------------

file_path = "data/agriculture_data.csv"

if not os.path.exists(file_path):
    st.error("No sensor data found. Run app.py first.")
    st.stop()

if os.path.getsize(file_path) == 0:
    st.error("CSV file is empty. Run app.py first.")
    st.stop()

df = pd.read_csv(file_path)

if df.empty:
    st.error("No sensor data available.")
    st.stop()

latest = df.iloc[-1]
st.sidebar.metric(
    "📄 Stored Records",
    len(df)
)

# -----------------------------
# HEADER
# -----------------------------

st.title("🌾 IoT Smart Agriculture Monitoring System")

st.markdown("""
Real-Time Farm Monitoring • Automated Irrigation • Smart Alerts • Analytics Dashboard
""")

st.divider()

# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.title("🚨 Alert Center")

alerts = str(latest["alerts"])

if "Low Soil Moisture" in alerts:
    st.sidebar.error("🌱 Low Soil Moisture")

if "High Temperature" in alerts:
    st.sidebar.warning("🌡 High Temperature")

if "Low Water Tank Level" in alerts:
    st.sidebar.error("🚰 Low Water Tank Level")

if alerts == "Normal":
    st.sidebar.success("✅ No Active Alerts")

st.sidebar.info(
    f"Last Update\n\n{latest['timestamp']}"
)

# -----------------------------
# FARM HEALTH
# -----------------------------

health = Analytics.calculate_farm_health(df)

status_col1, status_col2 = st.columns([1, 2])

with status_col1:

    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=health,
        title={'text': "Farm Health Score"},
        gauge={
            'axis': {'range': [0, 100]}
        }
    ))

    st.plotly_chart(
        gauge,
        use_container_width=True
    )

with status_col2:

    if health >= 80:
        st.success("🟢 Farm Status: Healthy")

    elif health >= 50:
        st.warning("🟡 Farm Status: Moderate")

    else:
        st.error("🔴 Farm Status: Critical")

    st.info(
        f"💡 Recommendation:\n\n{latest['recommendation']}"
    )

# -----------------------------
# KPI SECTION
# -----------------------------

st.subheader("📊 Live Sensor Metrics")

avg_temp = df["temperature"].mean()
avg_humidity = df["humidity"].mean()
avg_soil = df["soil_moisture"].mean()
avg_water = df["water_level"].mean()

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "🌱 Soil Moisture",
    f"{latest['soil_moisture']}%",
    f"{latest['soil_moisture'] - avg_soil:.1f}"
)

col2.metric(
    "🌡 Temperature",
    f"{latest['temperature']}°C",
    f"{latest['temperature'] - avg_temp:.1f}"
)

col3.metric(
    "💧 Humidity",
    f"{latest['humidity']}%",
    f"{latest['humidity'] - avg_humidity:.1f}"
)

col4.metric(
    "☀ Light",
    latest["light_intensity"]
)

col5.metric(
    "🚰 Water Level",
    f"{latest['water_level']}%",
    f"{latest['water_level'] - avg_water:.1f}"
)

# -----------------------------
# PUMP STATUS
# -----------------------------

if latest["pump_status"] == "ON":
    st.error("⚙ Pump Status : ON")
else:
    st.success("⚙ Pump Status : OFF")

# -----------------------------
# ALERT PANEL
# -----------------------------

st.subheader("🚨 Current Alerts")

if alerts == "Normal":
    st.success("No Active Alerts")
else:
    st.warning(alerts)

# -----------------------------
# ANALYTICS
# -----------------------------

st.subheader("📈 Farm Analytics")

a1, a2, a3 = st.columns(3)

a1.metric(
    "Average Temperature",
    f"{avg_temp:.2f} °C"
)

a2.metric(
    "Average Humidity",
    f"{avg_humidity:.2f} %"
)

a3.metric(
    "Average Soil Moisture",
    f"{avg_soil:.2f} %"
)

# -----------------------------
# CHARTS
# -----------------------------

st.subheader("📉 Sensor Trends")

chart1, chart2 = st.columns(2)

with chart1:

    fig = px.line(
        df,
        y="soil_moisture",
        title="Soil Moisture Trend"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with chart2:

    fig = px.line(
        df,
        y="temperature",
        title="Temperature Trend"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

chart3, chart4 = st.columns(2)

with chart3:

    fig = px.line(
        df,
        y="humidity",
        title="Humidity Trend"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with chart4:

    fig = px.line(
        df,
        y="water_level",
        title="Water Level Trend"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -----------------------------
# SENSOR STATUS
# -----------------------------

st.subheader("🔧 Sensor Health")

sensor_status = pd.DataFrame({
    "Sensor": [
        "Soil Moisture",
        "Temperature",
        "Humidity",
        "Light Intensity",
        "Water Level"
    ],
    "Status": [
        "Online",
        "Online",
        "Online",
        "Online",
        "Online"
    ]
})

st.dataframe(
    sensor_status,
    use_container_width=True
)

# -----------------------------
# RECENT DATA
# -----------------------------

st.subheader("📋 Latest Sensor Records")

st.dataframe(
    df.tail(50),
    use_container_width=True,
    height=500
)

# -----------------------------
# DOWNLOAD REPORT
# -----------------------------

csv = df.to_csv(index=False)

st.download_button(
    label="📥 Download Agriculture Report",
    data=csv,
    file_name="smart_agriculture_report.csv",
    mime="text/csv"
)
# ..