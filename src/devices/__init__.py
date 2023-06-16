from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship

from ..database import Base


class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    serial_number = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    device_model_id = Column(Integer, ForeignKey("device_models.id"))

    device_model = relationship("DeviceModel", back_populates="device")

    __table_args__ = UniqueConstraint("serial_number", "device_model_id")


class DeviceModel(Base):
    __tablename__ = "device_models"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    technical_name = Column(String, unique=True, index=True)
    device_id = Column(Integer, ForeignKey("devices.id"))
