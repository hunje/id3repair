# 깨진 ID3 Tag 고치기
## 개요
주로 윈도에서만 테스트를 거친 MP3의 태그들이 OSX로 넘어와서 iTunes에서 열만 한글이 깨지는 경우가 발생한다. 이 것은 주로 ID3v2.3 이하 버전에서 생성된 태그로 한글 인코딩이 euc-kr이기 때문이다. 

ID3 Tag는 언어 인코딩에 대한 정보가 없기 때문에 현재 인코딩이 무엇인지는 순전히 OS의 현재 로케일에 의존한다. 따라서 영문 혹은 기타 언어 상위의 OSX에서 euc-kr로 인코딩한 ID3태그를 로드하면 깨질 수 밖에. 

## 해결 방법
간단히 euc-kr로 입력된 태그를 euc-kr로 디코딩하여서 다시 utf-8로 인코딩하여 저장한다. python코드라면

```
broken_word = af.tag.title
af.tag.title = broken_word.encode('latin-1').decode('euc-kr')
```
