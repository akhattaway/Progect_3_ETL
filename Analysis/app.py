from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# Results from your data processing
data = {
    "Year": ["2023", "2024"],
    "Total Mockups Created in February": [8010, 7925],
    "Mockups Converted in Feb or Mar": [496, 636],
    "Total Quantity of Converted Mockups": [142573, 139807],
    "Mean Quantity per Conversion": [224, 173],
    "Standard Deviation of Quantities": [394, 251]
}
results_df = pd.DataFrame(data)

app = Dash(__name__)

# Customizing the bar charts to display data labels and using a larger font size
fig_mockups = px.bar(results_df, x='Year', y='Total Mockups Created in February',
                     title='Total Mockups Created in February by Year',
                     text='Total Mockups Created in February',
                     labels={'Total Mockups Created in February': 'Total Mockups'})
fig_mockups.update_traces(texttemplate='%{text}', textposition='inside')
fig_mockups.update_layout(title_x=0.5, uniformtext_minsize=18, uniformtext_mode='hide')

fig_converted = px.bar(results_df, x='Year', y='Mockups Converted in Feb or Mar',
                       title='Mockups Converted in February or March by Year',
                       text='Mockups Converted in Feb or Mar',
                       labels={'Mockups Converted in Feb or Mar': 'Converted Mockups'})
fig_converted.update_traces(texttemplate='%{text}', textposition='inside')
fig_converted.update_layout(title_x=0.5, uniformtext_minsize=18, uniformtext_mode='hide')

fig_total_quantity = px.bar(results_df, x='Year', y='Total Quantity of Converted Mockups',
                            title='Total Quantity of Converted Mockups Feb and Mar by Year',
                            text='Total Quantity of Converted Mockups',
                            labels={'Total Quantity of Converted Mockups': 'Total Quantity'})
fig_total_quantity.update_traces(texttemplate='%{text}', textposition='inside')
fig_total_quantity.update_layout(title_x=0.5, uniformtext_minsize=18, uniformtext_mode='hide')

fig_mean_quantity = px.bar(results_df, x='Year', y='Mean Quantity per Conversion',
                           title='Mean Quantity per Conversion Feb and Mar by Year',
                           text='Mean Quantity per Conversion',
                           labels={'Mean Quantity per Conversion': 'Mean Quantity'})
fig_mean_quantity.update_traces(texttemplate='%{text}', textposition='inside')
fig_mean_quantity.update_layout(title_x=0.7, uniformtext_minsize=18, uniformtext_mode='hide')

fig_std_dev = px.bar(results_df, x='Year', y='Standard Deviation of Quantities',
                     title='Standard Deviation of Quantities Feb and Mar by Year',
                     text='Standard Deviation of Quantities',
                     labels={'Standard Deviation of Quantities': 'Standard Deviation'})
fig_std_dev.update_traces(texttemplate='%{text}', textposition='inside')
fig_std_dev.update_layout(title_x=0.5, uniformtext_minsize=18, uniformtext_mode='hide')

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
