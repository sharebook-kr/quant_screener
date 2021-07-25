from pykrx import stock 

date = "20210415"
df = stock.get_market_fundamental_by_ticker(date=date, market="ALL")

# 1. PER filtering
# 2.5 <= PER <= 10
cond = (df['PER'] >= 2.5) & (df['PER'] <= 10)
df2 = df[cond].copy()

# 2. sort by PBR 
df2.sort_values(by="PBR", inplace=True)

# portfolio
portfolio = df2.iloc[:30].index
for code in portfolio:
    print(code)