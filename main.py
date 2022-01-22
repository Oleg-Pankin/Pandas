import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Games.csv')
df.plot(y = 'Sales', kind='bar')