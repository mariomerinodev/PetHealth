import uuid
from sqlalchemy import Column, String, Date, Numeric, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from ...config.database import Base


class Pet(Base):
    __tablename__ = "pets"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default="gen_random_uuid()")
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String(100), nullable=False)
    species = Column(String(50), nullable=False)
    breed = Column(String(100), nullable=True)
    birth_date = Column(Date, nullable=True)
    weight_kg = Column(Numeric(5, 2), nullable=True)
    microchip_number = Column(String(50), nullable=True)
    photo_url = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default="CURRENT_TIMESTAMP", nullable=True)

    # Relación bidireccional con el usuario
    owner = relationship("User", back_populates="pets")