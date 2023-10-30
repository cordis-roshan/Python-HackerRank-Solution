N = int(input())
countries = []
for i in range(N):
    country = input()
    countries.append(country)

dist_countries = set(countries)
print(len(dist_countries))