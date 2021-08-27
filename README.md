# 리드미 연습

## 글자크기

## 소스코드 작성법
```j
public class CharacterEncodingFilter implements Filter {

	@Override
	public void doFilter(ServletRequest req, 
			ServletResponse resp, FilterChain fc)
			throws IOException, ServletException {
		// TODO Auto-generated method stub
		
		req.setCharacterEncoding("UTF-8");
		fc.doFilter(req,resp);
		System.out.println("after filter");
	}

}
```

## 링크 작성법

[링크](https://github.com/nsy5687/codingteststudy/new/master?readme=1)

순서없는 목록 작성법

* ㅇㄴㅇㄹ
  * ㅇㄴㅇㄹ
  
## 인용 구문

> ㄴㅇㄹㄷ

##테이블 작성

수학|영어|국어|과학
---|---|---|---|
90|100|70|50|

## 강조

**치킨**
~~피자~~

## 사진

![background](https://user-images.githubusercontent.com/78149097/131092143-05eefee4-e22c-4cc4-a46b-c86a23db2580.jpg)
