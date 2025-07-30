import pandas as pd
import numpy as np 
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import dash
from dash import dcc, html
import io
import base64
df=pd.read_csv(r"D:\vs\uncleaned_sales_data_500.csv")
print(df.head())
print(df.columns)
# print(df.isnull().sum())
df["Product"]=df.groupby("Category")["Product"].transform(lambda x: x.fillna(x.mode()[0])if not x.mode().empty else x)
# print(df.isnull().sum())
df["Quantity"]=df.groupby("Product")["Quantity"].transform(lambda x : x.fillna(x.mode()[0])if not x.mode().empty else x)
# print(df.isnull().sum())
df["Unit_Price"]=df.groupby("Product")["Unit_Price"].transform(lambda x: x.fillna(x.median())if not x.median() is np.nan else x)
# print(df.isnull().sum())
df["Total_Amount"]=df["Quantity"]*df["Unit_Price"]
# print(df[["Quantity", "Unit_Price","Total_Amount"]])
df['Payment_Method'] = df['Payment_Method'].replace({
    'Credit-Card': 'Credit Card',
    'Debit-Card': 'Debit Card',
    'Online Payment': 'Online'
})
# print(df["Payment_Method"].unique())
df["Payment_Method"].fillna(df["Payment_Method"].mode()[0],inplace=True)
# print(df["Payment_Method"].unique())
# print(df["City"].isnull().sum())
df["City"]=df.groupby("Customer_ID")["City"].transform(lambda x: x.fillna(x.mode()[0])if not x.mode().empty else x)
# print(df.isnull().sum())
# print(df["Category"].unique())
df["Category"] = df["Category"].str.lower()
df["Category"] = df["Category"].replace({
    "accessories": "Accessories",
    "accesories": "Accessories",
    "accesory": "Accessories",
    "accersories": "Accessories",
})
df["Category"] = df["Category"].str.title()
# print(df["Category"].unique())
# print(df["City"].unique())
df["Date"]=pd.to_datetime(df["Date"])
# print(df["Date"].dtype)
# print(df["Payment_Method"].unique())
df["Payment_Method"]=df["Payment_Method"].str.upper()
# print(df["Product"].unique())
df["Quantity"]=df["Quantity"].astype(int)
# print(df.shape)
# print(df.describe())
# print(df.info())
# print(df.columns)
df["Product"]=df["Product"].str.title()
df["Payment_Method"]=df["Payment_Method"].str.title()
df["Category"]=df["Category"].str.title()
df["City"]=df["City"].str.title()
# print(df.head())
top_product=df.groupby("Product")["Total_Amount"].sum().sort_values(ascending=False)
print(top_product)
top_product_name = top_product.idxmax()
top_product_sales = top_product.max()
print(f"The top-selling product is: {top_product_name} with total sales of ₹{top_product_sales:,.2f}")




print(df["Category"].unique())
category_sales = df.groupby('Category', as_index=False)['Total_Amount'].sum()
category_sales = category_sales.sort_values('Total_Amount', ascending=False)

fig1 = px.pie(
    category_sales,
    names='Category',
    values='Total_Amount',
    title=' Category-wise Sales Share ',
    hole=0.4,
    color_discrete_sequence=px.colors.qualitative.Set3
)

fig1.update_traces(
    textinfo='percent+label',
    pull=[0.05] * len(category_sales),
    marker=dict(line=dict(color='white', width=2))
)

fig1.update_layout(
    title_font=dict(size=22),
    title_x=0.5,
    showlegend=True,
    legend_title_text='Category',
    font=dict(family='Arial', size=14),
    hoverlabel=dict(bgcolor='white', font_size=13),
    margin=dict(l=40, r=40, t=80, b=80),
    plot_bgcolor='white',
    paper_bgcolor='white'
)


fig2 = px.treemap(
    df,
    path=['Category', 'Product'],
    values='Total_Amount',
    title='🧩 Sales Breakdown by Category and Product🎋',
    color='Category',
    color_discrete_sequence=px.colors.qualitative.Pastel
)

fig2.update_traces(
    root_color='lightgray',
    hovertemplate='<b>%{label}</b><br>Total Sales: $%{value:,.2f}<extra></extra>',
    textinfo='label+value+percent entry'
)

fig2.update_layout(
    margin=dict(t=80, l=40, r=40, b=40),
    title_font=dict(size=22),
    title_x=0.5,
    paper_bgcolor='white',
    plot_bgcolor='white',
    font=dict(family='Arial', size=14)
)




product_sales = df.groupby('Product', as_index=False)['Total_Amount'].sum()
product_sales = product_sales.sort_values('Total_Amount', ascending=False)
fig3= px.bar(
    product_sales,
    x='Product',
    y='Total_Amount',
    color='Product',
    title='🛒 Total Sales by Product📊',
    text=product_sales['Total_Amount'],
    labels={'Product': 'Product', 'Total_Amount': 'Total Sales ($)'}
)

fig3.update_traces(
    texttemplate='$%{text:.2f}',
    textposition='outside',
    marker=dict(line=dict(width=1, color='black'))
)

fig3.update_layout(
    xaxis_title='Product',
    yaxis_title='Total Sales ($)',
    title_font=dict(size=22),
    title_x=0.5,
    uniformtext_minsize=12,
    uniformtext_mode='hide',
    yaxis=dict(tickprefix='$', showgrid=True, gridcolor='lightgray'),
    xaxis=dict(showgrid=False),
    plot_bgcolor='white',
    paper_bgcolor='white',
    font=dict(family='Arial', size=14),
    hoverlabel=dict(bgcolor='white', font_size=13),
    margin=dict(l=40, r=40, t=80, b=80),
    showlegend=False
)



product_qty = df.groupby('Product', as_index=False)['Quantity'].sum()
product_qty = product_qty.sort_values('Quantity', ascending=False)

fig4 = px.bar(
    product_qty,
    x='Product',
    y='Quantity',
    color='Product',
    title='📦 Product Popularity by Quantity Sold📊',
    text=product_qty['Quantity'],
    labels={'Product': 'Product', 'Quantity': 'Units Sold'}
)

fig4.update_traces(
    texttemplate='%{text}',
    textposition='outside',
    marker=dict(line=dict(width=1, color='black'))
)

fig4.update_layout(
    xaxis_title='Product',
    yaxis_title='Units Sold',
    title_font=dict(size=22),
    title_x=0.5,
    uniformtext_minsize=12,
    uniformtext_mode='hide',
    yaxis=dict(showgrid=True, gridcolor='lightgray'),
    xaxis=dict(showgrid=False),
    plot_bgcolor='white',
    paper_bgcolor='white',
    font=dict(family='Arial', size=14),
    hoverlabel=dict(bgcolor='white', font_size=13),
    margin=dict(l=40, r=40, t=80, b=80),
    showlegend=False
)




category_sales = df.groupby('Category', as_index=False)['Total_Amount'].sum()
category_sales = category_sales.sort_values('Total_Amount', ascending=False)
fig5 = px.bar(
    category_sales,
    x='Category',
    y='Total_Amount',
    color='Category',
    title='📦 Total Sales by Product Category 📊',
    text=category_sales['Total_Amount'],
    labels={'Category': 'Product Category', 'Total_Amount': 'Total Sales ($)'}
)
fig5.update_traces(
    texttemplate='$%{text:.2f}',
    textposition='outside',
    marker=dict(line=dict(width=1, color='black')),
    
)
fig5.update_traces(width=0.4)
fig5.update_layout(
    xaxis_title='Product Category',
    yaxis_title='Total Sales ($)',
    title_x=0.5,
    title_font=dict(size=22),
    uniformtext_minsize=12,
    uniformtext_mode='hide',
    yaxis=dict(tickprefix='$', showgrid=True, gridcolor='lightgray'),
    xaxis=dict(showgrid=False),
    plot_bgcolor='white',
    paper_bgcolor='white',
    font=dict(family='Arial', size=14),
    hoverlabel=dict(bgcolor='white', font_size=13),
    margin=dict(l=40, r=40, t=80, b=80),
    showlegend=False
)






df['Month'] = df['Date'].dt.to_period('M').astype(str)
monthly_sales = df.groupby('Month', as_index=False)['Total_Amount'].sum()
monthly_sales['Month'] = pd.to_datetime(monthly_sales['Month'])
monthly_sales = monthly_sales.sort_values('Month')
fig6 = px.line(
    monthly_sales,
    x='Month',
    y='Total_Amount',
    markers=True,
    title='📊 Monthly Sales Trend Over Time📊',
    text=monthly_sales['Total_Amount'],
    labels={'Month': 'Month', 'Total_Amount': 'Total Sales ($)'}
)
fig6.update_traces(
    line=dict(color='royalblue', width=3),
    marker=dict(size=8, color='darkblue'),
    textposition='top center',
    hovertemplate='<b>Month:</b> %{x|%B %Y}<br><b>Total Sales:</b> $%{y:.2f}<extra></extra>'
)
fig6.update_layout(
    xaxis_title='Month',
    yaxis_title='Total Sales ($)',
    title_font=dict(size=22),
    title_x=0.5,
    xaxis=dict(
        tickformat='%b %Y',
        showgrid=True,
        tickangle=45
    ),
    yaxis=dict(
        showgrid=True,
        tickprefix='$',
        ticksuffix='',
        gridcolor='lightgray'
    ),
    plot_bgcolor='white',
    font=dict(family='Arial', size=14),
    hoverlabel=dict(bgcolor='white', font_size=13),
    margin=dict(l=40, r=40, t=80, b=80)
)






df['Month'] = pd.to_datetime(df['Date']).dt.to_period('M').astype(str)
monthly_category = df.groupby(['Month', 'Category'])['Total_Amount'].sum().reset_index()
monthly_category['Month'] = pd.to_datetime(monthly_category['Month'])
monthly_category = monthly_category.sort_values('Month')

fig7 = px.bar(
    monthly_category,
    x='Month',
    y='Total_Amount',
    color='Category',
    barmode='group',
    title='📆 Monthly Sales by Category 📊',
    labels={'Month': 'Month', 'Total_Amount': 'Total Sales ($)'}
)

fig7.update_layout(
    xaxis=dict(
        tickformat='%b %Y',
        tickangle=45,
        showgrid=True,
        gridcolor='lightgray'
    ),
    yaxis=dict(
        tickprefix='$',
        showgrid=True,
        gridcolor='lightgray'
    ),
    title_font=dict(size=22),
    title_x=0.5,
    plot_bgcolor='white',
    paper_bgcolor='white',
    font=dict(family='Arial', size=14),
    hoverlabel=dict(bgcolor='white', font_size=13),
    margin=dict(l=40, r=40, t=80, b=80)
)








city_sales = df.groupby('City', as_index=False)['Total_Amount'].sum()
city_sales = city_sales.sort_values(by='Total_Amount', ascending=False)

fig9 = px.bar(
    city_sales,
    x='City',
    y='Total_Amount',
    color='City',
    title='🌆 Top Cities by Total Sales',
    text=city_sales['Total_Amount'],
    labels={'City': 'City', 'Total_Amount': 'Total Sales ($)'}
)

fig9.update_traces(
    texttemplate='$%{text:.2f}',
    textposition='outside',
    marker=dict(line=dict(width=1, color='black'))
)
fig9.update_traces(width=0.4)
fig9.update_layout(
    xaxis_title='City',
    yaxis_title='Total Sales ($)',
    title_font=dict(size=22),
    title_x=0.5,
    uniformtext_minsize=12,
    uniformtext_mode='hide',
    yaxis=dict(tickprefix='$', showgrid=True, gridcolor='lightgray'),
    xaxis=dict(showgrid=False),
    plot_bgcolor='white',
    paper_bgcolor='white',
    font=dict(family='Arial', size=14),
    hoverlabel=dict(bgcolor='white', font_size=13),
    margin=dict(l=40, r=40, t=80, b=80),
    showlegend=False
)






payment_counts = df['Payment_Method'].value_counts().reset_index()
payment_counts.columns = ['Payment_Method', 'Count']
fig10 = px.pie(
    payment_counts,
    names='Payment_Method',
    values='Count',
    title='💳 Payment Method Usage Share',
    hole=0.4,
    color_discrete_sequence=px.colors.qualitative.Set3
)
fig10.update_traces(
    textinfo='percent+label',
    pull=[0.05]*len(payment_counts),
    marker=dict(line=dict(color='white', width=2))
)

fig10.update_layout(
    title_font=dict(size=22),
    title_x=0.5,
    showlegend=True,
    legend_title_text='Payment Method',
    font=dict(family='Arial', size=14),
    hoverlabel=dict(bgcolor='white', font_size=13),
    margin=dict(l=40, r=40, t=80, b=80),
    plot_bgcolor='white',
    paper_bgcolor='white'
)




top_customers = df.groupby('Customer_ID', as_index=False)['Total_Amount'].sum()
top_customers = top_customers.sort_values('Total_Amount', ascending=False).head(10)

fig11 = px.bar(
    top_customers,
    x='Customer_ID',
    y='Total_Amount',
    color='Customer_ID',
    title='👤 Top 10 Customers by Spending',
    text=top_customers['Total_Amount'],
    labels={'Customer_ID': 'Customer ID', 'Total_Amount': 'Total Sales ($)'}
)

fig11.update_traces(
    texttemplate='$%{text:.2f}',
    textposition='outside',
    marker=dict(line=dict(width=1, color='black'))
)

fig11.update_layout(
    xaxis_title='Customer ID',
    yaxis_title='Total Sales ($)',
    title_font=dict(size=22),
    title_x=0.5,
    uniformtext_minsize=12,
    uniformtext_mode='hide',
    yaxis=dict(tickprefix='$', showgrid=True, gridcolor='lightgray'),
    xaxis=dict(showgrid=False),
    plot_bgcolor='white',
    paper_bgcolor='white',
    font=dict(family='Arial', size=14),
    hoverlabel=dict(bgcolor='white', font_size=13),
    margin=dict(l=40, r=40, t=80, b=80),
    showlegend=False
)







fig12 = px.scatter(
    df,
    x='Quantity',
    y='Unit_Price',
    color='Product',
    size='Total_Amount',
    hover_data=['Product', 'Category', 'City', 'Payment_Method'],
    title='📈 Unit Price vs Quantity',
    labels={'Quantity': 'Quantity Purchased', 'Unit_Price': 'Unit Price ($)'},
    color_discrete_sequence=px.colors.qualitative.Set1
)

fig12.update_traces(
    marker=dict(line=dict(width=1, color='black')),
    selector=dict(mode='markers')
)

fig12.update_layout(
    title_font=dict(size=22),
    title_x=0.5,
    xaxis=dict(showgrid=True, gridcolor='lightgray'),
    yaxis=dict(showgrid=True, gridcolor='lightgray', tickprefix='$'),
    plot_bgcolor='white',
    paper_bgcolor='white',
    font=dict(family='Arial', size=14),
    hoverlabel=dict(bgcolor='white', font_size=13),
    margin=dict(l=40, r=40, t=80, b=80),
    legend_title_text='Product'
)






plt.figure(figsize=(8, 6))
corr_matrix = df[['Quantity', 'Unit_Price', 'Total_Amount']].corr()

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap='Blues',
    fmt='.2f',
    linewidths=0.5,
    linecolor='white',
    square=True,
    cbar_kws={'shrink': 0.75, 'label': 'Correlation'}
)

plt.title('📊 Correlation Heatmap', fontsize=16, weight='bold')
plt.xticks(rotation=0, fontsize=12)
plt.yticks(rotation=0, fontsize=12)
plt.tight_layout()
buf = io.BytesIO()
plt.savefig(buf, format="png", bbox_inches='tight')
buf.seek(0)
encoded_image = base64.b64encode(buf.read()).decode('utf-8')
plt.close()

heatmap_component = html.Div([
    html.H3("Correlation Heatmap", style={'textAlign': 'center'}),
    html.Img(src='data:image/png;base64,{}'.format(encoded_image),
             style={'display': 'block', 'margin': '0 auto', 'maxWidth': '100%'})
])




app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Sales Data Visualization Project – End-to-End Analysis", style={'textAlign': 'center'}),
    dcc.Graph(figure=fig1),
    dcc.Graph(figure=fig2),
    dcc.Graph(figure=fig3),
    dcc.Graph(figure=fig4),
    dcc.Graph(figure=fig5),
    dcc.Graph(figure=fig6),
    dcc.Graph(figure=fig7),
    dcc.Graph(figure=fig9),
    dcc.Graph(figure=fig10),
    dcc.Graph(figure=fig11),
    dcc.Graph(figure=fig12),
    heatmap_component
])

if __name__ == '__main__':
    app.run(debug=True)



