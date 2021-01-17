# 알파벳 대소문자로 된 문자열이 주어지면,
# 이 문자열에서 가장 많이 사용된 알파벳이
# 무엇인지 출력하는 프로그램을 작성하시오.
# 단, 대소문자는 구별하지 않아요. 만약 동률이 존재하는 경우
# 알파벳 순으로 제일 앞에 있는
# 문자를 출력하세요.

# 문자열) "This is a sample Program mississippi river"
# 문자열) "abcdabcdababccddcd"

# 방법1
# str1 = 'This is a sample Program mississippi river'
# str2 = 'abcdabcdababccddcd'

str = list(input().lower().replace(' ', ''))
unique_str = list(set(str)) # 중복문자제거
print(unique_str)

cnt_list = [] # 알파벳 빈도수 저장용도
for x in unique_str:
    cnt = str.count(x)
    cnt_list.append(cnt)  # count 숫자를 리스트에 append
print(cnt_list)

max_cnt = max(cnt_list) # 최대빈도 개수
max_idx = cnt_list.index(max_cnt) # count 숫자 최대값 인덱스(위치)
print(max_idx)
print(unique_str[max_idx]) # i

# 심화 (?)
if cnt_list.count(max_cnt) > 1:  # max_cnt값이 중복되면
    print(cnt_list.count(max_cnt))
    pass # list[최대값]들을 set으로 돌려주면 됨
else:
    print(unique_str[max_idx])

# 방법2
import collections
str1 = 'This is a sample Program mississippi river'
print(collections.Counter(str1).most_common(1)[0][0]) # i

str2 = 'abcdabcdababccddcd'
print(collections.Counter(str2).most_common(1)[0][0]) # c