#  The following program uses variable and expressions to perform  a compound interest
principal = 1000 # initial amount
rate = 0.05
num_years = 5
year = 1
while year < num_years:
  principal = principal * (1 + rate)
  print(year, principal)
  year += 1
# To make the outcome very pretty can use f-strings like this
principal = 1000 # initial amount
rate = 0.05
num_years = 5
year = 1
while year < num_years:
  principal = principal * (1 + rate)
  print(f"{year:>3d} {principal:0.2f}" )
  year += 1
