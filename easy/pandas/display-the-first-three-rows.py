# name: 2879. display the first three rows
# link: https://leetcode.com/problems/display-the-first-three-rows

# solution #
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
	return employees.iloc[:3]
