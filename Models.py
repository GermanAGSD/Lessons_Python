from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from DataBaseSqlAlchemy import Base


class Hosts(Base):
    __tablename__ = "hosts"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    params = Column(String, nullable=False)
    name = Column(String, nullable=True)
    region = Column(String, nullable=True)



    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
