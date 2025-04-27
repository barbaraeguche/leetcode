# name: 2878. get the size of a dataframe
# link: https://leetcode.com/problems/get-the-size-of-a-dataframe

# solution #
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
	return list(players.shape)
