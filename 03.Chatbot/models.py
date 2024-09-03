# 디비를 만드는 코드
# python -> DB를 SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# 테이블 구조
class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    price = Column(Integer)
    stock = Column(Integer)
    created_at = Column(DateTime)
    

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String)
    name = Column(String)
    phone = Column(String)
    created_at = Column(DateTime)
    
    # 사용자가 구매한 구매이력들에 대한 참조가 가능
    purchase = relationship('Purchase', back_populates='user') #역참조(ORM 방식) => 부모도 자녀를 찾을 수 있도록!
    
class Purchase(Base):
    __tablename__ = 'purchases'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    quality = Column(Integer)
    status = Column(String)
    purchase_date = Column(DateTime)    
    
    user = relationship('User', back_populates='purchase')
    item = relationship("Item")