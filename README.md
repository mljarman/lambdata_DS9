# lambdata_mljarman
a collection of data science helper functions.

The dt_utils file provides useful functions for cleaning up dataframes:
* in particular a function that will split a datetime values into new columns that contain the day, month, and year of the original column.

The for_models file uses the Model_Prep class to prepare dataframes for running
predictive models.
* in particular includes a method that will split a dataframe into train set that defaults to:
	* train set with 60% of the data
	* val set with 20% of the data
	* test set with 20% of the data

My intent for this package is to add more to it which will make exploratory data analysis and running models streamlined and efficient. 
