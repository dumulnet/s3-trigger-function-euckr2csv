# s3-trigger-function-euckr2csv
소스 버킷에 데이터가 업로드될 경우 S3 트리거를 통해 EUC-KR 인코딩된 CSV 파일을 UTF-8로 변환합니다.

### 주의사항
- Lambda 실행 역할에 버킷 권한을 설정합니다.
- 5 MB 이상의 대용량 파일은 반드시 Put 이벤트와 함께 CompleteMultipartUpload 이벤트를 추가로 선택합니다.
- Lambda 함수의 메모리, 로컬 스토리지 용량, 타임아웃 시간을 여유있게 설정합니다.
