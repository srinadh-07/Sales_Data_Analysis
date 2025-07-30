
# 📊 Interactive Sales Dashboard

An interactive web dashboard built using **Dash**, **Plotly**, and **Pandas** to visualize and analyze sales data. It offers a dynamic way to explore trends, identify top-performing products, and understand customer behavior.

---

## 🧹 Key Data Cleaning Tasks

- Converted date columns to datetime format
- Extracted month from date for time-based analysis
- Standardized text fields (e.g., stripping whitespaces from city names)
- Filtered records to remove missing or inconsistent entries
- Aggregated sales metrics by product, category, city, and customer

---

## 🧰 Tools & Libraries

- **Pandas** – Data manipulation and cleaning
- **Plotly Express** – Interactive visualizations
- **Dash** – Web-based dashboard framework
- **Seaborn & Matplotlib** – Statistical and heatmap plots
- **Jupyter Notebook** – Exploratory analysis

---

## 🚀 Features

This dashboard includes multiple interactive visualizations for exploring sales data:

### 🧩 1. Overall Sales Composition
- ✅ Category-wise Sales Share (Pie Chart)
- ✅ Sales Breakdown by Category and Product (Treemap)

### 📦 2. Product-Level Insights
- ✅ Total Sales by Product (Bar Chart)
- ✅ Product Popularity by Quantity Sold (Bar Chart)

### 📁 3. Category-Level Insights
- ✅ Total Sales by Category (Bar Chart)

### 📅 4. Time-Based Analysis
- ✅ Monthly Sales Trend (Line Chart)
- ✅ Monthly Sales by Category (Grouped Bar Chart)

### 🌆 5. Geographic Insights
- ✅ Top Cities by Sales (Bar Chart)

### 💳 6. Payment Method Insights
- ✅ Payment Method Usage (Bar Chart / Histogram)
- ✅ Payment Method Share (Pie Chart)

### 👤 7. Customer Insights
- ✅ Top 10 Customers by Spending (Bar Chart)

### 🔍 8. Advanced Relationship Analysis
- ✅ Unit Price vs Quantity Sold (Scatter Plot)
- ✅ Correlation Heatmap (Seaborn)

---


## 📂 Project Structure

```
project/
│
├── app.py                # Main Dash app
├── data.csv              # Sales dataset
├── assets/               # Optional: CSS files
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```


## 👨‍💻 Author

**Srinadh kumar Kadimi**  
🔗 [GitHub](https://github.com/srinadh-07) • 📧 srinadhkadimi07@gmail.com

---

## 🚀 Future Improvements

- Add filtering options (e.g., dropdowns for product/category)
- Deploy the dashboard to the web (Heroku, Render, etc.)
- Integrate real-time data sources or database connection
- Add download/export functionality for charts
- Improve UI/UX with responsive layout and theming

