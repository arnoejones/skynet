import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_table

from app.config import Config

colors = {
    'background': '#006699',
    'text': '#f2f2f2'
}



def server_layout():
    layout = html.Div(style={'color': 'red'}, children = [
        html.Div([
            html.Label("Skynet: ", style={'color': 'green'}),
            html.A("Home Page   ", href='/', style={'color': 'green'}),
            html.A("Radio Page   ", href='/radio',style={'color': 'green'})
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
                "page_size": 35,
            },
            navigation="page",

            n_fixed_rows=1,
            # style_table={'overflowX': 'scroll'},
            style_table={'backgroundColor': 'rgb(50, 50, 50)'},

            style_cell_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': 'rgb(248, 248, 248)',
                    'if': {'row_index': 'even'},
                    'backgroundColor': 'rgb(148, 148, 148)'

                }],
            style_cell={
                'backgroundColor': 'rgb(50, 50, 50)',
                'color': 'white',
                # 'minWidth': '0px', 'maxWidth': '40px',
                'whiteSpace': 'normal',
                'textOverflow': 'ellipsis',
                'textAlign': 'left'
            },
            style_header={
                'backgroundColor': 'green',
                'fontWeight': 'bold'
            },
        ),
        html.Div(id='datatable-interactivity-container'),
        html.Div(id='footer-div-id',
                 children=(html.H3("I'm at the bottom!",
                                   style={
                     'textAlign': 'center',
                     'color':colors['text'],
                     })),
        )
        ]
    )
    return layout