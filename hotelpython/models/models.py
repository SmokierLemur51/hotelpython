import datetime
from typing import List

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(60), nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(String(12), nullable=False, unique=True)
    f_name: Mapped[str] = mapped_column(String(40), nullable=False)
    l_name: Mapped[str] = mapped_column(String(40), nullable=False)
    passhash: Mapped[str] = mapped_column(String(60))

    total_bookings: Mapped[int] = mapped_column(Integer)
    # does the func for this go here or somewhere else


class Address(Base):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(primary_key=True)
    street: Mapped[str] = mapped_column(String(100), nullable=False)
    city: Mapped[str] = mapped_column(String(30), nullable=False)
    state: Mapped[str] = mapped_column(String(2), nullable=False)
    zip: Mapped[str] = mapped_column(String(5), nullable=False)

    hotel: Mapped["Address"] = relationship("Hotels",
                                              back_populates="address")

    def __repr(self) -> str:
        return f"Street: {self.street!r}, City: {self.city!r}, State: {self.state!r}, Zip: {self.zip!r}"


class EmployeeRole(Base):
    __tablename__ = "employee_roles"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    role: Mapped[str] = mapped_column(String(30), nullable=False)
    role_description: Mapped[str] = mapped_column(String(250), nullable=False)

    employees: Mapped[List["Employee"]] = relationship(back_populates="role")

    
class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(primary_key=True)
    f_name: Mapped[str] = mapped_column(String(40), nullable=False)
    m_name: Mapped[str] = mapped_column(String(40), nullable=False)
    l_name: Mapped[str] = mapped_column(String(40), nullable=False)
    email: Mapped[str] = mapped_column(String(60), nullable=False, unique=True)
    hourly: Mapped[float] = mapped_column(Float, nullable=False)

    role: Mapped[int] = mapped_column(ForeignKey("employee_roles.id"), nullable=False)
    
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels.id"))
    hotel: Mapped["Hotel"] = relationship(back_populates="employees")

    address_id: Mapped[int] = mapped_column(ForeignKey("addresses.id"))
    address: Mapped["Address"] = relationship(back_populates="employees")

    def __repr__(self) -> str:
        return f"Employee: {self.f_name!r}, ID: {self.id!r}"


class Hotel(Base):
    __tablename__ = "hotels"

    id: Mapped[int] = mapped_column(primary_key=True)
    hotel: Mapped[str] = mapped_column(String(50), nullable=False)
    address: Mapped[int] = mapped_column(ForeignKey("addresses.id"))
    floors: Mapped[int] = mapped_column(Integer, nullable=False)

    # reference employees
    employees: Mapped[List["Employee"]] = relationship(
        back_populates="hotel", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"Hotel: {self.hotel!r}, ID: {self.id!r}"


class Room(Base):
    __tablename__ = "rooms"

    id: Mapped[int] = mapped_column(primary_key=True)
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels.id"))
    floor: Mapped[int] = mapped_column(Integer, nullable=False)
    room_number: Mapped[str] = mapped_column(String(50),
                                             nullable=False)  # f"Htl-Flr-Rm"
    clean: Mapped[bool] = mapped_column(Boolean, nullable=False)


class Reservation(Base):
    __tablename__ = "reservations"

    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"),
                                             nullable=False)
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels.id"),
                                          nullable=False)
    room: Mapped[int] = mapped_column(ForeignKey("rooms.id"), nullable=False)

    gross_price: Mapped[float] = mapped_column(Float, nullable=False)
    sales_tax: Mapped[float] = mapped_column(Float, nullable=False)
    # set at 0.00 if there isnt one
    discount: Mapped[float] = mapped_column(Float, nullable=False)
    total: Mapped[float] = mapped_column(Float, nullable=False)
    paid: Mapped[bool] = mapped_column(Boolean, nullable=False)
    check_in: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now())
