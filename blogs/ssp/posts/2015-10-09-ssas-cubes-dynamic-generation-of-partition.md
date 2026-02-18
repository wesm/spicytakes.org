---
title: "SSAS Cubes – Dynamic generation of partition"
date: 2015-10-09
url: https://www.ssp.sh/blog/ssas-cubes-dynamic-generation-of-partition/
slug: ssas-cubes-dynamic-generation-of-partition
word_count: 751
---

![SSAS Cubes – Dynamic generation of partition](https://www.ssp.sh/blog/ssas-cubes-dynamic-generation-of-partition/images/cube-partitions-e1444391131116.jpg)

Contents

There is no easy way to generate partition for SSAS Cubes by default. So you have to do a SSIS-Package  (here is a way you can do it [dynamic-cube-partitioning-in-ssas-2008](http://sql-bi-dev.blogspot.ch/2010/12/dynamic-cube-partitioning-in-ssas-2008.html)) or write a SQL Script which generates XMLA executables.


As shown in the Statement, you can dynamically generate month partitions. The trick is, to create a linked server, that you can execute XMLA statements with relational T-SQL, so i created a Linked Server first.


Thanks for any advice or improvements in the comment section:



| `  1
  2
  3
  4
  5
  6
  7
  8
  9
 10
 11
 12
 13
 14
 15
 16
 17
 18
 19
 20
 21
 22
 23
 24
 25
 26
 27
 28
 29
 30
 31
 32
 33
 34
 35
 36
 37
 38
 39
 40
 41
 42
 43
 44
 45
 46
 47
 48
 49
 50
 51
 52
 53
 54
 55
 56
 57
 58
 59
 60
 61
 62
 63
 64
 65
 66
 67
 68
 69
 70
 71
 72
 73
 74
 75
 76
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
` | `EXEC master.dbo.Sp_addlinkedserver
  @server = 'SSAS',
  @srvproduct = '',
  @provider = 'MSOLAP',
  @datasrc = '[DB-NAME]';

EXEC master.dbo.Sp_serveroption
  @server='SSAS',
  @optname='rpc out',
  @optvalue='true';

CREATE SCHEMA ssas;

CREATE PROCEDURE ssas.Usp_execute (@XMLA XML)
AS
    DECLARE @Command VARCHAR(max) = CONVERT(VARCHAR(max), @XMLA);

    EXEC (@Command) at ssas;

CREATE PROCEDURE ssas.Usp_processdatabase (@CubeName        NVARCHAR(50),
                                           @CubeID          NVARCHAR(50),
                                           @MeasureGroupID  NVARCHAR(50),
                                           @DataSourceID    NVARCHAR(50),
                                           @StartDT         DATETIME
                                           --'YYYY-MM-DD'
                                           ,
                                           @EndDT           DATETIME,
                                           @PartitionPreFix NVARCHAR(20),
                                           @SqlQuery        NVARCHAR(max) =''
/*'SELECT FK_AS_Produkt_ID, FK_AS_Produkt_productId_BK, FK_AS_Vertrag_ID, FK_AS_Vertrag_bookingId_BK, FK_AS_Inserent_ID, FK_AS_Inserent_accountId_BK, FK_AS_Objekt_ID, FK_AS_Objekt_vehicleId_BK,
FK_CD_Zeit_Zeit_ID, FK_CD_Zeit_Zeit_DIM_ZEIT_KEY_BK, [Datum Start], [Datum Ende], [Datum Start Booking], [Status ID], [Anzahl Plätze], [Anzahl verwendete Plätze], Preis, MwSt,
privateInserters_distict_cnt_PD, privateInsertersReturners1_distict_cnt, privateInsertersReturners12_distict_cnt, privateInsertersReturners48_distict_cnt, soldMemberSlotsFixdate_sum_PD,
privateInsertersMoto_sum_PD, vehiclesPrivatInsertersAuto_sum_PD, revenuePrivateInsertersListingsAuto_sum_PD, revenuePrivateInsertersAdditionalsAuto_sum_PD, vehiclesPrivatInsertersMoto_sum_PD,
revenuePrivateInsertersAdditionalsMoto_sum_PD, SA_SourceSystem_ID, SA_Load_ID, CA_Load_ID, DW_Load_ID, SCD_TransactionDate, DS_Load_ID
FROM DM.AS_BookingStats
WHERE FK_CD_Zeit_Zeit_ID BETWEEN <#=dateFrom#> AND <#=dateTo#>'*/
)
AS
    DECLARE @myXMLA        XML,
            @myXMLA_before XML,
            @myXMLA_delete XML
    DECLARE @value    NVARCHAR(30),
            @dateFrom VARCHAR(10),
            @dateTo   VARCHAR(10),
            @year     NVARCHAR(4)
    DECLARE @replSqlQuery NVARCHAR(max)

    SET @dateFrom=Format(Dateadd(month, Datediff(month, 0, @StartDT), 0),
                  'yyyyMMdd') --First day of month

    SELECT @value = @PartitionPreFix
                    + Format (@StartDT, 'yyyyMM') + '_before'

    SELECT @replSqlQuery = Replace(@SqlQuery,
           'WHERE FK_CD_Zeit_Zeit_ID BETWEEN <#=dateFrom#> AND <#=dateTo#>'
           , 'WHERE FK_CD_Zeit_Zeit_ID &lt; '
           + @dateFrom)

    --delete standard
    SET @myXMLA_delete = N'<Delete xmlns="http://schemas.microsoft.com/analysisservices/2003/engine"> <Object> <DatabaseID>' + @CubeName + '</DatabaseID> <CubeID>' + @CubeID
                         + '</CubeID> <MeasureGroupID>' + @MeasureGroupID
                         + '</MeasureGroupID> <PartitionID>' + @MeasureGroupID + '</PartitionID> </Object> </Delete>'

    PRINT CONVERT(NVARCHAR(max), @myXMLA_delete)

    EXEC ssas.Usp_execute
      @myXMLA_delete;

    PRINT ' '

    --delete first partition before
    SET @myXMLA_delete = N'<Delete xmlns="http://schemas.microsoft.com/analysisservices/2003/engine"> <Object> <DatabaseID>' + @CubeName + '</DatabaseID> <CubeID>' + @CubeID
                         + '</CubeID> <MeasureGroupID>' + @MeasureGroupID
                         + '</MeasureGroupID> <PartitionID>' + @value + '</PartitionID> </Object> </Delete>'

    PRINT CONVERT(NVARCHAR(max), @myXMLA_delete)

    EXEC ssas.Usp_execute
      @myXMLA_delete;

    PRINT ' '

    SET @myXMLA =N'<Create xmlns="http://schemas.microsoft.com/analysisservices/2003/engine"> <ParentObject> <DatabaseID>' + @CubeName + '</DatabaseID> <CubeID>' + @CubeID
                 + '</CubeID> <MeasureGroupID>' + @MeasureGroupID + '</MeasureGroupID> </ParentObject> <ObjectDefinition> <Partition xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ddl2="http://schemas.microsoft.com/analysisservices/2003/engine/2" xmlns:ddl2_2="http://schemas.microsoft.com/analysisservices/2003/engine/2/2" xmlns:ddl100_100="http://schemas.microsoft.com/analysisservices/2008/engine/100/100" xmlns:ddl200="http://schemas.microsoft.com/analysisservices/2010/engine/200" xmlns:ddl200_200="http://schemas.microsoft.com/analysisservices/2010/engine/200/200" xmlns:ddl300="http://schemas.microsoft.com/analysisservices/2011/engine/300" xmlns:ddl300_300="http://schemas.microsoft.com/analysisservices/2011/engine/300/300" xmlns:ddl400="http://schemas.microsoft.com/analysisservices/2012/engine/400" xmlns:ddl400_400="http://schemas.microsoft.com/analysisservices/2012/engine/400/400"> <ID>'
                 + @value + '</ID> <Name>' + @value + '</Name> <Source xsi:type="QueryBinding"> <DataSourceID>'
                 + @DataSourceID + '</DataSourceID> <QueryDefinition> ' + @replSqlQuery + ' </QueryDefinition> </Source> <StorageMode>Molap</StorageMode> <ProcessingMode>Regular</ProcessingMode> <ProactiveCaching> <SilenceInterval>-PT1S</SilenceInterval> <Latency>-PT1S</Latency> <SilenceOverrideInterval>-PT1S</SilenceOverrideInterval> <ForceRebuildInterval>-PT1S</ForceRebuildInterval> <Source xsi:type="ProactiveCachingInheritedBinding" /> </ProactiveCaching> </Partition> </ObjectDefinition> </Create>'

    PRINT CONVERT(NVARCHAR(max), @myXMLA)

    EXEC ssas.Usp_execute
      @myXMLA;

    PRINT ' '

    WHILE @StartDT < @EndDT
      BEGIN
          SET @dateFrom=Format(Dateadd(month, Datediff(month, 0, @StartDT), 0),
                        'yyyyMMdd') --First day of month
          SET @dateTo =Format(Dateadd(month, Datediff(month, -1, @StartDT), -1),
                       'yyyyMMdd') --Last Day of month

          SELECT @value = @PartitionPreFix
                          + Format (@StartDT, 'yyyyMM')

          SELECT @replSqlQuery = Replace(Replace(@SqlQuery, '<#=dateTo#>',
                                         @dateTo),
                                        '<#=dateFrom#>', @dateFrom)

          SET @myXMLA_delete = N'<Delete xmlns="http://schemas.microsoft.com/analysisservices/2003/engine"> <Object> <DatabaseID>' + @CubeName + '</DatabaseID> <CubeID>' + @CubeID
                               + '</CubeID> <MeasureGroupID>' + @MeasureGroupID
                               + '</MeasureGroupID> <PartitionID>' + @value + '</PartitionID> </Object> </Delete>'

          PRINT CONVERT(NVARCHAR(max), @myXMLA_delete)

          EXEC ssas.Usp_execute
            @myXMLA_delete;

          PRINT ' '

          SET @myXMLA =N'<Create xmlns="http://schemas.microsoft.com/analysisservices/2003/engine"> <ParentObject> <DatabaseID>' + @CubeName + '</DatabaseID> <CubeID>' + @CubeID
                       + '</CubeID> <MeasureGroupID>' + @MeasureGroupID + '</MeasureGroupID> </ParentObject> <ObjectDefinition> <Partition xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ddl2="http://schemas.microsoft.com/analysisservices/2003/engine/2" xmlns:ddl2_2="http://schemas.microsoft.com/analysisservices/2003/engine/2/2" xmlns:ddl100_100="http://schemas.microsoft.com/analysisservices/2008/engine/100/100" xmlns:ddl200="http://schemas.microsoft.com/analysisservices/2010/engine/200" xmlns:ddl200_200="http://schemas.microsoft.com/analysisservices/2010/engine/200/200" xmlns:ddl300="http://schemas.microsoft.com/analysisservices/2011/engine/300" xmlns:ddl300_300="http://schemas.microsoft.com/analysisservices/2011/engine/300/300" xmlns:ddl400="http://schemas.microsoft.com/analysisservices/2012/engine/400" xmlns:ddl400_400="http://schemas.microsoft.com/analysisservices/2012/engine/400/400"> <ID>'
                       + @value + '</ID> <Name>' + @value + '</Name> <Source xsi:type="QueryBinding"> <DataSourceID>'
                       + @DataSourceID + '</DataSourceID> <QueryDefinition> ' + @replSqlQuery + ' </QueryDefinition> </Source> <StorageMode>Molap</StorageMode> <ProcessingMode>Regular</ProcessingMode> <ProactiveCaching> <SilenceInterval>-PT1S</SilenceInterval> <Latency>-PT1S</Latency> <SilenceOverrideInterval>-PT1S</SilenceOverrideInterval> <ForceRebuildInterval>-PT1S</ForceRebuildInterval> <Source xsi:type="ProactiveCachingInheritedBinding" /> </ProactiveCaching> </Partition> </ObjectDefinition> </Create>'

          PRINT CONVERT(NVARCHAR(max), @myXMLA)

          EXEC ssas.Usp_execute
            @myXMLA;

          PRINT ' '

          SET @StartDT = Dateadd(month, 1, @StartDT)
      END

go
` |


[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/ssas-cubes-dynamic-generation-of-partition/)
|
[Pay what you like](https://ko-fi.com/sspaeti)
|
[Cube](https://www.ssp.sh/tags/cube/)
[Microsoft](https://www.ssp.sh/tags/microsoft/)
[Partitioning](https://www.ssp.sh/tags/partitioning/)
[SSAS](https://www.ssp.sh/tags/ssas/)
