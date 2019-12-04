import pandas as pd
filename = r"C:\Users\MOHNISH\AppData\Roaming\Microsoft\Windows\Network Shortcuts\NIIT\trial.csv"
df = pd.read_csv(filename)
print(df['temperature'])
