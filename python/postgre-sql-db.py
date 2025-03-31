from sqlalchemy import create_engine # движок для подключения
from sqlalchemy.orm import DeclarativeBase # базовая модель
from sqlalchemy.orm import sessionmaker # сессия
from sqlalchemy import  Column, Integer, String, DateTime, CHAR, Date, Boolean

# подключение движка
# engine = create_engine("postgresql://postgre:qwerty1234@localhost/mydb")

# создание класса с базовой моделью
class Base(DeclarativeBase): pass

# Пациенты: id, ФИО, дата рождения, пол, телефон, email, адрес, полис ОМС
class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fio = name = Column(String)
    birthdate = Column(Date)
    gender = Column(String) # бывший Column(CHAR)
    phone = Column(String)
    email = Column(String)
    adress = Column(String)
    oms = Column(String)

# Врачи: id, ФИО, специальность, кабинет, номер телефона, email.
class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fio = Column(String)
    spec = Column(String)
    cab = Column(Integer)
    phone = Column(String)
    email = Column(String)

# Услуги: id, наименование, стоимость, описание, длительность
class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    price = Column(Integer)
    description = Column(String)
    duration = Column(Integer)

# Записи на приём: id, пациент, врач, дата и время, услуга, статус (запланировано/выполнено/отменено).
class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    # [пациент из patients]
    # [врач из doctors]
    datetime = Column(DateTime)
    # [услуга из services]
    status = Column(String)

# Диагнозы: id, приём, диагноз, комментарии врача.
class Diagnose(Base):
    __tablename__ = "diagnoses"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    # [id от appointments]
    diagnose = Column(String)
    comment = Column(String)

# Расписание врачей: id, врач, день недели, рабочее время (с/до), доступность.
class Timetable(Base):
    __tablename__ = "timetables"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    # [врач из doctors]
    day = Column(String)
    worktime = Column(String)
    availability = Column(Boolean)


# создаем таблицы
Base.metadata.create_all(bind=engine)
print("База данных и таблица созданы")

# создаем класс сессии
Session = sessionmaker(autoflush=False, bind=engine)