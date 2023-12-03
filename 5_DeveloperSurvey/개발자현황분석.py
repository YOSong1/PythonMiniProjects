# 판다스 라이브러리 탑재
import pandas as pd

# CSV 파일 읽어오기
raw_data = pd.read_csv("survey_results_public.csv")

# 데이터 확인하기
print(raw_data.info())
# 일부 데이터 확안하기
raw_data.head()
# 필요한 열 추출
revised_data = raw_data[["Age", "Country", "LanguageHaveWorkedWith", "LearnCode"]]

# 일부 값 확인
revised_data.head()
# 연령대 확인하기
revised_data["Age"]
# 중복 값 삭제하기
revised_data["Age"].drop_duplicates()
# 연령대 데이터 그룹화하기
revised_data.groupby(["Age"])
# 연령대 그룹별 크기 확인하기
size_by_age = revised_data.groupby(["Age"]).size()
size_by_age
# 국가 그룹별 크기 확인하기
size_by_country = revised_data.groupby(["Country"]).size()
size_by_country
# 선 그래프 그리기
size_by_age.plot.line(rot=45)
# 수직 막대그래프 그리기
size_by_age.plot.bar()
# 수평 막대그래프 그리기
size_by_age.plot.barh()
# 현재 색인 확인하기
size_by_age.index
# 재색인하기
reindxed_size_by_age = size_by_age.reindex(index=[
    'Prefer not to say',
    '65 years or older',
    '55-64 years old',         
    '45-54 years old', 
    '35-44 years old',
    '25-34 years old', 
    '18-24 years old', 
    'Under 18 years old' 
    ])

# 재색인한 결과 확인하기
reindxed_size_by_age
# 수평 그래프 다시 그리기
reindxed_size_by_age.plot.barh()
# 기본 파이 그래프 그리기
size_by_country.plot.pie()
# 파이 그래프 크기 조정하기
size_by_country.plot.pie(figsize=(10, 10))
# 국가 상위 20개 확인하기
size_by_country.nlargest(20)
# 국가 상위 20개 파이 그래프 그리기
size_by_country.nlargest(20).plot.pie(figsize=(10, 10))
# 프로그래밍 언어 데이터 추출
languages = revised_data["LanguageHaveWorkedWith"]

# 데이터 확인
languages
# 데이터 문자열 변환 후 구분자(;)로 구분
languages = languages.str.split(";")

# 데이터 확인
languages
# 리스트 항목을 행으로 나누기
exploded_languages = languages.explode()

# 데이터 확인
exploded_languages
# 프로그래밍 별 응답 수 구하기
size_by_languages = exploded_languages.groupby(exploded_languages).size()

# 데이터 확인
size_by_languages
# 파이 그래프 그리기
size_by_languages.nlargest(10).plot.pie(figsize=(10, 10))
# 백분율 표기하기
size_by_languages.nlargest(10).plot.pie(figsize=(10, 10), autopct='%1.1f%%')
# 25~34세 연령대가 사용한 프로그래밍 언어 정보 추출
languages_for_25_34 = revised_data[revised_data.Age == '25-34 years old']["LanguageHaveWorkedWith"].str.split(";").explode()

# 데이터 확인
languages_for_25_34
# 상위 10개 데이터 파이 그래프 그리기
languages_for_25_34.groupby(languages_for_25_34).size().nlargest(10).plot.pie(figsize=(10, 10), autopct='%1.0f%%')