# PPT Translator Web Service

로컬에 있는 PPT 파일을 업로드하면 선택한 언어(한국어/영어/폴란드어)로 텍스트를 번역해주는 개인용 웹서비스입니다. MCP 멀티 에이전트 리뷰 루프를 최소 5회 실행하여 품질 점검 로그를 제공합니다.

## 기능
- PPTX 파일 업로드 후 번역 파일 다운로드
- 한국어/영어/폴란드어 지원
- MCP 멀티 에이전트 리뷰 로그(5회 이상 반복)

## 로컬 실행

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload
```

브라우저에서 `http://localhost:8000` 접속 후 사용합니다.

## Render 배포

`render.yaml` 을 사용해 Web Service로 배포할 수 있습니다.

```bash
render services create --from render.yaml
```
