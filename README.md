# skynet
tl;dr Query SQLServer db and put the results in a Dash Datatable with the datatable refreshing to show the results of the new query.

The problem I was faced with was how to retrieve and present legacy data stored in a SQL Server database.  
A requirement was that the results should accessable by anyone and not be required to install an app locally.  Serve it via http then.
I didn't want to install Apache or any other heavy server so I elected to utilize flask to serve and dash for the layout.
There is a dictionary of tuples that represent the query description and the actual query.  This dictionary is read by the radio.html
page and displayed as a list of radio buttons.  The user clicks a button and then submits the request.  The resultant query string queries
the SQL server and returns the results to the dash layout.  The dash layout is a defined method instead of being called directly.  

One of the issues I ran across while developing this app was that no matter which query I selected, the Datatable would always display the 
default set of results - never refreshing.  I spent an embarrassing amount of time trying to figure this problem out.  The key to 
getting the datatable to refresh and display the new query results was to define the layout in a function and call that function from the 
dash_app.layout.  The 'gotcha' was that instead of dash_app.layout = layout.server_layout(), I needed instead to pass in the object as in
dash_app.layout = layout.server_layout  Notice the lack of ().
