import pandas as pd
import argparse
import string


## 	function pivots dataframe to return the path as columns 
## 		df: dataframe
##
def path_to_columns(df):
	return df.pivot(index='user_id', columns= 'path', values='length').fillna(0)

def aggregate_df(df):
	return df.groupby(['user_id', 'path'],as_index = False)['length'].sum()


## 	function downloads a csv for every letter of the alphabet within a range and aggregates into a single 
##	dataframe. 
## 		df: dataframe to aggregate into (start with None)
##		baseurl: base url where csv files can be found
## 		charindex begining character 
##		limit: number of characters to check files for
##
def df_append_and_sum(df, baseurl, charindex, limit):

	## end recursion
	if charindex >= limit:
		return df


	file = f'{baseurl}{list(string.ascii_lowercase)[charindex]}.csv'
	print(f'Processing file: {file}')

	# catching exceptions and moving on to the next file
	try:
		# get data and sum length feilds per user, path
		c = aggregate_df(pd.read_csv(file))

		# add aggreated data and resum counts
		df = aggregate_df(pd.concat([df, c]))
	except: 
		print(f'Failed to process {file}!')

	return df_append_and_sum(df, baseurl, charindex +1, limit)


##	function gets and builds transformed dataset based on url
##		baseurl: url directory to download a-z files from
##
def get_and_transform(baseurl):

	df = df_append_and_sum(None, baseurl, 0, 26)
	
	return df.pivot(index='user_id', columns= 'path', values='length').fillna(0)


def run(baseurl, outputfile):
	get_and_transform(baseurl).to_csv(outputfile)


## main cli function
##
def main():
    parser = argparse.ArgumentParser(
        description="Aggregate and pivot traffic data files found at X base url.")
    parser.add_argument("baseurl", type=str, help="Base URL or directory location of files to download: http://test.com/dir/")
    parser.add_argument("outputfile", type=str, help="Output file for formatted csv ")

    args = parser.parse_args()

    run(args.baseurl, args.outputfile)
  
if __name__ == "__main__":
    main()
