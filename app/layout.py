import dash_html_components as html
import dash_table

from app.config import Config


def server_layout():
    layout = html.Div([
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
                'backgroundColor': 'black',
                'fontWeight': 'bold'
            },
        ),
        html.Div(id='datatable-interactivity-container')
        ]
    )
    return layout