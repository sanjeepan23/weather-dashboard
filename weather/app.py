from h2o_wave import main, app, Q
from .dashboard_red import show_dashboard

@app('/')
async def serve(q: Q):
    route = q.args['#']
    if route == 'dashboards/London':
        await show_dashboard(q,"London")
    elif route == 'dashboards/Toronto':
        await show_dashboard(q,"Toronto")
    elif route == 'dashboards/NewYork':
        await show_dashboard(q,"NewYork")
    elif route == 'dashboards/Colombo':
        await show_dashboard(q,"Colombo")
    elif route == 'dashboards/Paris':
        await show_dashboard(q,"Paris")

    elif route == 'dashboards/Mumbai':
        await show_dashboard(q,"Mumbai")
    elif route == 'dashboards/Singapore':
        await show_dashboard(q,"Singapore")
    elif route == 'dashboards/Melbourne':
        await show_dashboard(q,"Melbourne")
    elif route == 'dashboards/Tokyo':
        await show_dashboard(q,"Tokyo")
    else:
        await show_dashboard(q,"Colombo")
