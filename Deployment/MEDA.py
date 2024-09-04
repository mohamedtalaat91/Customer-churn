import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def clean_data(data):

    data.columns=data.columns.str.lower()

    data['customerid'] = data['customerid'].astype('object')
    data['churn'] = data['churn'].astype('object')
    data['citytier'] = data['citytier'].astype('object')
    data['complain'] = data['complain'].astype('object')
    # Fill missing values with median for specific columns
    med_cols = ['tenure', 'warehousetohome', 'hourspendonapp', 'orderamounthikefromlastyear', 'daysincelastorder']
    for col in med_cols:
        data[col].fillna(data[col].median(), inplace=True)
    
    # Conditional filling of missing values
    if 'couponused' in data.columns and 'ordercount' in data.columns:
        coupon_factor = data.groupby('ordercount')['couponused'].median()
        data['couponused'] = data['couponused'].fillna(data['ordercount'].map(coupon_factor))
    
        ordercount_factor = data.groupby('couponused')['ordercount'].median()
        data['ordercount'] = data['ordercount'].fillna(data['couponused'].map(ordercount_factor))
    
    # Drop the customer ID column
    if 'customerid' in data.columns:
        data.drop('customerid', axis=1, inplace=True)
    
    return data

import numpy as np

def remove_outlier(col):
    """
    Removes outliers from a given numerical column
    by capping the outliers at the lower and upper bounds.
    """
    sorted(col)
    Q1, Q3 = np.percentile(col, [25, 75])
    IQR = Q3 - Q1
    lr = Q1 - (1.5 * IQR)
    ur = Q3 + (1.5 * IQR)
    lr = round(lr, 0)
    ur = round(ur, 0)
    return lr, ur

def treat_outliers(data):
    """
    Treats outliers in the DataFrame by capping values
    outside the IQR bounds at the respective bounds.
    """
    for column in data.columns:
        if data[column].dtype != 'object':  # Only treat numerical columns
            lr, ur = remove_outlier(data[column])
            data[column] = np.where(data[column] > ur, ur, data[column])
            data[column] = np.where(data[column] < lr, lr, data[column])
    
    return data


import plotly.graph_objs as go
from plotly.subplots import make_subplots

def plot_numeric_distributions(data):
    """
    Creates a subplot of box plots for each numeric column in the DataFrame.
    
    Parameters:
    data (pd.DataFrame): The input DataFrame with numeric columns to plot.
    
    Returns:
    fig (plotly.graph_objs.Figure): The subplot figure containing box plots.
    """
    numeric_data = data.select_dtypes(include=np.number)
    
    fig = make_subplots(cols=3, rows=4, subplot_titles=numeric_data.columns)

    for i, col in enumerate(numeric_data.columns):
    # Bar trace
        bar_trace = go.Bar(
            x=numeric_data[col].value_counts().sort_index().index,
            y=numeric_data[col].value_counts().sort_index().values,
            name=col
        )
        
        # Line trace
        line_trace = go.Scatter(
            x=numeric_data[col].value_counts().sort_index().index,
            y=numeric_data[col].value_counts().sort_index().values,
            mode='lines',
            name=f'{col} Line'
        )
        
        # Add traces to the figure
        fig.add_trace(bar_trace, row=i//3+1, col=i%3+1)
        fig.add_trace(line_trace, row=i//3+1, col=i%3+1)

    fig.update_layout(height=800, width=1400, template='plotly_dark',showlegend=False)

        
    return fig

def plot_categorical_distributions(data):
    cat_data = data.select_dtypes(include='object')
    # Assuming cat_data is your DataFrame with numeric columns
    fig = make_subplots(cols=4, rows=2, subplot_titles=cat_data.columns)


    for i, col in enumerate(cat_data.columns):
        # Bar trace
        bar_trace = go.Bar(
            x=cat_data[col].value_counts().sort_index().index,
            y=cat_data[col].value_counts().sort_index().values,
            name=col
        )
        
        
        # Add traces to the figure
        fig.add_trace(bar_trace, row=i//4+1, col=i%4+1)

    fig.update_layout(height=800, width=1400, template='plotly_dark',showlegend=False)
    return fig


def generate_churn_analysis_plot(data, column, average_churn=20.25):
    # Calculate churn-related metrics for the given column
    churn_sum = data.groupby(column).churn.sum().rename('Customers_churned')
    total_customers = data[column].value_counts().rename('Total_Customers')
    perc_of_total_cust = round(data.groupby(column).churn.sum() * 100 / data[column].value_counts(), 2).rename('perc_of_total_cust')

    # Combine the metrics into a single DataFrame
    churn_analysis_df = pd.concat([churn_sum, total_customers, perc_of_total_cust], axis=1).reset_index()
    churn_analysis_df = churn_analysis_df.rename(columns={'index': column})

    # Create the Plotly figure
    fig = go.Figure()

    # Adding the lines for the left y-axis
    fig.add_trace(go.Scatter(x=churn_analysis_df[column], y=churn_analysis_df['Customers_churned'],
                             mode='lines', name='Customers churned', line=dict(color='lightskyblue')))
    fig.add_trace(go.Scatter(x=churn_analysis_df[column], y=churn_analysis_df['Total_Customers'],
                             mode='lines', name='Total Customers', line=dict(color='dodgerblue')))

    # Adding the line for the right y-axis
    fig.add_trace(go.Scatter(x=churn_analysis_df[column], y=churn_analysis_df['perc_of_total_cust'],
                             mode='lines', name='Churn as Percent of total', line=dict(color='yellowgreen'), yaxis='y2'))

    # Adding the average customer churn line
    avg_churn_line = [average_churn] * len(churn_analysis_df[column])
    fig.add_trace(go.Scatter(x=churn_analysis_df[column], y=avg_churn_line,
                             mode='lines', name='Average customer Churn', line=dict(color='orangered', dash='dash'), yaxis='y2'))

    # Updating the layout
    fig.update_layout(
        title=f'Customers Churn analyzed by {column}',
        xaxis=dict(title=column, tickangle=45),
        yaxis=dict(title='No. of customers'),
        yaxis2=dict(title='Percentage of customers churned', overlaying='y', side='right'),
        legend=dict(x=1.1, y=1),
        template='plotly_white'
    )

    return fig

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
def generate_churn_analysis_subplots(data, avg_churn=20.25):
    # Dictionary to store the processed data for each categorical column
    d = {}
    cat_data_columns = data.select_dtypes(include='object').columns
    # Processing each categorical column and storing the relevant metrics
    for col in data.columns:
        churn_sum = data.groupby(col).churn.sum().rename('Customers_churned')
        total_customers = data[col].value_counts().rename('Total_Customers')
        perc_of_total_cust = round(data.groupby(col).churn.sum() * 100 / data[col].value_counts(), 2).rename('perc_of_total_cust')
        
        d[col] = pd.concat([churn_sum, total_customers, perc_of_total_cust], axis=1)
        d[col].reset_index(level=0, inplace=True)
        d[col] = d[col].rename(columns={'index': col})

    def analysis_chart_plotly(variable):
        if variable not in d:
            raise ValueError(f"Variable '{variable}' not found in the data dictionary.")
        
        data_var = d[variable]
        
        if data_var.empty:
            raise ValueError(f"No data available for variable '{variable}'.")

        traces = []

        # Adding the lines for the left y-axis
        traces.append(go.Scatter(x=data_var[variable], y=data_var['Customers_churned'],
                                 mode='lines', name='Customers churned', line=dict(color='lightskyblue')))
        traces.append(go.Scatter(x=data_var[variable], y=data_var['Total_Customers'],
                                 mode='lines', name='Total Customers', line=dict(color='dodgerblue')))

        # Adding the line for the right y-axis
        traces.append(go.Scatter(x=data_var[variable], y=data_var['perc_of_total_cust'],
                                 mode='lines', name='Churn as Percent of total', line=dict(color='yellowgreen'), yaxis='y2'))
        
        # Adding the average customer churn line
        y = [avg_churn] * len(data_var[variable])
        traces.append(go.Scatter(x=data_var[variable], y=y,
                                 mode='lines', name='Average customer Churn', line=dict(color='orangered', dash='dash'), yaxis='y2'))

        return traces

    # Create subplots
    num_plots = len(cat_data_columns)
    rows = (num_plots + 1) // 2
    fig = make_subplots(rows=rows, cols=2, subplot_titles=cat_data_columns)

    # Populate the subplots with traces
    for i, col in enumerate(cat_data_columns):
        traces = analysis_chart_plotly(col)
        for trace in traces:
            fig.add_trace(trace, row=i//2+1, col=i%2+1)

    # Update the layout
    fig.update_layout(height=900, width=1400, template='plotly_dark', showlegend=False)
    
    return fig




    
