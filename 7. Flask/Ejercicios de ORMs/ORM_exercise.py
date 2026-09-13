from sqlalchemy import create_engine, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session

DB_URI = 'postgresql://postgres:postgres@localhost:5432/postgres'
engine = create_engine(DB_URI, echo=True)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

    addresses: Mapped[list["Address"]] = relationship(back_populates="user")
    cars: Mapped[list["Car"]] = relationship(back_populates="user")

    @classmethod
    def create_user(cls, session: Session, name: str, address: str | None = None):
        user = cls(name=name)
        if address:
            user.addresses.append((Address(address=address)))
        session.add(user)
        session.commit()
        return user

    @classmethod
    def get_user(cls, session: Session, user_id: int):
        return session.query(cls).filter_by(id=user_id).first()

    @classmethod
    def update_user(cls, session: Session, user_id: int, new_name: str):
        user = session.query(cls).filter_by(id=user_id).first()
        if user:
            user.name = new_name
            session.commit()

    @classmethod
    def delete_user(cls, session: Session, user_id: int):
        user = session.query(cls).filter_by(id=user_id).first()
        if user:
            session.delete(user)
            session.commit()
    
class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE")) # not nullable
    address: Mapped[str]

    user: Mapped["User"] = relationship(back_populates="addresses")

    @classmethod
    def create_address(cls, session: Session, user_id: int, address: str):
        addr = cls(user_id=user_id, address=address)
        session.add(addr)
        session.commit()

    @classmethod
    def get_address(cls, session: Session, address_id: int):
        return session.query(cls).filter_by(id=address_id).first()

    @classmethod
    def update_address(cls, session: Session, address_id: int, new_address: str):
        address = session.query(cls).filter_by(id=address_id).first()
        if address:
            address.address = new_address
            session.commit()

    @classmethod
    def delete_address(cls, session: Session, address_id: int):
        address = session.query(cls).filter_by(id=address_id).first()
        if address:
            session.delete(address)
            session.commit()

class Car(Base):
    __tablename__ = "car"

    id: Mapped[int] = mapped_column(primary_key=True)
    # nullable and ondelete set to null -> if the user is deleted, the user_id in the car table will be set to null
    user_id: Mapped[int| None] = mapped_column(ForeignKey("user.id", ondelete="SET NULL")) 
    year: Mapped[int]
    model: Mapped[str]
    brand: Mapped[str]

    user: Mapped["User"] = relationship(back_populates="cars")

    @classmethod
    def create_car(cls, session: Session, user_id: int | None, year: int, model: str, brand: str):
        car = cls(user_id=user_id, year=year, model=model, brand=brand)
        session.add(car)
        session.commit()
        return car

    @classmethod
    def get_car(cls, session: Session, car_id: int):
        return session.query(cls).filter_by(id=car_id).first()

    @classmethod
    def update_car(cls, session: Session, car_id: int, new_year: int, new_model: str, new_brand: str):
        car = session.query(cls).filter_by(id=car_id).first()
        if car:
            car.year = new_year
            car.model = new_model
            car.brand = new_brand
            session.commit()
        return car

    @classmethod
    def assign_to_user(cls, session: Session, car_id: int, user_id: int):
        try:
            user = session.query(User).filter_by(id=user_id).first()
            if not user:
                raise ValueError(f"User with id {user_id} does not exist.")

            car = session.query(cls).filter_by(id=car_id).first()
            if not car:
                raise ValueError(f"Car with id {car_id} does not exist.")
            elif car.user_id is not None:
                raise ValueError(f"Car with id {car_id} is already assigned to the user with id {car.user_id}.")
            else:
                car.user_id = user_id
                session.commit()
        except ValueError as e:
            print(f"Error: {e}")
            return None
        return car

    @classmethod
    def delete_car(cls, session: Session, car_id: int):
        car = session.query(cls).filter_by(id=car_id).first()
        if car:
            session.delete(car)
            session.commit()
        return car

    @classmethod
    def delete_car(cls, session: Session, car_id: int):
        car = session.query(cls).filter_by(id=car_id).first()
        if car:
            session.delete(car)
            session.commit()

# Used to drop all tables and create them again, for changing the schema.
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


#Validates if the tables already exist, if not, it creates them.
# Base.metadata.create_all(engine, checkfirst=True) 

with Session(engine) as session:
    #Creating a user with an address
    u = User.create_user(session, "spongebob", address="Bikini Bottom, Pinaple House")
    c = Car.create_car(session, None, 2020, "Corolla", "Toyota")

    # Happy path
    Car.assign_to_user(session, c.id, u.id)

    # Trying to assign the same car to another user
    u2 = User.create_user(session, "patrick", address="Bikini Bottom, Rock House")
    Car.assign_to_user(session, c.id, u2.id)

    # assign to a non-existent user
    Car.assign_to_user(session, c.id, 999)

    # assign a non-existent car to a user
    Car.assign_to_user(session, 999, u.id)  
