# llm-bot
LLM chat bot to use CrewAI


## 1. 프로젝트 세팅
- VSC
- Github 연동

## 2. 프로제트 구성
- 가상환경을 설정 => Docker Container 개념 (공간을 분리해서 따로 관리하겠다.)
- Python 3.8 
    => 3.8 함수를 썼다면 3.3에는 없는 함수 => 오류 =>
    => 로컬에서 작업하는 환경과 호스트 서버에서 작업하는 환경을 일치시켜 주기 위함
    => Docker(Virtual Machine) // venv 모듈을 사용해서 환경 설정을 해주도록 하겠습니다.

- python3.10 -m venv .venv
.venv/Scripts/activate

## 3. 프로젝트

(1) ollama 다운로드
(2) ollama를 통해서 llm 다운로드

> ollama pull llama3.1
> ollama run llama3.1

> ollama pull phi3:3.8b
> ollama run phi3:3.8b

(3) CrewAI 설치
- 언어 모델의 API 관리를 편리하게 도와주는 라이브러리
- 모델 - 클로드, 잼민, GPT3.5, ... => import OpenAI // 언어마다 SDK를 다운받아줘야해요.
- LangChain 안하고 왜 CrewAI 하나요? => 가벼워서요. (러닝 커브가 낮아서)

=> RestAPI (기술 명세)
=> 쇼핑몰이 어디까지 있으신가요?
=> 우리 챗봇은 여러분이 만드신 REST API를 기반으로 동작할 거니깐.

> pip install crewai crewai-tools


### 3-1. Ollama 모델 + CrewAI


### 3-2. Flask 사용해서 기본적인 챗봏