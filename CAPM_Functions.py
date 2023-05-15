import plotly.express as px

# function to plot an interactive chart
def interactive_plot(df):
    fig = px.line()
    for column in df.columns[1:]:
        fig.add_scatter(x=df['Date'], y=df[column], name=column)
    fig.update_layout(
        width=450,
        margin=dict(l=20, r=20, t=50, b=20),
        legend=dict(orientation='h', yanchor='bottom'),
        yaxis=dict(title='Normalized Price'),
        xaxis=dict(title='Date'),
    )
    return fig

# function to normalize stock prices based on the initial prices
def normalize(df):
    for column in df.columns[1:]:
        df[column] = df[column] / df[column][0]
    return df
