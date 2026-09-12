from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class User(Base):
    # 3. Specify the table name
    __tablename__ = "users"

class User(Base):
    # 3. Specify the table name
    __tablename__ = "users"
    
    # 4. Map columns with explicit primary key requirements
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    age: Mapped[int] = mapped_column(Integer(3))