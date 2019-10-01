import dash_html_components as html
import dash_table
import dash_bootstrap_components as dbc
from app.config import Config


def nav_bar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="http://10.213.81.6:5000/home")),
            dbc.NavItem(dbc.NavLink("Query", href="http://10.213.81.6:5000/radio")),
            dbc.NavItem(dbc.NavLink("Custom", href="http://10.213.81.6:5000/custom")),
            # dbc.NavItem(dbc.NavLink("Page 1", href="#")),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("Technical Stuff", header=True),
                    dbc.DropdownMenuItem("Raw SQL Query", href="http://10.213.81.6:5000/raw_sql_query"),
                    dbc.DropdownMenuItem("Query Description", href="http://10.213.81.6:5000/sql_description"),
                ],
                nav=True,
                in_navbar=True,
                label="More",
            ),
        ],

        brand="Skynet Query Results",
        brand_href="http://10.213.81.6:5000//home",
        sticky="right",
    )
    return navbar


def server_layout():
    layout = html.Div(id="table-header-div", children=[
        html.Div([
            nav_bar(),
        ]),

        # content will be rendered in this element
        html.Div(id='page-content'),

        dash_table.DataTable(
            id='skynet-datatable',
            columns=[{"name": i, "id": i, "deletable": False} for i in Config.df.columns],
            data=Config.df.to_dict("rows"),


            sort_action='native',
            sort_mode='multi',
            page_action="native",
            page_current=0,
            # page_size=40,
            fixed_rows={'headers':True, 'data':0},

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
                'minWidth': '0px', 'maxWidth': '40px',
                'whiteSpace': 'normal',
                'textOverflow': 'ellipsis',
                'textAlign': 'left',
            },
            # css=[{
                # 'selector': '.dash-cell div.dash-cell-value',
                # 'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'
            # }],

        ),

        html.Div(children=
                 [html.Br(),
                  html.A(html.Button(children='Download table as xlsx',
                                     id='table_download_button',
                                     style={'color': 'blue'}),
                                     href="/download_excel/", ),

                  html.P(" (Large files can take a few seconds)",
                         style={
                             'color': 'green'
                         })
                  ])
        ,
        html.Div(id='datatable-interactivity-container'),
    ])
    return layout
