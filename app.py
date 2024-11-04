import pandas as pd
import os
import dash
from dash import dcc, Dash, html, dash_table, callback, Output, Input
from dash.dependencies import Input, Output
import plotly.express as px
from dash import dcc

df = pd.read_csv("C:\\3rd\\WEB_MAPPING\\week_10\\service_311.csv", encoding='ISO-8859-1')

app = Dash()
app.layout = html.Div(
    [html.Div(children='Lab08', style={'color':'red'}),
    dash_table.DataTable(id='data-table', data = df.to_dict('records'), page_size=10),
    dcc.Graph(figure=px.histogram(df, x = 'weekday', barmode='relative', histfunc='count', color='reason'), id='graph_his'),
    dcc.RadioItems(options=['daytime', 'nighttime', 'All'], value='All', id='radio_button')]
)

@callback(
    [Output(component_id='graph_his', component_property='figure'),
    Output(component_id='data-table', component_property='data')],
    Input(component_id='radio_button', component_property='value')
)

def update_graph(time):
    if time == 'All':
        filter_df = df
    else:
        filter_df = df[df['time_of_day']==time]
    fig = px.histogram(filter_df, x = 'weekday', barmode='relative', histfunc='count', color='reason')
    table_data = filter_df.to_dict('records')

    return fig, table_data

if __name__ == '__main__':
    app.run(debug=True)
