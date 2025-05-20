from mcp.server.fastmcp import FastMCP, Context
import json

# MCP 서버 초기화
mcp = FastMCP("custom")

# 리소스: 지역-좌표 매핑
@mcp.resource("custom://location_coords")
def load_location_coords():
    """지역명과 기상청 좌표(nx, ny) 매핑 데이터"""
    location_coords = {
        "서울": {"nx": "60", "ny": "127"},"부산": {"nx": "98", "ny": "76"},"대구": {"nx": "89", "ny": "90"},
        "인천": {"nx": "55", "ny": "124"},"광주": {"nx": "58", "ny": "74"},"대전": {"nx": "67", "ny": "100"},
        "울산": {"nx": "102", "ny": "84"},"세종": {"nx": "66", "ny": "103"},"경기": {"nx": "60", "ny": "120"},
        "강원": {"nx": "73", "ny": "134"},"충북": {"nx": "69", "ny": "107"},"충남": {"nx": "68", "ny": "100"},
        "전북": {"nx": "63", "ny": "89"},"전남": {"nx": "51", "ny": "67"},"경북": {"nx": "89", "ny": "91"},
        "경남": {"nx": "91", "ny": "77"},"제주": {"nx": "52", "ny": "38"}
    }

    return json.dumps(location_coords, ensure_ascii=False)

# 도구: 지역명으로 좌표 변환
@mcp.tool()
async def get_location_coords(ctx: Context, location: str) -> str:
    """
    지역명으로 기상청 좌표를 조회한다.
    
    Args:
        location: 조회할 지역명 (예: 서울, 부산)
    
    Returns:
        해당 지역의 기상청 좌표(nx, ny) 정보
    """
    # 리소스에서 지역-좌표 데이터 가져오기
    location_data = await ctx.read_resource("custom://location_coords")
    location_data = location_data[0].content
    location_data = json.loads(location_data)
    
    if location in location_data:
        return json.dumps(location_data[location], ensure_ascii=False)
    else:
        return json.dumps({"error": f"'{location}' 지역을 찾을 수 없습니다."}, ensure_ascii=False)

# 날씨 조회 프롬프트 추가
@mcp.prompt()
def coords_query(location: str) -> str:
    """
    특정 지역의 기상청 좌표를 조회하기 위한 프롬프트
    """
    return f"""
다음 지역의 기상청 좌표(nx, ny) 정보를 조회해주세요: {location}

get_location_coords 도구를 사용하여 {location}의 좌표를 확인하고 알려주세요.
"""

# 서버 시작
if __name__ == "__main__":
    mcp.run()
