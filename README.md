# song-pipeline
음악 api 데이터 적재, 카테고리/키워드 별 처리 및 추천 시스템을 airlow 파이프라인 workflow로 구현.

<img width="848" alt="스크린샷 2023-06-07 오후 4 04 18" src="https://github.com/CatJerry/eco-pipeline/assets/79153994/ad2e429a-4a1b-45d0-b7f3-b5d1c3327315">

* api_data: Spotify api에서 음악 데이터 호출
* load_data: 호출한 데이터 RDB에 적재
* trans_data_category/keyword: 음악장르에 따라 카테고리 구분, 지표에 따라 키워드 설정
* load_trans_data: 키워드와 카테고리 분류한 데이터 적재
* service_start: 사용자가 서비스 이용
* user_emotion: 사용자의 기분 키워드 선택(밝은/슬픈/정적인 등)
* user_time: 출.퇴근 시간 또는 주말에 따른 키워드 분석
* apply_user: 결과 데이터 사용자에게 전송
* visualize: 전송된 데이터 시각화(or 재생)
