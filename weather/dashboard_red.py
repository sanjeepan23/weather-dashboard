from h2o_wave import ui, data, Q, pack
from datetime import datetime
from .common import global_nav
from .Utils import *

async def show_dashboard(q: Q,city):
    
    res_data_current = get_Data_current(city)
    res_data_forecast = get_Data_forecast(city)

    
    
    q.page['sidebar'] = ui.tall_article_preview_card(
        box='1 2 2 7',
        subtitle=res_data_current['name'],
        title= "Partial Cloudy",
        value=str(str(res_data_current['main']['temp']) + " °F"),
        name='tall_article',
        image='https://images.pexels.com/photos/3225517/pexels-photo-3225517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260', # noqa

    )
    

    rows1= extract_forecast_temp(res_data_forecast["hourly"])
    q.page['main'] = ui.form_card(
        box='3 2 7 5',
        title=str("Temparature Forecast"),
        items=[
            ui.text(str("All the temparatures in F")),
            ui.stats(items=[
                ui.stat(label=str("Forecast Temparatures for coming 3 days")),
                # ui.stat(label=str("Today's Temparature graph"), value=str("Today's Temparature graph")),
                # ui.stat(label=str("Today's Temparature graph"), value=str("Today's Temparature graph")),
            ]),
            ui.visualization(
                plot=ui.plot([
                    ui.mark(type='area', x_scale='time', x='=date', y='=visitors', color='=site',
                            color_range='$blue $tangerine'),
                    ui.mark(type='line', x_scale='time', x='=date', y='=visitors', color='=site',
                            color_range='$blue $tangerine'),
                ]),
                data=data(
                    fields=['site', 'date', 'visitors'],
                    rows=rows1,
                    pack=True
                ),
                # height='210px',
            )
        ],
    )

    q.page['header'] = ui.header_card(box='1 1 9 1', title='Weather Forecast', subtitle='Dashboard',nav=global_nav)


    q.page['Humidity'] = ui.tall_gauge_stat_card(
        box='1 11 2 3',
        title="Humidity",
        value=str(res_data_current['main']['humidity']),
        aux_value='%',
        plot_color='$red',
        progress=res_data_current['main']['humidity']/100 
    )


    q.page['Pressure'] = ui.tall_gauge_stat_card(
        box='1 9 2 2',
        title="Pressure",
        value=str(res_data_current['main']['pressure']),
        aux_value='Pascal',
        plot_color='$green',
        progress=res_data_current['main']['pressure']/100
    )

    
    q.page['visibility'] = ui.tall_gauge_stat_card(
        box='3 7 1 2',
        title="Visibility",
        value=str(res_data_current['visibility']),
        aux_value='',
        plot_color='$blue',
        progress=0.8
    )


    q.page['wind1'] = ui.small_stat_card(
        box='4 7 1 2',
        title='Wind Speed',
        value=str(str(res_data_current['wind']['speed']*3.6)[:4]+ " Km/h")
    )


    q.page['wind2'] = ui.small_stat_card(
        box='5 7 1 1',
        title='Wind degree',
        value=str(str(res_data_current['wind']['deg']) + " °F")
    )

   
    q.page['Clouds'] = ui.small_stat_card(
        box='5 8 1 1',
        title='Clouds',
        value=str(res_data_forecast['current']['clouds'])
    )


    menu = '''
    <ol>
    {{#each dishes}}
    <li>{{name}} -  <strong>{{price}}</strong> </li>
    <br>
    {{/each}}
    </ol
    '''
    q.page['Temparatute'] = ui.template_card(
        box='6 7 3 2',
        title='Today\'s Temparature',
        content=menu,
        data=pack(dict(dishes=[
            dict(name='Feel\'s Like Temparature', price=str(str(res_data_current['main']['feels_like']) + " °F")),
            dict(name='Maximum Temparature', price=str(str(res_data_current['main']['temp_max']) + " °F")),
            dict(name='Minimum Temparature', price=str(str(res_data_current['main']['temp_min']) + " °F")),
        ])),
    )
    

    dt = datetime.datetime.utcfromtimestamp(int(res_data_current["sys"]["sunrise"])).strftime('%Y-%m-%d %H:%M:%S')
    q.page['Sunrise'] = ui.small_stat_card(
        box='9 7 1 1',
        title='Sunrise Time',
        value=str(str(dt.split()[1][:-3]) + " AM")
    )


    dt = datetime.datetime.utcfromtimestamp(int(res_data_current["sys"]["sunset"])).strftime('%Y-%m-%d %H:%M:%S')
    q.page['sunset'] = ui.small_stat_card(
        box='9 8 1 1',
        title='Sunset Time',
        value=str(str(dt.split()[1][:-3]) + " PM")
    )
    

    rows2= extract_forecast_humty(res_data_forecast["hourly"])
    rows3= extract_forecast_wind_spd(res_data_forecast["hourly"])
    q.page['bottom'] = ui.form_card(
        box='3 9 7 5',
        title=str("Humidity Forecast"),
        items=[
            ui.text(str("All the Humidity in g/m³")),
            ui.stats(items=[
                ui.stat(label=str("Forecast Humidity for coming 3 days")),
                # ui.stat(label=str("Today's Temparature graph"), value=str("Today's Temparature graph")),
                # ui.stat(label=str("Today's Temparature graph"), value=str("Today's Temparature graph")),
            ]),
            ui.visualization(
                plot=ui.plot([
                    ui.mark(type='area', x_scale='time', x='=date', y='=visitors', color='=site',
                            color_range='$blue $tangerine'),
                    ui.mark(type='line', x_scale='time', x='=date', y='=visitors', color='=site',
                            color_range='$blue $tangerine'),
                ]),
                data=data(
                    fields=['site', 'date', 'visitors'],
                    rows=rows2 + rows3,
                    pack=True
                ),
                # height='210px',
            )
        ],
    )
   

    q.page['footer'] = ui.footer_card(box='5 12 2 1', caption='(c) 2021 All rights reserved.')

    await q.page.save()
