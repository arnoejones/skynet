import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_table
import dash_bootstrap_components as dbc
from app.config import Config

colors = {
    'background': '#006699',
    'text': '#f2f2f2'
}
def nav_bar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Link", href="#")),
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Menu",
                children=[
                    dbc.DropdownMenuItem("Entry 1"),
                    dbc.DropdownMenuItem("Entry 2"),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Entry 3"),
                ],
            ),
        ],
        brand="Demo",
        brand_href="#",
        sticky="top",
    )
    return navbar

def server_layout():
    layout = html.Div(id= "table-header-div", children = [
        html.Div([
            html.Label("Skynet Table: ", style={'color':'blue', 'fontSize':22},id="skynet-label"),
            html.A("Home",style={'color':'blue',
                                     'fontSize':20,
                                     'backgroundColor':'blue',
                                     'color':'white',
                                     'boxShadow':'0 3px 0 #006FBA',
                                     'padding':'5px 5px 5px 5px'},
                id="home-page-label", href='/', target='_blank'
            ),
            html.A("Query",style={'color':'blue',
                                     'fontSize':20,
                                     'backgroundColor':'#EF6918',
                                     'color':'white',
                                     'boxShadow':'0 3px 0 #006FBA',
                                     'padding':'5px 5px 5px 5px'},
                id="radio-page-label", href='/radio', target='_blank')
    ]),
        # content will be rendered in this element
        html.Div(id='page-content'),

        dash_table.DataTable(
            id='skynet-datatable',

            columns=[{"name": i, "id": i, "deletable": False} for i in Config.df.columns],

            data=Config.df.to_dict("rows"),
            editable=False,
            filtering=False,
            sorting=True,
            sorting_type="multi",
            row_selectable="multi",
            row_deletable=True,
            selected_rows=[],
            pagination_mode="fe",
            pagination_settings={
                "displayed_pages": 1,
                "current_page": 0,
                "page_size": 45,
            },
            navigation="page",

            n_fixed_rows=1, #keep the header on the screen, do not let it scroll.
            # style_table={'overflowX': 'scroll'},
            style_table={'backgroundColor': 'rgb(50, 50, 50)',
                         'maxHeight':'30',
                         'overflowY':'scroll'},

            style_cell_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': '#33adff',
                    'if': {'row_index': 'even'},
                    'backgroundColor': '#0088cc'

                }],
            style_cell={
                'font-weight': 'bold',
                'backgroundColor': '#33bbff',
                'color': 'white',
                #'minWidth': '0px', 'maxWidth': '40px', this messes up the header
                'whiteSpace': 'normal',
                'textOverflow': 'ellipsis',
                'textAlign': 'left'
            },
            style_header={
                'backgroundColor': '#006699',
                'fontWeight': 'bold'
            },
        ),
        html.Div(id='datatable-interactivity-container'),

        html.Div(children=
                 [html.A("download excel", href="/download_excel/")])

    ,


    ])
    return layout