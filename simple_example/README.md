# 🛠️ uv 기반 Python 프로젝트 환경 설정 (PowerShell)

이 문서는 PowerShell 환경에서 [uv](https://github.com/astral-sh/uv)를 사용하여 Python 프로젝트를 설정하는 전체 과정을 설명합니다.

---

```powershell
# uv 설치
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# 프로젝트 생성 및 이동
uv init helloworld
cd helloworld

# 가상환경 생성 및 활성화
uv venv
.venv\Scripts\activate

# ⚠️ 에러 발생 시 아래 명령어를 먼저 실행 후 재시도
# Set-ExecutionPolicy Bypass -Scope Process -Force

# 의존성 패키지 설치
uv add mcp[cli] httpx

# 초기 Python 파일 생성
new-item helloworld.py
```
---
✅ 완료 안내
helloworld 디렉토리에 다음이 설정됩니다:
1. uv를 통한 프로젝트 초기화
2. .venv 가상환경 생성 및 활성화
3. mcp[cli], httpx 패키지 설치
4. helloworld.py 파일 생성

이제 helloworld.py를 열고 시작하시면 됩니다! 🚀
