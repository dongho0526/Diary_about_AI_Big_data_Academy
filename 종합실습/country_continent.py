import pandas as pd

df = pd.read_csv('Car.csv')


# 이름에서 브랜드만 따로 추출
df['Name'] = df['Name'].apply(lambda x: 'Land-Rover' if 'Land Rover' in x else x)
df['Brand'] = df['Name'][:].str.split(' ').str[0]

split_names = df['Name'].str.split(' ')
joined_brands = split_names.apply(lambda x: ' '.join(x[1:]))
df['Name'] = joined_brands


# 브랜드가 속한 나라 별로 딕셔너리 형성
brands = {
    'India': ['Maruti', 'Tata', 'Land-Rover', 'Mahindra', 'Ambassador', 'Force', 'Hindustan'],
    'Japan': ['Honda', 'Toyota', 'Mitsubishi', 'ISUZU', 'Nissan', 'Datsun'],
    'Korea': ['Hyundai'],
    'Germany': ['Volkswagen', 'Mercedes-Benz', 'BMW', 'Porsche', 'Audi', 'Skoda', 'Mini', 'Smart', 'OpelCorsa'],
    'France': ['Renault'],
    'USA': ['Ford', 'Chevrolet', 'Jeep'],
    'UK': ['Jaguar', 'Bentley'],
    'Sweden': ['Volvo'],
    'Italy': ['Fiat', 'Lamborghini']
}

# 새로운 파생 변수 Country 생성 - 모든 데이터들에 결측치 없이 값이 지정됨
brand_country = {brand: country for country, brands_list in brands.items() for brand in brands_list}

df['Country'] = df['Brand'].map(brand_country)


# 나라가 속한 대륙 별로 딕셔너리 형성
continents = {
    'Europe' : ['Germany', 'France', 'Sweden', 'Italy', 'UK'],
    'Asia' : ['Korea', 'Japan', 'India'],
    'America' : ['USA']
}


# 새로운 파생 변수 Continent 생성 - 모든 데이터들에 결측치 없이 값이 지정됨
brand_continent = {}
for continent, countries in continents.items():
    for country in countries:
        brand_continent[country] = continent

# 대륙 정보 기반으로 새로운 열 추가
df['Continent'] = df['Country'].map(brand_continent)

# 결과 확인
df
