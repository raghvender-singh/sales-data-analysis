# Sales Data Analysis

## Overview

This project analyzes sales data using Python to understand revenue, sales volume, product performance, and city-wise performance.

The analysis includes data cleaning, feature creation, exploratory data analysis, and data visualization using Pandas, Matplotlib, and Seaborn.

## Dataset

The dataset contains sales transactions with information about:

- Order ID
- Date
- Product
- Category
- City
- Quantity
- Unit Price

A Revenue column was created using:

`Revenue = Quantity × Unit Price`

A Month column was also created from the Date column.

## Tools & Technologies

- Python
- Pandas
- Matplotlib
- Seaborn
- VS Code

## Analysis Performed

- Calculated total revenue
- Analyzed revenue by category
- Analyzed revenue by city
- Analyzed revenue by product
- Calculated Average Order Value (AOV) by city
- Analyzed quantity sold by product
- Analyzed total quantity sold by city
- Analyzed average unit price by product and category
- Analyzed monthly revenue
- Created visualizations to identify sales patterns and performance

## Key Business Insights

- Total revenue generated during the analysis period was ₹2,58,300.
- Electronics generated the highest revenue of ₹2,11,000.
- Delhi generated the highest city-wise revenue of ₹1,35,200.
- Lucknow had the highest Average Order Value (AOV) of approximately ₹34,833.
- Laptop generated the highest product revenue of ₹1,65,000.
- Pen had the highest quantity sold, with 20 units.
- Kanpur had the highest total quantity sold, despite generating lower revenue.

## Visualizations

The project includes the following visualizations:

- Revenue by Category
- Revenue by City
- Revenue by Product
- Average Order Value (AOV) by City
- Quantity Sold by Product

## How to Run

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Install the required Python libraries:

```bash
pip install pandas seaborn matplotlib
```

4. Run the Python script:

```bash
python sales_analysis.py
```

## Project Structure

sales_analysis_project/
│
├── README.md
├── sales_analysis.py
└── sales.csv

## Future Improvements

- Add more months of sales data for deeper time-based analysis.
- Build an interactive dashboard using Power BI or Tableau.
- Perform more detailed customer and product-level analysis.
- Add advanced statistical analysis to identify sales trends and patterns.

