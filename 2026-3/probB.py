total = int(input())
year = total // 365
month = total % 365 // 30
day = total % 365 % 30 
print(f"{year} ano(s)")
print(f"{month} mes(es)")
print(f"{day} dia(s)")

