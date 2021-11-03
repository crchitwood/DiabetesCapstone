SELECT  * 
FROM dbo.diabetestemp 
INNER JOIN dbo.race_uninsured_2008
ON dbo.diabetestemp.race = dbo.race_uninsured_2008.Race