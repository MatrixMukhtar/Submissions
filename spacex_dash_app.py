# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

app.config.suppress_callback_exceptions = True

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                    
                                        dcc.Dropdown(id='site-dropdown',
                                                options=[
                                                    {'label': 'All Sites', 'value': 'ALL'},
                                                    {'label': 'CCA', 'value': 'CCAFS SLC 40'},
                                                    {'label': 'KSC', 'value': 'KSC LC 39A'},
                                                    {'label': 'VAFB', 'value': 'VAFB SLC 4E'},
                                                    {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                                                ],
                                                value='ALL',
                                                placeholder="place holder here",
                                                searchable=True
                                                ),
                              
                                html.Div([ html.Div([ ], id='success-pie-chart') ], style={'display': 'flex'})

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                
                              
                                

                               # html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                #dcc.RangeSlider(id='payload-slider',...)

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                
                                ])

                                       
@app.callback(Output(component_id='success-pie-chart', component_property='children'),
                    Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    filtered_df = spacex_df[spacex_df["Launch Site"]==entered_site]
    segmented=spacex_df.groupby(["Launch Site"]).mean()["class"].reset_index()
    filtered_d=filtered_df.groupby(["Launch Site"]).mean()["class"].reset_index()
    fig1 = px.pie(segmented, values='class', 
        names='Launch Site', 
        title='Total Success Launches By Site')
    fig = px.pie(filtered_d, values='class', 
        names='Launch Site', 
        title='Total Success Launches For Site '+entered_site)
    if entered_site == 'ALL':
        return dcc.Graph(figure=fig)
    else:
        return dcc.Graph(figure=fig)

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output


# Run the app
if __name__ == '__main__':
    app.run_server()
