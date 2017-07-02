import pandas as pd
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

# CSV query
# df = pd.read_csv(os.path.join( dir_path, 'AirPassengers.csv'))
df = pd.read_csv('AirPassengers.csv')
print(df['AirPassengers'])
print(df['time'][135])

# CSV creation
names = ['Wade', 'James', 'Kobe', 'Curry']
total = [55, 50, 44, 36]
data_set = list(zip(names, total))
data_frame = pd.DataFrame(data = data_set, columns = ['Names', 'Total'])
data_frame.to_csv('Points.csv', index = True, header = True)