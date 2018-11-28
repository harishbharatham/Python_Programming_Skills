m = eval(input('Enter the number of minutes:'))
years = m//525600
days = m%525600
days = days//1440
print(m,'minutes is approximately',years,'years and',days,'days')