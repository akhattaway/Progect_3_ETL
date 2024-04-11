from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# Results from your data processing
data = {
    "Year": ["2023", "2024"],
    "Total Mockups Created in February": [8010, 7925],
    "Mockups Converted in Feb or Mar": [496, 636],
    "Total Quantity of Converted Mockups Feb and March": [142573, 139807],
    "Mean Quantity of Converted Mockups Feb and March": [224, 173],
    "Standard Deviation of Converted Mockups Feb and March": [394, 251]
}
results_df = pd.DataFrame(data)

app = Dash(__name__)

# Creating bar charts for each category with improved labels and titles
fig_mockups = px.bar(results_df, x='Year', y='Total Mockups Created in February',
                     title='Total Mockups Created in February by Year',
                     labels={'Total Mockups Created in February': 'Total Mockups'})

fig_converted = px.bar(results_df, x='Year', y='Mockups Converted in Feb or Mar',
                       title='Mockups Converted in February or March by Year',
                       labels={'Mockups Converted in Feb or Mar': 'Converted Mockups'})

fig_total_quantity = px.bar(results_df, x='Year', y='Total Quantity of Converted Mockups Feb and March',
                            title='Total Quantity of Converted Mockups Feb and March by Year',
                            labels={'Total Quantity of Converted Mockups Feb and March': 'Total Quantity'})

fig_mean_quantity = px.bar(results_df, x='Year', y='Mean Quantity of Converted Mockups Feb and March',
                           title='Mean Quantity per Conversion Feb and March by Year',
                           labels={'Mean Quantity of Converted Mockups Feb and March': 'Mean Quantity'})

fig_std_dev = px.bar(results_df, x='Year', y='Standard Deviation of Converted Mockups Feb and March',
                     title='Standard Deviation of Quantities Feb and March by Year',
                     labels={'Standard Deviation of Converted Mockups Feb and March': 'Standard Deviation'})

app.layout = html.Div([
    html.H1("Mockup Analysis Results Dashboard"),
    html.Div([
        dcc.Graph(id='graph1', figure=fig_mockups),
        dcc.Graph(id='graph2', figure=fig_converted),
        dcc.Graph(id='graph3', figure=fig_total_quantity),
        dcc.Graph(id='graph4', figure=fig_mean_quantity),
        dcc.Graph(id='graph5', figure=fig_std_dev),
    ], style={'columnCount': 2})
])

if __name__ == '__main__':
    app.run_server(debug=True)
