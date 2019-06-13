class QueriesDictionary():
    # for flask, what shows on the radio list is the 2nd part of the tuple
    def queries(self):
        queries = [
            (
            "SELECT count(AI) AS 'AI count',AI AS 'AI', G2S AS 'G2S Enabled', SAS AS 'SAS Enabled', PushNumber AS 'Push Number', DateOfTest AS 'Date of Test', Theme AS 'Theme' FROM GameLogs WHERE DateOfTest BETWEEN '2018-10-08'and '2019-04-08' AND AI LIKE '%m%' AND G2S LIKE '%G2STrue%' GROUP BY AI, G2S, SAS, PushNumber, DateOfTest, Theme ",
            "Count of AIs, pushes, with G2S and SAS enabled"),
            (
            "select top 5 count(GameName) as 'Game Name Count with G2S Enabled', GameName as 'Game Name Enabled' from GameLogs where GameName <> '' and G2S like '%G2STrue%' Group by GameName Order By 'Game Name Count with G2S Enabled' DESC",
            "Count of Games tested with G2S enabled"),
            (
            "SELECT COUNT(GameName) AS 'Game Name Count', GameName AS 'Game Name', Denom AS 'Denom', Bet AS 'Bet', AI AS 'AI', Win AS 'Win', G2S as 'G2S', SAS AS 'SAS' FROM GameLogs WHERE GameName != '' GROUP BY Bet, GameName, AI, Denom, Win, G2S, SAS ORDER BY GameName ASC",
            "List of Game Stats"),
            (
            "SELECT GameName AS '# of Games Tested', COUNT(GameName) AS 'Games Tested Amount' FROM GameLogs WHERE GameName <> '' GROUP BY GameName ORDER BY 'Games Tested Amount' DESC",
            "Number of Times a Game's Been Tested"),
            (
            "SELECT top 5 count(GameName) as 'Game Name Count with G2S Enabled', GameName as 'Game Name Enabled' from GameLogs where GameName <> '' and G2S like '%G2STrue%' Group by GameName Order By 'Game Name Count with G2S Enabled' DESC",
            "Last 5 Days Tests Were Run"),
        ]
        return queries
