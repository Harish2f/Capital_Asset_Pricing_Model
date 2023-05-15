import plotly.express as px 

# function to plot interactive chart
def interactive_plot(df):
    fig = px.line()
    for i in df.columns[1:]:
        fig.add_scatter(x = df['Date'], y =df[i], name = i)
    fig.update_layout(width = 450, margin = dict(l=20, r=20, t=50, b=20),
                      legend= dict(orientation = 'h', yanchor = 'bottom'),
                      y = 1.02, xanchor = 'right', x = 1,)
    return fig

# function to normalize stock prices based on the initial frices
def normalize(df):
    for i in df.columns[1:]:
        df[i] = df[i]/df[i][0]
    return df