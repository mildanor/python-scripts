#WORKFLOW BASED COMMANDS

#read csv & store in variable
new_data = pd.read_csv('Rein_filters.csv', delimiter = ',')

#data types inside a dataframe
new_data.dtypes

#Convert column(s) to string
new_data[["Geography"]] = new_data[["Geography"]].astype(str) 
new_data[["CcompanyName"]] = new_data[["companyName"]].astype(str)
new_data[["Orgs"]] = new_data[["Orgs"]].astype(str)
new_data[["Sector"]] = new_data[["Sector"]].astype(str)
new_data[["Themes"]] = new_data[["Themes"]].astype(str)

#Splitting stuff inside cell https://stackoverflow.com/questions/12680754/split-explode-pandas-dataframe-string-entry-to-separate-rows
companyName_contentType = pd.concat([Series(row['companyName'], row['ContentType'].split(','))              
    for _, row in new_data.iterrows()]).reset_index()

companyName_geo = pd.concat([Series(row['companyName'], row['Geography'].split(','))              
    for _, row in new_data.iterrows()]).reset_index()

companyName_orgs = pd.concat([Series(row['companyName'], row['Orgs'].split(','))              
    for _, row in new_data.iterrows()]).reset_index()

cName_sector = pd.concat([Series(row['companyName'], row['Sector'].split(','))              
    for _, row in new_data.iterrows()]).reset_index()

cName_themes = pd.concat([Series(row['companyName'], row['Themes'].split(','))              
    for _, row in new_data.iterrows()]).reset_index()


#rename columns 
companyName_geo.columns = ['geography', 'company']
df.head()

#filtering for strings
#companyName_contentType[companyName_contentType['company'].str.contains('CITIZENS FINANCIAL GROUP')]
stateTrustCompany = cName_themes[cName_themes['company'].str.contains('State Street Bank and Trust Company')]
scotia = cName_themes[cName_themes['company'].str.contains('Scotiabank')]
stateTrust = cName_themes[cName_themes['company'].str.contains('State Street Bank and Trust')]
EY = cName_themes[cName_themes['company'].str.contains('Ernst & Young LLP')]
#companyName_contentType[companyName_contentType['company'].str.contains('Citco London Ltd')]
BNY = cName_themes[cName_themes['company'].str.contains('BNY Mellon')]
#stateTrustCompany_content_type = companyName_contentType[companyName_contentType['company'].str.contains('State Street Bank and Trust Company')]

#Frequency
stateTrust['content_type'].value_counts()
new_data['companyName'].value_counts()
EY.groupby(['content_type']).content_type.value_counts().nlargest(35)

#top 10 exmaple
df.groupby(['Borough', 'Neighborhood']).Neighborhood.value_counts().nlargest(5)

#what I ran for top 35 content types for all companies
companyName_contentType.groupby(['content_type']).content_type.value_counts().nlargest(35)

##SAVING

#save output as dataframe
contentType_count_frame = pd.DataFrame(contentType_count)
#save into csv
contentType_count_frame.to_csv('contentype.csv')