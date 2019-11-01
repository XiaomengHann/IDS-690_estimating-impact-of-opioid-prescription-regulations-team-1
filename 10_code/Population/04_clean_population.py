print(pop_2000_2018.columns)

pop_2000_2018['STATE_x'] = pop_2000_2018['STATE_x'].astype(str).str.zfill(2)
pop_2000_2018['COUNTY_x'] = pop_2000_2018['COUNTY_x'].astype(str).str.zfill(3)
pop_2000_2018['FIPS'] = pop_2000_2018['STATE_x'].map(str) + pop_2000_2018['COUNTY_x'].map(str)

# drop unrelated data and rename variables
pop_2000_2018 = pop_2000_2018.drop(["STATE_x","COUNTY_x", "STATE_y", "COUNTY_y","STNAME_y", "CTYNAME_y"], axis = 1)
pop_2000_2018 = pop_2000_2018.rename({'STNAME_x':'STNAME', 'CTYNAME_x':'CTYNAME'}, axis = 'columns')

pop_2000_2018 = pop_2000_2018[[ 'FIPS', 'STNAME', 'CTYNAME', 'ESTIMATESBASE2000', 'POPESTIMATE2000',
       'POPESTIMATE2001', 'POPESTIMATE2002', 'POPESTIMATE2003',
       'POPESTIMATE2004', 'POPESTIMATE2005', 'POPESTIMATE2006',
       'POPESTIMATE2007', 'POPESTIMATE2008', 'POPESTIMATE2009',
       'CENSUS2010POP_x', 'POPESTIMATE2010_x', 'CENSUS2010POP_y',
       'ESTIMATESBASE2010', 'POPESTIMATE2010_y', 'POPESTIMATE2011',
       'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014',
       'POPESTIMATE2015', 'POPESTIMATE2016', 'POPESTIMATE2017',
       'POPESTIMATE2018']]

# We only use data from 2003 to 2015.
pop_2003_2015 = pop_2000_2018.drop(["POPESTIMATE2000","POPESTIMATE2001", "POPESTIMATE2002", 'CENSUS2010POP_y','POPESTIMATE2010_x', 'POPESTIMATE2010_y',"POPESTIMATE2016",'POPESTIMATE2017',
       'POPESTIMATE2018'], axis = 1)
pop_2003_2015 = pop_2003_2015.rename(columns = {'CENSUS2010POP_x':'CENSUS2010'})

# Save dataframe as csv file
pop_2000_2018.to_csv(outpath + 'population_2000_2018.csv')
pop_2003_2015.to_csv(outpath + 'population_2003_2015.csv')
