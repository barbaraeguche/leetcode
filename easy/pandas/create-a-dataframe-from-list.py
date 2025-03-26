# name: 2877. create a dataframe from list
# link: https://leetcode.com/problems/create-a-dataframe-from-list

# solution #
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
	return pd.DataFrame(student_data, columns=["student_id", "age"])