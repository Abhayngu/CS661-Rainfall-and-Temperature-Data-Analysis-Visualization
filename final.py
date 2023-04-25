import pandas as pd 
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import json
import plotly.express as px
from urllib.request import urlopen
import geopandas as gpd 
import plotly.express as px
import dash_daq as daq
import numpy as np
import plotly.graph_objects as go



data = pd.read_csv("Final_Edited_data.csv")
india_states = json.load(open("dists11.geojson", "r"))
india = json.load(open("states.geojson","r"))
temperatureData = pd.read_csv("temperatures.csv")


app = Dash(__name__)


indian_states_lat_log = {
    "Andhra Pradesh": (15.9129, 79.7399),
    "Arunachal Pradesh": (28.2180, 94.7278),
    "Assam": (26.2006, 92.9376),
    "Bihar": (25.0961, 85.3131),
    "Chattisgarh": (21.2787, 81.8661),
    "Goa": (15.2993, 74.1240),
    "Gujarat": (22.2587, 71.1924),
    "Haryana": (29.0588, 76.0856),
    "Himachal Pradesh": (31.1048, 77.1734),
    "Delhi" : (28.7041, 77.1025),
    "Jammu and Kashmir" : (33.2778, 75.3412),
    "Jharkhand": (23.6102, 85.2799),
    "Karnataka": (15.3173, 75.7139),
    "Kerala": (10.8505, 76.2711),
    "Madhya Pradesh": (22.9734, 78.6569),
    "Maharashtra": (19.7515, 75.7139),
    "Manipur": (24.6637, 93.9063),
    "Meghalaya": (25.4670, 91.3662),
    "Mizoram": (23.1645, 92.9376),
    "Nagaland": (26.1584, 94.5624),
    "Orissa": (20.9517, 85.0985),
    "Punjab": (31.1471, 75.3412),
    "Rajasthan": (27.0238, 74.2179),
    "Sikkim": (27.5330, 88.5122),
    "Tamil Nadu": (11.1271, 78.6569),
    "Telangana": (18.1124, 79.0193),
    "Tripura": (23.9408, 91.9882),
    "Uttar Pradesh": (26.8467, 80.9462),
    "Uttarakhand": (30.0668, 79.0193),
    "West Bengal": (22.9868, 87.8550),
    "Puducherry": (11.9416, 79.8083),
    "Lakshadweep": (10.3280,72.7847)
}

months={
    1: 'Jan',
    2: 'Feb',
    3: 'Mar',
    4: 'Apr',
    5: 'May',
    6: 'Jun',
    7: 'Jul',
    8: 'Aug',
    9: 'Sep',
    10: 'Oct',
    11: 'Nov',
    12: 'Dec'
}

state_names = ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar',
       'Chandigarh', 'Chattisgarh', 'Dadra & Nagar Haveli',
       'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh',
       'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala',
       'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
       'Meghalaya', 'Mizoram', 'Nagaland', 'Orissa', 'Puducherry',
       'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana',
       'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal','Daman & Diu']

l1 = [['Sikkim',28],
        ['Meghalaya',21],
        ['Mizoram',22],
        ['Manipur',20],                         
        ['Assam',2],
        ['Tripura',31],
        ['Arunachal Pradesh',1],
        ['Nagaland',23],
        [ 'Uttarakhand',33],
        ['Himachal Pradesh',12],
        ['Jammu and Kashmir',13],
        ['Bihar',3],
        ['West Bengal',34],
        ['Jharkhand',14],
         ['Delhi' ,8],
        ['Chandigarh',4],
        ['Uttar Pradesh',32],
        ['Punjab' ,26],
        ['Haryana',11],
         ['Maharashtra',19],
        ['Goa',9],
        ['Karnataka',15],
        ['Kerala',16],
        ['Gujarat',10],
        ['Dadra & Nagar Haveli',6],
        ['Orissa',24],
        ['Andhra Pradesh',0],
        ['Tamil Nadu',29],
        ['Puducherry',25],
        ['Madhya Pradesh',18],
        ['Chattisgarh',5],
         ['Rajasthan',27],
         ['Telangana',30],
          ['Lakshadweep',17]
      
                
]

labels_ = [
    "Eastern Himalayan Region",
        'Sikkim',
        'Meghalaya',
        'Mizoram',
        'Manipur',                          
        'Assam',
        'Tripura',
        'Arunachal Pradesh',
        'Nagaland',
    
    'western Himalayan Region',
        'Uttarakhand',
        'Himachal Pradesh',
        'Jammu and Kashmir',

    'Eastern Region',
        'Bihar',
        'West Bengal',
        'Jharkhand',

   'Western Region',
        'Delhi' ,
        'Chandigarh',
        'Uttar Pradesh',
        'Punjab' ,
        'Haryana',


    'Western Coastal Region',
        'Maharashtra',
        'Goa',
        'Karnataka',
        'kerala',
        'Gujarat',
        'Dadra & Nagar Haveli',

    'Eastern Coastal Region',
        'Orissa',
        'Andhra Pradesh',
        'Tamil Nadu',
        'Puducherry',

   'Central India',
        'Madhya Pradesh',
        'Chattisgarh',
    
    'Rajashthan',

    'Telanagana',
    
    'Lakshadweep'

]

parents_  = [
    
    "",
        'Eastern Himalayan Region',
        'Eastern Himalayan Region',
        'Eastern Himalayan Region',
        'Eastern Himalayan Region',                          
        'Eastern Himalayan Region',
        'Eastern Himalayan Region',
        'Eastern Himalayan Region',
        'Eastern Himalayan Region',
    
    '',
        'western Himalayan Region',
        'western Himalayan Region',
        'western Himalayan Region',

    '',
        'Eastern Region',
        'Eastern Region',
        'Eastern Region',

   '',
        'Western Region' ,
        'Western Region',
        'Western Region',
        'Western Region' ,
        'Western Region',


    '',
        'Western Coastal Region',
        'Western Coastal Region',
        'Western Coastal Region',
        'Western Coastal Region',
        'Western Coastal Region',
        'Western Coastal Region',

    '',
        'Eastern Coastal Region',
        'Eastern Coastal Region',
        'Eastern Coastal Region',
        'Eastern Coastal Region',

   '',
        'Central India',
        'Central India',
    
    '',
        

    '',
        
    ''

    
]

temp1 = gpd.GeoDataFrame.from_features(india["features"]).rename(columns={'ST_NM':'State'})
temp2 = gpd.GeoDataFrame.from_features(india_states["features"]).rename(columns={'DISTRICT':'District'})


states = data["State"].unique()
monthList = list(months.values())
normalize = lambda x: (x - x.min()) / (x.max() - x.min())


season_data = data.copy()
# season_data.set_index("Year", inplace=True)
par_data = season_data.iloc[:, 2:13]
season_data['ANNUAL'] = par_data.sum(axis=1)
season_data['SUMMER'] = season_data[['Feb','Mar','Apr','May']].sum(axis=1)
season_data['MONSOON'] = season_data[['Jun','Jul','Aug','Sep']].sum(axis=1)
season_data['WINTER'] = season_data[['Oct','Nov','Dec','Jan']].sum(axis=1)
data_mean = season_data["ANNUAL"].groupby(season_data["State"])

summer_rainfall = season_data.loc[:, ["State", "SUMMER"]].groupby("State").mean().reset_index()
monsoon_rainfall = season_data.loc[:, ["State", "MONSOON"]].groupby("State").mean().reset_index()
winter_rainfall = season_data.loc[:, ["State", "WINTER"]].groupby("State").mean().reset_index()

summer_rainfall_melt = summer_rainfall.melt(id_vars="State", value_vars="SUMMER", var_name="Season", value_name="Rainfall")
monsoon_rainfall_melt = monsoon_rainfall.melt(id_vars="State", value_vars="MONSOON", var_name="Season", value_name="Rainfall")
winter_rainfall_melt = winter_rainfall.melt(id_vars="State", value_vars="WINTER", var_name="Season", value_name="Rainfall")

rainfallSeason = pd.concat([summer_rainfall_melt, monsoon_rainfall_melt, winter_rainfall_melt])

grpWiseRainFall = []
grpWiseTemperature = []

def rainfallTrend():
    yearWiseRainFall = {}
    groupLen = 10
    for year in range(1901, 2003):
        temp = data[data['Year']==year]
        curYearRainfall = 0
        l = 0
        for m in months:
            t2 = temp[months[m]]
            curYearRainfall += t2.sum()
            l += len(t2)
        yearWiseRainFall[year] = curYearRainfall/l
    yr = 1901
    while(yr + 10 < 2003):
        rainfallInGrp = 0
        for i in range(10):
            rainfallInGrp += yearWiseRainFall[yr]
            yr+=1
        grpWiseRainFall.append(rainfallInGrp/10)
    return pd.DataFrame(grpWiseRainFall, columns=['rainfall'])

def yearWiseCumulative():
    yearWiseRainFall = {}
    for year in range(1901, 2003):
        temp = data[data['Year']==year]
        curYearRainfall = 0
        l = 0
        for m in months:
            t2 = temp[months[m]]
            curYearRainfall += t2.sum()
            l += len(t2)
        yearWiseRainFall[year] = curYearRainfall/l
    cumulativeRainfall = [0]
    i = 1
    for yr in yearWiseRainFall:
        cumulativeRainfall.append(yearWiseRainFall[yr] + cumulativeRainfall[i-1])
        i+=1
    # print(cumulativeRainfall)
    return pd.DataFrame(list(yearWiseRainFall.values()), columns=['rainfall'])
    

def temperatureTrend():
    yearWiseTemperature = {}
    groupLen = 10
    for year in range(1901, 2018):
        temp = temperatureData[temperatureData['Year']==year]
        # print(temp['ANNUAL'])
        yearWiseTemperature[year] = (temp['ANNUAL'])
    yr = 1901
    while(yr + 10 < 2018):
        tempInGrp = 0
        for i in range(10):
            tempInGrp += int(yearWiseTemperature[yr])
            yr+=1
        grpWiseTemperature.append(tempInGrp/10)
    # print(grpWiseTemperature)
    return pd.DataFrame(grpWiseTemperature, columns=['temperature'])

def rainfallTempTrend():
    yearWiseRainFall = {}
    groupLen = 10
    for year in range(1901, 2003):
        temp = data[data['Year']==year]
        curYearRainfall = 0
        l = 0
        for m in months:
            t2 = temp[months[m]]
            curYearRainfall += t2.sum()
            l += len(t2)
        yearWiseRainFall[year] = curYearRainfall/l
    yearWiseRainFall = [float(i) for i in yearWiseRainFall.values()]
    
    yearWiseTemperature = {}
    for year in range(1901, 2018):
        temp = temperatureData[temperatureData['Year']==year]
        # print(temp['ANNUAL'])
        yearWiseTemperature[year] = (temp['ANNUAL'])
    yearWiseTemperature = [float(i) for i in yearWiseTemperature.values()]
    yearWiseTemperature = yearWiseTemperature[0:len(yearWiseRainFall)]
    dfR = pd.DataFrame(yearWiseRainFall, columns=['rainfall'])
    dfT = pd.DataFrame(yearWiseTemperature, columns=['temperature'])
    dfR = dfR.apply(normalize)
    dfT = dfT.apply(normalize)
    # print(dfR.shape, dfT.shape)
    df = pd.DataFrame()
    df['rainfall'] = dfR
    df['temperature'] = dfT
    # print(df)
    return df

def rainfallMonthWiseTrend():
    monthwise_rainfall = {}
    for m in months:
        month_data = data[months[m]]
        monthly_avg_data = month_data.sum()/len(month_data)
        monthwise_rainfall[months[m]] = monthly_avg_data
    df = pd.DataFrame()
    df['Rainfall'] = list(monthwise_rainfall.values())
    return df
    

season_fig = px.bar(rainfallSeason, x="State", y="Rainfall", color="Season",
             title="Seasonal Rainfall in Indian States",
             labels={"STATE": "State", "Rainfall": "Rainfall (mm)"})

# fig.show()


monthWiseRainfall = px.pie(rainfallMonthWiseTrend(), values='Rainfall', names = monthList, )
monthWiseRainfall.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',  
    paper_bgcolor='#eff8fc',  
    font_color='rgb(0,0,0)',  
)
monthWiseRainfall.update_layout(clickmode='event+select')
monthWiseRainfall.update_layout(hovermode='x')
# monthWiseRainfall.update_xaxes(title='Months')
# monthWiseRainfall.update_yaxes(title='Rainfall')    

# rainfallTempTrend()
grpFigureRainfall = px.line(rainfallTrend(),  x=[i for i in range(1, 11)], y='rainfall')
grpFigureRainfall.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',  
    paper_bgcolor='#cae7b9',  
    font_color='rgb(0,0,0)',  
)
grpFigureRainfall.update_xaxes(title='10 year group')
grpFigureRainfall.update_yaxes(title='Rainfall')

grpFigureTemp = px.line(temperatureTrend(),  x=[i for i in range(1, 12)], y=['temperature'])
grpFigureTemp.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',  
    paper_bgcolor='#cae7b9',  
    font_color='rgb(0,0,0)',  
)
grpFigureTemp.update_xaxes(title='10 year group')
grpFigureTemp.update_yaxes(title='Temperature')

rainTempTrend =  px.line(rainfallTempTrend(), x=[i for i in range(1901, 2003)], y=['rainfall', 'temperature'], color_discrete_sequence=['red','blue'])
rainTempTrend.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',  
    paper_bgcolor='#cae7b9',  
    font_color='rgb(0,0,0)',  
)
rainTempTrend.update_xaxes(title='Year')
rainTempTrend.update_yaxes(title='Normalized value')

yearWiseCumulativeBar =  px.line(yearWiseCumulative(), x=[i for i in range(1901, 2003)], y='rainfall', color_discrete_sequence=['red','blue'])
yearWiseCumulativeBar.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',  
    paper_bgcolor='#cae7b9',  
    font_color='rgb(0,0,0)',  
)
yearWiseCumulativeBar.update_xaxes(title='Year')
yearWiseCumulativeBar.update_yaxes(title='Rainfall')







# def layout1():
app.layout = html.Div(children=[
    html.Div([
        html.H1('Rain Fall Data Visualization', style={'color': 'Grey' , 'text-align': 'center' , 'margin-bottom': '10px'}),
        ], 
        style={'border': '1px solid black', 'padding': '10px'}
    ),
    html.Div([
        dcc.Slider(
            id='slider_year',
            min=1901,
            max=2003,
            step=1,
            marks={
                1901: '1901',
                1920: '1920',
                1940: '1940',
                1960: '1960',
                1980: '1980',
                2003: '2003'
            },
            value = 2000
        ),
        dcc.Slider(
            id='month-slider',
            min=1,
            max=12,
            step=1,
            marks={
                1: 'Jan',
                2: 'Feb',
                3: 'Mar',
                4: 'Apr',
                5: 'May',
                6: 'Jun',
                7: 'Jul',
                8: 'Aug',
                9: 'Sep',
                10: 'Oct',
                11: 'Nov',
                12: 'Dec'
            },
            value=7
        )
    ]),
    
    html.Div([
        dcc.Graph(id='india-graph', figure={} , style={'width': '70%', 'height': '500px', 'margin': 'auto' , 'margin-top': '10px'})
    ], style={'display': 'inline-block', 'width': '50%'}),
    html.Div([
        dcc.Graph(id='state-graph',figure={} , style={'width': '100%', 'height': '500px', 'margin': 'auto' , 'margin-top': '10px'})
    ], style={'display': 'inline-block', 'width': '50%'}),
    html.H1('Comparison across various states', style={'color': 'Grey' , 'text-align': 'center' , 'margin-bottom': '10px'}),
    html.Div([

        html.Div([
            daq.Slider(
                id='year_slider2',
                min=1900,
                max=2003,
                step=1,
                size = 1000,
                marks={
                    1900: '1900',
                    1920: '1920',
                    1940: '1940',
                    1960: '1960',
                    1980: '1980',
                    2002: '2002'
                },
                value = 2000
            )
        ],style={'display': 'flex', 'justifyContent' : 'center', 'width': '100%', 'marginBottom' : '50px'})
    ]),
    html.Div([
        dcc.Dropdown(
            id = 'state_dropdown',
            options= [{'label': state, 'value': state} for state in state_names ],
            value= ['Gujrat', 'Rajashthan'],
            multi= True
            
        )
    ]),
    html.Div([
        dcc.Graph(id='lineChart2', figure={} , style={'width': '100%', 'height': '500px', 'margin': 'auto' , 'margin-top': '10px'})
    ], style={'display': 'inline-block', 'width': '50%'}),
    html.Div([
        dcc.Graph(id='sunGraph',figure={} , style={'width': '100%', 'height': '500px', 'margin': 'auto' , 'margin-top': '10px'})
    ], style={'display': 'inline-block', 'width': '50%'}),

    html.Div([
        html.H1('Change in Average rainfall and average temperature', style={'color': 'Grey' , 'textAlign': 'center'}),
        
        dcc.Slider(
            id='slider',
            min=1901,
            max=2002,
            step=1,
            marks={
                1901: '1901',
                1920: '1920',
                1940: '1940',
                1960: '1960',
                1980: '1980',
                2002: '2002'
            },
            tooltip={"placement": "bottom", "always_visible": True},
            value = 2000,
            className='year-slider'
        ),
        
        html.Div(children = [ dcc.Graph(id='rainfall-correlation', style={'backgroundColor' : 'red'}),
        dcc.Graph(id='temp-correlation', style={'backgroundColor' : 'red'}),], style={'display' : 'flex', 'justifyContent' : 'space-evenly'}),
        
         html.H1('Average Rainfall trend in 10 years interval', style={'color': 'Grey' , 'textAlign': 'center'}),
         html.Div([ dcc.Graph( figure=grpFigureRainfall, style={'width' : '90%'}),], style={'display' : 'flex', 'justifyContent' : 'center'}),
       
        
         html.H1('Average Temperature trend in 10 years interval', style={'color': 'Grey' , 'textAlign': 'center'}),
         html.Div([dcc.Graph( figure=grpFigureTemp,style={'width' : '90%'}),], style={'display' : 'flex', 'justifyContent' : 'center'}),
        
        
         html.H1('Rainfall and temperature correlation', style={'color': 'Grey' , 'textAlign': 'center'}),
          html.Div([  dcc.Graph(figure=rainTempTrend,style={'width' : '90%'}),], style={'display' : 'flex', 'justifyContent' : 'center', 'marginBottom' : '80px'}),
          
        html.H1('Monthwise Rainfall trend', style={'color': 'Grey' , 'textAlign': 'center'}),
        html.Div(children = [dcc.Graph(figure=monthWiseRainfall, style={'width' : '80%'}),], style={'display' : 'flex', 'justifyContent' : 'center', 'marginBottom' : '40px', 'marginTop' : '40px'}),

        html.H1('Yearwise rainfall', style={'color': 'Grey' , 'textAlign': 'center'}),
        html.Div(children = [dcc.Graph(figure=yearWiseCumulativeBar, style={'width' : '80%'}),], style={'display' : 'flex', 'justifyContent' : 'center', 'marginBottom' : '40px', 'marginTop' : '40px'}),
      
        html.H1('Season wise rainfall', style={'color': 'Grey' , 'textAlign': 'center'}),
        html.Div(children = [dcc.Graph(figure=season_fig, style={'width' : '80%'}),], style={'display' : 'flex', 'justifyContent' : 'center', 'marginBottom' : '40px', 'marginTop' : '40px'}),
        
        dcc.Dropdown(
        id="state-dropdown",
        options=[{"label": state, "value": state} for state in states],
        value=states[0],
        style={'width' : '80%', 'paddingLeft' : '20%'}
        ),
        
        html.Div(children = [dcc.Graph(id="rainfall-bar-chart", style={'width' : '80%'}),], style={'display' : 'flex', 'justifyContent' : 'center', 'marginBottom' : '40px', 'marginTop' : '40px'}),
        
          
        html.Div([
        dcc.Dropdown(
            id="state-dropdown-1",
            options=[{"label": state, "value": state} for state in states],
            value=states[0],
            style={'width' : '90%'}
        ),
        dcc.Dropdown(
            id="state-dropdown-2",
            options=[{"label": state, "value": state} for state in states],
            value=states[1],
            style={'width' : '90%'}
        ),
        ], style={"display": "flex", 'paddingLeft' : '30px', 'paddingRight' : '20px'}),
           
    html.Div(children = [dcc.Graph(id="rainfall-scatter-plot", style={'width' : '80%'}),], style={'display' : 'flex', 'justifyContent' : 'center', 'marginBottom' : '40px', 'marginTop' : '40px'}),
        
    ])
])


   
    
    

# app.layout = html.Div([
#     dcc.Location(id='url', refresh=False),
#     html.Div(id='page-content')
# ])


#################################
# Sungraph and lineCharts Callbacks
#################################

@app.callback(Output('sunGraph', component_property='figure'),
              [Input('year_slider2','value'),Input('state_dropdown','value')]
)
def update_fig21(slider_value,dropdown_value):
    data_ = data[data['Year'] == slider_value]
    data_ = data_.groupby('State').mean(numeric_only=True)
    data_ = data_.drop('Year',axis=1)
    data_ = data_.assign(Annual=data_['Jan'] + data_['Feb'] + data_['Mar'] + data_['Apr'] + data_['May'] + data_['Jun']
                     + data_['Jul'] + data_['Aug'] + data_['Sep'] + data_['Oct'] +  + data_['Nov'] +  + data_['Dec'])
    data_ = data_.reset_index()
    l2 = []
    for i in l1:
        t = data_[data_['State']==i[0]]['Annual'][i[1]]
        l2.append(t)
    values_ = [
    
             l2[0]+l2[1]+l2[2]+l2[3]+l2[4]+l2[5]+l2[6]+l2[7],
                l2[0],
                l2[1],
                l2[2],
                l2[3],                          
                l2[4],
                l2[5],
                l2[6],
                l2[7],

            l2[8]+l2[9]+l2[10],
                l2[8],
                l2[9],
                l2[10],

            l2[11]+l2[12]+l2[13],
                l2[11],
                l2[12],
                l2[13],

           l2[14]+l2[15]+l2[16]+l2[17]+l2[18],
                l2[14],
                l2[15],
                l2[16],
                l2[17],
                l2[18],


            l2[19]+l2[20]+l2[21]+l2[22]+l2[23]+l2[24],
                l2[19],
                l2[20],
                l2[21],
                l2[22],
                l2[23],
                l2[24],

            l2[25]+l2[26]+l2[27]+l2[28],
                l2[25],
                l2[26],
                l2[27],
                l2[28],

           l2[29]+l2[30],
                l2[29],
                l2[30],

        #     l2[31],
                l2[31],

        #     l2[32],
                l2[32],
            l2[33]

        ]
    # labels_ = ["Eastern Himalayan Region","wtern Himalayan Region","western Himalayan Region","western Himalayan Region","western Himalayan Region"]
    fig =go.Figure(go.Sunburst(
        labels=labels_,
        parents=parents_,
        values=values_
    ))
    fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))

    # fig.show()
    return fig
    
    
    
@app.callback(Output('lineChart2', component_property='figure'),
              [Input('year_slider2','value'),Input('state_dropdown','value')]
)
def update_fig2(slider_value,dropdown_value):
    data_ = data[data['Year'] == slider_value]
    data_ = data_.groupby('State').mean(numeric_only=True)
    data_ = data_.drop('Year',axis=1)
    data_ = data_.T
    for i in state_names:
        if(i not in dropdown_value):
            data_ = data_.drop(i,axis=1)
    data_.reset_index(inplace=True)
    fig = px.line(data_, x="index", y=data_.columns,
              hover_data={'index': "|%B %X, %Y"},
              title='custom tick labels')
    fig.update_xaxes(
        dtick="M1",
        tickformat="%b\n%Y")
    return fig



########################
# Map Callbacks
########################


@app.callback(Output('state-graph', component_property='figure'),
              [Input('india-graph', 'clickData'),Input('slider_year','value'),Input('month-slider','value')]
)
def update_states(clickData,slider_value,month_value):
    if clickData is not None:
        value = clickData['points'][0]['location']
    else:
        value = "Madhya Pradesh"
#     print(value,slider_value,month_value)
    data_ = data[data['State']==value]
    data_ = data_[data_['Year']==slider_value]
    data_ = data_.loc[:,['District',months[month_value]]]
    global temp2
    
    temp = temp2[temp2['ST_NM']==value]
    merged = temp.merge(data_, on="District").set_index("District")
    merged = merged.loc[:,['geometry',months[month_value]]]
    
    fig = px.choropleth_mapbox(merged,
                               geojson=merged.geometry,
                               locations=merged.index,
                               color=months[month_value],
                            #    range_color=(0, 500),
                               color_continuous_scale='Viridis_r',
                               mapbox_style='carto-positron',
                               center={'lat': indian_states_lat_log[value][0], 'lon': indian_states_lat_log[value][1]},
                               zoom=5,
                              )
    fig.update_layout(margin={'r':0,'l':0,'b':0,'t':0})
#     fig.show()
    return fig

@app.callback(
    Output('india-graph', 'figure'),
    [Input('slider_year', 'value'),Input('month-slider','value')]
)
def update_map(slider_value,month_value):
#     data_ = data.groupby('State')['Jul'].mean().reset_index()
#     print(slider_value,month_value)
    print(slider_value)
    data_ = data[data['Year']==slider_value]
    data_ = data_.groupby('State')[months[month_value]].mean().reset_index()
    global temp1
    temp = temp1
    merged = temp.merge(data_, on="State").set_index("State")
    merged = merged.loc[:,['geometry',months[month_value]]]
                        
    fig = px.choropleth_mapbox(merged, 
                            geojson=merged.geometry,
                           locations=merged.index,
                           color=months[month_value],
                        #    range_color=(0, 500),
                           color_continuous_scale='Viridis_r',
                           mapbox_style='carto-positron',
                           center={'lat': 20.5937, 'lon': 78.9629},
                           zoom=3,
                          )
    fig.update_layout(margin={'r':0,'l':0,'b':0,'t':0})
    return fig


############
# Line Charts Callback
###########

@app.callback(
    Output("rainfall-scatter-plot", "figure"),
    [Input("state-dropdown-1", "value"),
     Input("state-dropdown-2", "value")]
)
def update_scatter_plot(state_1, state_2):
    state_1_data = data[data["State"] == state_1]
    state_2_data = data[data["State"] == state_2]
    
    avg_monthly_data_1 = []
    avg_monthly_data_2 = []
    for m in months:
        monthly_data_1 = state_1_data[months[m]]
        monthly_data_2 = state_2_data[months[m]]
        
        if(len(monthly_data_1) == 0):
            avg_monthly_data_1.append(0)
        else:
            avg_monthly_data_1.append(monthly_data_1.sum()/len(monthly_data_1))
            
        if(len(monthly_data_2) == 0):
            avg_monthly_data_2.append(0)
        else:
            avg_monthly_data_2.append(monthly_data_2.sum()/len(monthly_data_2))
    # Create the Plotly scatter plot
    monthly_avg_1 = pd.DataFrame(avg_monthly_data_1, columns=[state_1])
    monthly_avg_2 = pd.DataFrame(avg_monthly_data_2, columns=[state_2])
    fig = px.scatter(monthly_avg_1, x=state_1, y=monthly_avg_2[state_2], 
                     title="Comparison of Average Rainfall")
    fig.update_xaxes(title=state_1)
    fig.update_yaxes(title=state_2)
    fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',  
    paper_bgcolor='#b9d2e7',  
    font_color='rgb(0,0,0)',  
)
    return fig


@app.callback(
    Output("rainfall-bar-chart", "figure"),
    Input("state-dropdown", "value")
)
def update_bar_chart(state):
    # print(state)
    state_data = data[data["State"] == state]
    # print(state_data[0:2])
    avg_monthly_data = []
    for m in months:
        monthly_data = state_data[months[m]]
        if(len(monthly_data) == 0):
            avg_monthly_data.append(0)
        else:
            avg_monthly_data.append(monthly_data.sum()/len(monthly_data))
    monthly_avg = pd.DataFrame(avg_monthly_data, columns=['rainfall'])
    fig = px.bar(monthly_avg, x=monthList, y="rainfall")
    fig.update_xaxes(title='Months')
    fig.update_yaxes(title='Rainfall')
    fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',  
    paper_bgcolor='#b9d2e7',  
    font_color='rgb(0,0,0)',  
)
    return fig
update_bar_chart('Andhra Pradesh')
# #b9d2e7
@app.callback(Output('rainfall-correlation', 'figure'), Input('slider', 'value'))
def updateRainfall(sliderVal):
    print('changing rainfall')
    temp = data[data['Year']==sliderVal]
    dfR = pd.DataFrame({'avgRainfall' : []})
    for m in months:
        t1 = temp[months[m]]
        avgRainfall = t1.sum()/len(t1)
        dfR.loc[m, 'avgRainfall'] = avgRainfall
    df = pd.DataFrame()
    df['avgRainfall'] = dfR
    fig = px.line(df, x=list(months.values()), y=['avgRainfall'])
    fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',  
    paper_bgcolor='#e2d2bc',  
    font_color='rgb(0,0,0)',  
)
    fig.update_xaxes(title='Months')
    fig.update_yaxes(title='Rainfall')
    return fig

@app.callback(Output('temp-correlation', 'figure'), Input('slider', 'value'))
def updateTemperature(sliderVal):
    print('changing temp')
    temp = temperatureData[temperatureData['Year']==sliderVal]
    dfT = pd.DataFrame({'avgTemperature' : []})
    for m in months:
        t1 = temp[months[m]]
        avgTemperature = t1.sum()/len(t1)
        dfT.loc[m, 'avgTemperature'] = avgTemperature
    df = pd.DataFrame()
    df['avgTemperature'] = dfT
    fig = px.line(df, x=list(months.values()), y=['avgTemperature'], color_discrete_sequence=['red'])
    fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',  
    paper_bgcolor='#e2d2bc',  
    font_color='rgb(0,0,0)',  
)
    fig.update_xaxes(title='Months')
    fig.update_yaxes(title='Temperature')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True,use_reloader=False)



