from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models import Base, User, Purchase, Item

# ORM 방식 데이터를 처리해주고 있다. => 나중에 MySql로 하면 SQL로도 가능하다.

engine = create_engine("sqlite:///./test.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# 예제 데이터 추가
item1 = Item(name="삼성노트북", price=10000, stock=10, created_at=datetime.now())
item2 = Item(name="LG노트북", price=20000, stock=10, created_at=datetime.now())
item3 = Item(name="맥북에어", price=30000, stock=10, created_at=datetime.now())
item4 = Item(name="맥북프로13", price=40000, stock=10, created_at=datetime.now())
item5 = Item(name="맥북프로16", price=50000, stock=10, created_at=datetime.now())

session.add_all([item1, item2, item3, item4, item5])
session.commit()

user1 = User(name='홍길동', email='hong@test.com', phone='01012345678', created_at=datetime.now())
user2 = User(name='오길동', email='oh@test.com', phone='01022345678', created_at=datetime.now())


session.add_all([user1, user2])
session.commit()

purchase1 = Purchase(user_id=user1.id, item_id=item4.id, quality=1, status='paid', purchase_date=datetime.now())
purchase2 = Purchase(user_id=user1.id, item_id=item5.id, quality=1, status='canceled', purchase_date=datetime.now())


session.add_all([purchase1, purchase2])
session.commit()