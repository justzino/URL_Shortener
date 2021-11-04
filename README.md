# URL Shortener

### [사이트 링크](https://originalll.pythonanywhere.com/)


## 요구 사항

**① 주제: URL Shortener** (Algorithm, Performance)

**② SPEC:**

- 웹 페이지 입력폼에 URL 입력 시 단축된 결과 출력
- 브라우저의 주소창에 단축 URL 입력 시 기존 URL로 리다이렉트
- 같은 URL 입력 시 동일한 결과값 도출
- 결과값은 주소를 제외하고 8글자 이내로 생성

## 조건 정리
1. 같은 URL 입력시 동일한 결과값이 나와야함. 즉, 그때마다 새로 발급할 수 없음  
2. 주소에 들어가는 문자 추리기: BASE62 로 사용  
   - 이유: BASE64 에는 '+', '/' 가 포함되기 때문에 제외하고 사용.
   - `BASE62 = ascii_letters + digits` 로 생성 가능

## url shortening 구현 방법 고민
1. Hash 기반의 알고리즘  
   → 8자리 미만으로 hash 충돌이 일어나지 않음을 보장해야함.  
2. BASE62로 주소 Encoding  
   → 길이가 너무 길어짐.
3. original_url : short_url 로 저장.
   1. key-value 형태의 db 사용
   2. 일반 RDBMS 사용 ✅

> 선택: 일반 RDBMS에 id, original_url, short_url 형태로 저장.

## 아키텍처
- MTV (MVC) 아키텍처 사용
- API Server 와 Client Server 를 나누기에는 너무 작은 규모.

## 과정
1. form 에 사용자가 original_url 입력 (POST 요청)
2. form 을 통해 넘어온 original_url 유효성 검사
3. original_url 에 대한 중복성 검사
4. 전부 통과하면, model 을 통해 save()
5. save method 동작시 short_url 생성 후 저장  
   < short_url 생성 과정 >
   1. `make_short_url(self)` 호출 → 중복되지 않는 short_path 리턴
   2. `make_random_path()` 호출 → short_path 로 사용할 random_path 리턴
6. short_url 저장
7. GET {도메인}/{short_url} 요청시 redirect_view 로 redirect
   1. 해당 short_url 이 저장되어 있으면
      1. `URLMap.objects.get(short_url=short_path)`으로 object 받아옴
      2. 받아온 object.original_url 로 redirect 시킴
   2. URLMap.DoesNotExist 발생시
      1. raise exception
      2. error code: 404, error message: '유효하지 않은 url 입니다.'

## 배포
1. AWS EC2 - 클라우드 사용하기엔 너무 작은 규모의 프로젝트.
2. pythonanywhere

임시로 pythonanywhere 를 사용하여 배포하였습니다.

