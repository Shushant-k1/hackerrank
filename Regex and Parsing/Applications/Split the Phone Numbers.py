import re
pattern = r'(\d+)'
for i in range(int(input())):
    ans = re.findall(pattern, input())
    print('CountryCode='+str(ans[0])+',LocalAreaCode='+str(ans[1])+',Number='+str(ans[2]))
