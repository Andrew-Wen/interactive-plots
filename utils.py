def plotly_scatter_plot_matrix(df, columns):
    
    import plotly.express as px
    
    # convert the label from integer to string
    df['label'] = df['label'].astype(str)
    
    # set some common configs
    opacity = 0.6
    bgcolor = 'rgb(217,217,217)'
    hover = ['class','start','end']
    colors = ['#4C78A8','#DC3912']
    
    fig = px.scatter_matrix(df, 
                            dimensions = columns,
                            color = 'label', 
                            hover_data = hover, 
                            opacity = opacity,
                            color_discrete_sequence = colors,
                           )
    fig.update_layout(
                        {
                        'plot_bgcolor': bgcolor
                        },
                        width = 1200,
                        height = 1200,
                      )
    fig.update_traces(marker = dict(size = 2))
    fig.show()
    
    
def single_plotly_plot(df, x, y, opacity=0.6, seperate=False):
    '''
    Generates an interacitve plot using plotly.
    
    Arguments:
        df (object): A pandas.DataFrame that stores the data from a specific partition.
        x (str): The attribute to be on x-axis.
        y (str): The attribute to be on y-axis.
        opacity (float): The alpha blending value, between 0 (transparent) and 1 (opaque).
        separate (bool): Whether or not to plot flaring and non-flaring data separatly.
    '''
    
    import plotly.express as px
    
    # convert the label from integer to string
    df['label'] = df['label'].astype(str)
    
    # set some common configs
    bgcolor = 'rgb(217,217,217)'
    hover = ['class','start','end']
    colors = ['#4C78A8','#DC3912']
    
    if seperate:
        lim = [-0.05, 1.05]
        
        fig1 = px.scatter(df[df['label'] == '0'], 
                            x = x, 
                            y = y, 
                            color = 'label', 
                            hover_data = hover, 
                            opacity = opacity,
                            color_discrete_sequence = colors[0]
                           )
        fig1.update_layout(
                          {
                           'plot_bgcolor': bgcolor
                          },
                            xaxis = dict(range = lim),
                            yaxis = dict(range = lim)
                          )
        fig2 = px.scatter(df[df['label'] == '1'], 
                            x = x, 
                            y = y, 
                            color = 'label', 
                            hover_data = hover, 
                            opacity = opacity,
                            color_discrete_sequence = color[1]
                         )
        fig2.update_layout(
                            {
                           'plot_bgcolor': bgcolor
                            },
                            xaxis = dict(range = lim),
                            yaxis = dict(range = lim)
                          )
        fig1.show()
        fig2.show()
    else:
        fig = px.scatter(df, 
                         x = x, 
                         y = y, 
                         color = 'label', 
                         hover_data = hover, 
                         opacity = opacity,
                         color_discrete_sequence = colors
                        )
        fig.update_layout(
                          {
                           'plot_bgcolor': bgcolor
                          },
                            width = 1000,
                            height = 600,                    
                         )
        fig.show()
