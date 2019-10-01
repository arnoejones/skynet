class QueriesDictionary():
    # for flask, what shows on the radio list is the 2nd part of the tuple
    def queries(self):
        queries = [
            (
                "SELECT DISTINCT count(EgmGamePackages.GamePackage) AS 'Game Packages Tested G2S Disabled, SAS Enabled', GamePackage, EgmConfig.G2S AS 'G2S is False', EgmConfig.SAS AS 'SAS is True' FROM dbo.EgmGamePackages inner JOIN  EgmConfig ON EgmConfig.config_id=EgmGamePackages.config_id WHERE G2S = 'G2SFalse' AND SAS = 'SASTrue' GROUP BY GamePackage, G2S, SAS ORDER BY GamePackage",
                "Show the number of times a game package has been tested with G2S disabled and SAS enabled"
            ),
            (
                "SELECT DISTINCT count(EgmGamePackages.GamePackage) AS 'Game Packages Tested G2S Enabled, SAS Enabled', GamePackage, EgmConfig.G2S AS 'G2S Enabled', EgmConfig.SAS AS 'SAS Enabled' FROM dbo.EgmGamePackages inner JOIN  EgmConfig ON EgmConfig.config_id=EgmGamePackages.config_id WHERE G2S = 'G2STrue' AND SAS = 'SASTrue' GROUP BY GamePackage, G2S, SAS ORDER BY GamePackage",
                "Show the number of times a game package has been tested with G2S enabled and SAS enabled"
            ),
            (
                "SELECT DISTINCT count(EgmGamePackages.GamePackage) AS 'Game Packages Tested G2S Disabled, SAS Disabled', GamePackage, EgmConfig.G2S AS 'G2S Disabled', EgmConfig.SAS AS 'SAS Disabled' FROM dbo.EgmGamePackages inner JOIN  EgmConfig ON EgmConfig.config_id=EgmGamePackages.config_id WHERE G2S = 'G2SFalse' AND SAS = 'SASFalse' GROUP BY GamePackage, G2S, SAS ORDER BY GamePackage",
                "Show the number of times a game package has been tested with G2S disabled and SAS disabled"
             ),
            (
                "SELECT DISTINCT count(EgmGamePackages.GamePackage) AS 'Game Packages Tested G2S Enabled, SAS Disabled', GamePackage, EgmConfig.G2S AS 'G2S Enabled', EgmConfig.SAS AS 'SAS Disabled' FROM dbo.EgmGamePackages inner JOIN  EgmConfig ON EgmConfig.config_id=EgmGamePackages.config_id WHERE G2S = 'G2STrue' AND SAS = 'SASFalse' GROUP BY GamePackage, G2S, SAS ORDER BY GamePackage",
                "Show the number of times a game package has been tested with G2S enabled and SAS disabled"
            ),
            (
                "SELECT Foundation, count(Foundation) AS 'How many times has a Foundation been tested' FROM EgmConfig GROUP BY Foundation ORDER BY 'How many times has a Foundation been tested' DESC",
                "How many times has a Foundation been tested"
            ),
            (
                "SELECT count(EgmGamePackages.config_id) AS 'How many times has a Game Package been tested on each Foundation', EgmGamePackages.GamePackage, EgmConfig.Foundation FROM EgmGamePackages INNER JOIN EgmConfig ON EgmConfig.config_id=EgmGamePackages.config_id GROUP BY EgmGamePackages.GamePackage, EgmConfig.Foundation ORDER BY 'How many times has a Game Package been tested on each Foundation' DESC",
                "How many times has a Game Package been tested on each Foundation"
            ),
            (
                "SELECT DISTINCT EgmConfig.Foundation AS 'Foundations Tested Last 30 Days', EgmHardware.IP AS IP, EgmStatus.DateOfLogFile FROM EgmConfig INNER JOIN EgmStatus ON EgmStatus.config_id = EgmConfig.config_id JOIN EgmHardware ON EgmConfig.hardware_id = EgmHardware.hardware_id WHERE EgmStatus.LogTimeStamp >= DATEADD(DAY, -30, GETDATE()) AND EgmStatus.LogTimeStamp <= GETDATE() GROUP BY EgmConfig.Foundation, EgmHardware.IP, EgmStatus.DateOfLogFile ORDER BY EgmConfig.Foundation, EgmHardware.IP, EgmStatus.DateOfLogFile Desc",
                "Foundations Tested in the Last 30 Days"
            ),
            (
                "SELECT distinct EgmConfig.Foundation AS 'Foundations Tested Last 7 Days' FROM EgmConfig INNER JOIN EgmStatus ON EgmStatus.config_id = EgmConfig.config_id WHERE EgmStatus.LogTimeStamp >= DATEADD(DAY, -7, GETDATE()) AND EgmStatus.LogTimeStamp <= GETDATE() GROUP BY EgmConfig.Foundation ORDER BY EgmConfig.Foundation Desc",
                "Foundations Tested in the Last Week"
            ),
            (
                "SELECT DISTINCT DateOfLogFile AS 'Last 5 Days of Testlogs' FROM EgmStatus WHERE DateOfLogFile BETWEEN DATEADD(DAY, -7, GETDATE()) AND DATEADD(DAY, 1, GETDATE()) ORDER BY DateOfLogFile DESC",
                "Last 5 Days Tests Were Run (Automation Check)"
            ),
            (
                "SELECT DISTINCT DateOfLogFile AS 'Testlogs From the Future (Misconfigured EGM)' FROM EgmStatus WHERE DateOfLogFile > GETDATE() ORDER BY DateOfLogFile DESC",
                "Log Files From the Future (Misconfigured EGM's)"
            ),
            (
                "SELECT count(DISTINCT LogTimeStamp) AS 'Total Log Entries' FROM EgmStatus",
                "Grand Total of All Log Entries"
            ),
            (
                "SELECT Distinct DateOfLogFile AS 'Date of all Logs', COUNT(LogTimeStamp) AS 'Total Log Entries for Date' FROM EgmStatus GROUP BY DateOfLogFile",
                "For Each Date, How Many Log Entries Are There"
            ),
            (
                "SELECT DISTINCT EgmConfig.Foundation, EgmConfig.OI, EgmHardware.Cabinet, EgmHardware.Brainbox, EgmHardware.CPU, EgmHardware.TotalRam, EgmConfig.ButtonPanelFirmware, EgmConfig.VideoTopper, EgmConfig.Printer, EgmConfig.Lighting, EgmConfig.Digitizer, EgmConfig.ButtonPanelHardware FROM EgmHardware INNER JOIN EgmConfig ON EgmHardware.hardware_id = EgmConfig.hardware_id ORDER BY EgmConfig.Foundation DESC ",
                "What hardware are we running a particular AI or OS on"
            ),
            (
                "SELECT COUNT(Foundation) AS 'Count of Times M-Series (*M0001) Tested', Foundation, Push AS 'Push Nunber' FROM EgmConfig WHERE Foundation LIKE '%M0001' GROUP BY Push, Foundation ORDER BY Push DESC",
                "Count the Number of Times M-Series (*M0001) Has Been Tested"
            ),
            (
                "SELECT EgmGamePackages.GamePackage AS 'M-Series Game Package Tested On Which Foundation', COUNT(EgmGamePackages.GamePackage) AS 'Tested', EgmConfig.Foundation FROM EgmGamePackages JOIN EgmConfig ON EgmGamePackages.config_id = EgmConfig.config_id WHERE Foundation LIKE 'AI020000M%%%%%' GROUP BY GamePackage, Foundation ORDER BY EgmGamePackages.GamePackage DESC ",
                "Game Packages Tested Against M-Series on Which Foundation"
            ),
            (
                "SELECT DISTINCT EgmHardware.Cabinet, EgmConfig.Foundation, EgmGamePackages.GamePackage AS 'Game Packages Tested On Foundation and Cabinet' FROM EgmHardware JOIN EgmConfig ON EgmHardware.hardware_id = EgmConfig.hardware_id JOIN EgmGamePackages ON EgmGamePackages.config_id = EgmConfig.config_id GROUP BY EgmHardware.Cabinet, EgmConfig.Foundation, EgmGamePackages.GamePackage",
                "What Game Packages Tested Against Which Foundation on What Cabinet"
            ),
            (
                "SELECT TOP 0 "
                "EgmHardware.IP,"
                "EgmHardware.BrainBox,"
                "EgmHardware.Cabinet,"
                "EgmHardware.CPU,"
                "EgmHardware.TotalRam,"
                "EgmConfig.Foundation,"
                "EgmConfig.AIPackage,"
                "EgmConfig.Push,"
                "EgmConfig.FI,"
                "EgmConfig.OI,"
                "EgmConfig.AvailableRam,"
                "EgmConfig.G2S,"
                "EgmConfig.SAS,"
                "EgmConfig.Boot1,"
                "EgmConfig.Boot2,"
                "EgmConfig.BV,"
                "EgmConfig.ButtonPanelFirmware,"
                "EgmConfig.VideoTopper,"
                "EgmConfig.Printer,"
                "EgmConfig.Lighting,"
                "EgmConfig.Digitizer,"
                "EgmConfig.ButtonPanelHardware,"
                "EgmGamePackages.GamePackage,"
                "EgmStatus.GameName,"
                "EgmStatus.Game,"
                "EgmStatus.Theme,"
                "EgmStatus.Percentage,"
                "EgmStatus.Bet,"
                "EgmStatus.Win,"
                "EgmStatus.Denom,"
                "EgmStatus.Credit,"
                "EgmStatus.Currency,"
                "EgmStatus.LogTimeStamp,"
                "EgmStatus.DateOfLogFile,"
                "EgmStatus.ActionItem,"
                "EgmStatus.ConfigItemChanged "
                "FROM EgmHardware "
                "JOIN EgmConfig ON EgmHardware.hardware_id = EgmConfig.hardware_id "
                "JOIN EgmGamePackages ON EgmConfig.config_id = EgmGamePackages.config_id "
                "JOIN EgmStatus ON EgmConfig.config_id = EgmStatus.config_id ",
                "Just What Items are Available to Me?"
            ),
            (
                "SELECT distinct CONVERT(VARCHAR(11),DateOfLogFile) AS 'Dates of Tests That Have Been Run' FROM EgmStatus ORDER BY 'Dates of Tests That Have Been Run'",
                "Show All Dates That Tests Have Been Run"
            ),
            (
                "SELECT distinct MIN(DateOfLogFile) AS 'Oldest Logfile' , MAX(DateOfLogFile) AS 'Newest Logfile' FROM EgmStatus",
                "Find the oldest and newest Log file"
            ),
            (
                "SELECT m.MeterName, mc.MeterCategoryName, ssm.MasterValue, ssm.PeriodValue, ss.Foundation, ss.Date FROM Meter m JOIN MeterCategory mc ON m.MeterCategoryID = mc.MeterCategoryID JOIN SnapshotMeter ssm ON m.MeterID = ssm.MeterID JOIN Snapshot ss ON ss.SnapshotID = ssm.SnapshotID ORDER BY mc.MeterCategoryName",
                "Get All the Values of All Meters"
            ),
            (
                "SELECT distinct SecurityMeters.SecurityMeterName, cast(SecurityMeterValues.SecurityMeterValue AS INT) AS 'Power Hits per Foundation per Date', SecurityMeterValues.DateOfLogFile, EgmConfig.Foundation FROM SecurityMeters JOIN SecurityMeterValues ON SecurityMeters.security_meter_id = SecurityMeterValues.security_meter_id JOIN EgmConfig ON SecurityMeterValues.config_id = EgmConfig.config_id AND SecurityMeters.SecurityMeterName LIKE 'Total power failures%' and cast(SecurityMeterValues.SecurityMeterValue AS INT) > 0 ORDER BY EgmConfig.Foundation",
                "Get Number of Power Failures per Foundation per date"
            ),
            (
                "SELECT distinct SecurityMeters.SecurityMeterName, SecurityMeterValues.SecurityMeterValueDateTime AS 'Last Power On by Foundation', SecurityMeterValues.DateOfLogFile, EgmConfig.Foundation FROM SecurityMeters JOIN SecurityMeterValues ON SecurityMeters.security_meter_id = SecurityMeterValues.security_meter_id JOIN EgmConfig ON SecurityMeterValues.config_id = EgmConfig.config_id AND SecurityMeters.SecurityMeterName LIKE 'Last power on%' ORDER BY EgmConfig.Foundation",
                "Last Power On by Foundation"
            ),
            (
                'SELECT distinct EgmConfig.Foundation, COUNT(EgmStatus.Bet) as "Total Games Played Against All Tested Foundations" FROM EgmStatus JOIN EgmConfig ON EgmStatus.config_id = EgmStatus.config_id WHERE Bet is not null GROUP BY EgmConfig.Foundation order by "Count" DESC',
                "Total Games Played Against All Tested Foundations"
             ),
            (
                "SELECT distinct EgmConfig.Foundation, COUNT(EgmStatus.Bet) AS 'Total Games Played Against All Tested Foundations when G2S is Enabled' FROM EgmStatus JOIN EgmConfig ON EgmStatus.config_id = EgmStatus.config_id WHERE Bet is not null AND EgmConfig.G2S LIKE 'G2STrue' GROUP BY EgmConfig.Foundation ",
                "Total Games Played Against All Tested Foundations when G2S is Enabled"
            ),
            (
                "SELECT distinct EgmConfig.Foundation, COUNT(EgmStatus.Bet) AS 'Total Games Played Against All Tested Foundations when SAS is Enabled' FROM EgmStatus JOIN EgmConfig ON EgmStatus.config_id = EgmStatus.config_id WHERE Bet is not null AND EgmConfig.SAS LIKE 'SASTrue' GROUP BY EgmConfig.Foundation",
                "Total Games Played Against All Tested Foundations when SAS is Enabled"
            ),
            (
                "SELECT distinct EgmConfig.Foundation, COUNT(EgmStatus.Bet) AS 'Total Games Played Against All Tested Foundations when SAS is Enabled and G2S is Disabled' FROM EgmStatus JOIN EgmConfig ON EgmStatus.config_id = EgmStatus.config_id WHERE Bet is not null AND EgmConfig.SAS LIKE 'SASTrue' AND EgmConfig.G2S LIKE 'G2SFalse' GROUP BY EgmConfig.Foundation",
                "Total Games Played Against All Tested Foundations when SAS is Enabled and G2S is Disabled"
            ),
            (
                "SELECT distinct EgmConfig.Foundation, COUNT(EgmStatus.Bet) AS 'Total Games Played Against All Tested Foundations when SAS is Disabled and G2S is Enabled' FROM EgmStatus JOIN EgmConfig ON EgmStatus.config_id = EgmStatus.config_id WHERE Bet is not null AND EgmConfig.SAS LIKE 'SASFalse' AND EgmConfig.G2S LIKE 'G2STrue' GROUP BY EgmConfig.Foundation",
                "Total Games Played Against All Tested Foundations when SAS is Disabled and G2S is Enabled"
            ),
            (
                "SELECT distinct EgmConfig.Foundation, COUNT(EgmStatus.Bet) AS 'Total Games Played Against All Tested Foundations when SAS is Disabled and G2S is Disabled' FROM EgmStatus JOIN EgmConfig ON EgmStatus.config_id = EgmStatus.config_id WHERE Bet is not null AND EgmConfig.SAS LIKE 'SASFalse' AND EgmConfig.G2S LIKE 'G2SFalse' GROUP BY EgmConfig.Foundation",
                "Total Games Played Against All Tested Foundations when SAS is Disabled and G2S is Disabled"
            ),
            (
                "SELECT distinct EgmConfig.Foundation, COUNT(EgmStatus.Bet) AS 'Total Games Played Against All Tested Foundations when SAS is Disabled and G2S is Disabled AND Brain Box is a 40Plus' FROM EgmStatus JOIN EgmConfig ON EgmStatus.config_id = EgmStatus.config_id JOIN EgmHardware ON EgmConfig.hardware_id = EgmHardware.hardware_id WHERE Bet is not null AND EgmConfig.SAS LIKE 'SASFalse' AND EgmConfig.G2S LIKE 'G2SFalse' AND EgmHardware.BrainBox LIKE '40Plus' GROUP BY EgmConfig.Foundation",
                "Total Games Played Against All Tested Foundations when SAS is Disabled and G2S is Disabled AND Brain Box is a 40Plus"
            ),
            (
                "select count(GameName) AS 'How Many Times a Game has been Played Against a Foundation', GameName, EC.Foundation from EgmStatus join EgmConfig EC on EgmStatus.config_id = EC.config_id where EgmStatus.Bet is not null Group by GameName, Foundation order by count(GameName) desc",
                'How Many Times a Game has been Played Against a Foundation'
            )


        ]
        return queries
