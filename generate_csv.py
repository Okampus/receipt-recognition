import pandas as pd
import numpy as np
from test_all_regex import test_regex

# Read the data
data = pd.read_csv("false.csv")

dates = []
totals = []
for i in range(len(data)):
    text = data["text"][i]

    date, total = test_regex(text)
    dates.append(date)
    totals.append(total)

data["new_date"] = dates
data["new_total"] = totals

data.to_csv("test.csv")
data.head(20)
