import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/Git2025Pot/experiment-3/refs/heads/main/Exp_3_1.csv");
# print(df);
df.drop(['name'],axis=1,inplace=True);
ohed = pd.get_dummies(df,columns=['Comp_Name','insu_status']);

print(ohed);
plt.scatter(df["age"],df["insu_status"]);
plt.show()