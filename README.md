## 인스타그램 피드 글 크롤링

- 프로젝트를 위해서 인스타그램 피드 글을 크롤링하는 코드가 필요했다.
- 인스타그램에서 제공하는 API가 없고, 인스타그램에서는 원칙적으로 크롤링을 막는다.
- 따라서, 인스타그램 크롤링을 연습하는 레포지토리이다.

다음의 자료들을 참고하였다.
- https://m.blog.naver.com/badzoo/222298378145
- https://gmwoo.tistory.com/93

방식은 다음과 같다.
- `authentication-free.py`
  - 로그인을 하지 않은 채로 크롤링을 하는 것이다. 로그인을 하지 않았기 때문에 전체의 본문이 아닌 축약된 부분만 크롤링되는 문제가 발생하였다.
- `authentication-required.py`
  - Selenium과 BeautifulSoup 라이브러리를 이용하여 인스타그램에 로그인하고 특정 게시물의 피드를 가져온다. 
  - Selenium을 사용하여 웹 브라우저를 자동으로 제어합니다. 이를 통해 인스타그램에 접속하고 로그인한다.
  - 그 다음, 특정 게시물의 URL로 이동하여 해당 페이지의 HTML 소스코드를 가져온다.
  - BeautifulSoup을 사용하여 HTML을 파싱하고, 특정 CSS 클래스를 가진 요소를 가져온다.