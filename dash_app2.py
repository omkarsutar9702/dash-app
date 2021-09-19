from dash_html_components.Title import Title
import pandas as pd
import plotly.graph_objects as go
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input , Output

#create the dash application
app = dash.Dash(__name__)

airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})

# Get the layout of the application and adjust it.
# Create an outer division using html.Div and add title to the dashboard using html.H1 component
# Add a html.Div and core input text component
# Finally, add graph component.

app.layout = html.Div(children=[ html.H1('Airline Performance Dashboard', 
                                style={'textAlign': 'center', 'color': '#503D36',
                                'font-size': 40}),
                                html.Div(["Input Year: ", dcc.Input(id='input-year', value='2010', 
                                type='number', style={'height':'50px', 'font-size': 35}),], 
                                style={'font-size': 40}),
                                html.Br(),
                                html.Br(),
                                html.Div(dcc.Graph(id='line-plot')),
                                ])

# app.layout = html.Div(children=[ html.H1('airline Performance Dashboard',
#                                          style={'textAlign': 'center', 'color': 'blue' , 'font-size':40}),
#                                 html.Div(["input Year: ", dcc.Input(id='input-year', value='2010', type='number', style={'height':'50px', 'font-size':35}),], 
#                                          style={'font-size': 40}),
#                                 html.br(),
#                                 html.br(),
#                                 html.Div(dcc.Graph(id='line-plot')),
#                                 ])

# add callback decorator
# @app.callback(Output(component_id='line-plot',component_property = 'figure'),
#               Input(component_id='input-year',component_property = 'value'))

@app.callback( Output(component_id='line-plot', component_property='figure'),
               Input(component_id='input-year', component_property='value'))

def get_graph(entered_year):
    df = airline_data[airline_data['Year']==int(entered_year)]
    
    line_data = df.groupby('Month')['ArrDelay'].mean().reset_index()
    
    fig= go.Figure(data=go.Scatter(x=line_data['Month'] , y=line_data['ArrDelay'],mode='lines' , marker=dict(color='red')))
    fig.update_layout(title = 'Month vs average flights delay time' , xaxis_title='Month' , yaxis_title='Arrdelay')
    return fig

if __name__ == '__main__':
    app.run_server()
