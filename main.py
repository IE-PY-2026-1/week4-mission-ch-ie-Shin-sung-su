# 파일이름 : 나만의 맛집 버킷리스트
# 작 성 자 : 60231805 신성수
bucket_list = []
bucket_list.append(input("첫 번째 맛집을 입력: "))
bucket_list.append(input("두 번째 맛집을 입력: "))
bucket_list.append(input("세 번째 맛집을 입력: "))

print(f"리스트: {bucket_list}")

add_place = input("\n1순위 VIP 맛집 추가: ")
bucket_list.insert(0, add_place)
print(f"리스트: {bucket_list}")

remove_place = input("\n오늘 방문한 맛집: ")
bucket_list.remove(remove_place)
print(f"리스트: {bucket_list}")

