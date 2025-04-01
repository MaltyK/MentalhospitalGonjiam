from sqlalchemy import create_engine # движок для подключения
from sqlalchemy.orm import DeclarativeBase # базовая модель
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker # сессия
from sqlalchemy import  Column, Integer, String, DateTime, CHAR, Date, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
# from django.conf import settings

# # Получаем параметры подключения из settings.py
# db_name = settings.DATABASES['default']['NAME']
# db_user = settings.DATABASES['default']['USER']
# db_password = settings.DATABASES['default']['PASSWORD']
# db_host = settings.DATABASES['default']['HOST']
# db_port = settings.DATABASES['default']['PORT']

# # Создаем строку подключения для SQLAlchemy
# connection_string = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

# Строка подключения
connection_string = "postgresql://postgre:qwerty1234@localhost/mydb"
# Создаем движок SQLAlchemy
engine = create_engine(connection_string)

# создание класса с базовой моделью
Base = declarative_base()

# Записи на приём
class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    doctor_id = Column(Integer, ForeignKey('doctors.id'), nullable=False)
    service_id = Column(Integer, ForeignKey('services.id'), nullable=False)
    datetime = Column(DateTime, nullable=False)
    status = Column(String, nullable=False)

    patient = relationship("Patient", back_populates="appointments")
    doctor = relationship("Doctor", back_populates="appointments")
    service = relationship("Service", back_populates="appointments")
    diagnoses = relationship("Diagnose", back_populates="appointment")

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fio = Column(String)
    birthdate = Column(Date)
    gender = Column(String)
    phone = Column(String)
    email = Column(String)
    adress = Column(String)
    oms = Column(String)

    appointments = relationship("Appointment", back_populates="patient")

class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fio = Column(String)
    spec = Column(String)
    cab = Column(Integer)
    phone = Column(String)
    email = Column(String)

    appointments = relationship("Appointment", back_populates="doctor")
    timetables = relationship("Timetable", back_populates="doctor")

class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    price = Column(Integer)
    description = Column(String)
    duration = Column(Integer)

    appointments = relationship("Appointment", back_populates="service")

class Diagnose(Base):
    __tablename__ = "diagnoses"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)