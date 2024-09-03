# 디비를 만드는 코드
# python -> DB를 SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# 테이블 구조
class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    price = Column(Integer)
    stock = Column(Integer)
    created_at = Column(DateTime)


# 강의를 하는 것보다 듣는 게 더 힘들어요.
# - 모토: 쓸데없는 것 보다 필요한 거 빠르게 배워서 바로 써먹자.
# - AI 공부할 때도 과외를 받았어요. => 

# 앱 개발 -> 1개당 1~3천 // 옆 마을 AI: 단가 1억 => 무조건 해야겠다.
# LLM => 챗봇.AI Agent.자동화 => 펜션 관련 자동화 (예약이 잡히면 문자보내고, 잘 오고 계신가요???) => 구매.
# 다음 달에 제주도에 리조트 -> 자동화 시스템 2주