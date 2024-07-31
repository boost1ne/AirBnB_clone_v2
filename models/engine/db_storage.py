#!/usr/bin/python3
"""Storage class for storing databases."""
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv


class DBStorage:
    """A storage class for SQLAlchemy"""
    __engine = None
    __session = None

    def __init__(self):
        """ Initialize the database """
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        db_url = "mysql+mysqldb://{}:{}@{}/{}".format(
            user, password, host, db)

        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        obj_list = []
        if cls:
            if isinstance(cls, str):
                try:
                    cls = globals()[cls]
                except KeyError:
                    pass
            if issubclass(cls, Base):
                obj_list = self.__session.query(cls).all()
        else:
            for subclass in Base.__subclasses__():
                obj_list.extend(self.__session.query(subclass).all())

        obj_dict = dict()
        for obj in obj_list:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """Adds an object to the current database session (self.__session)"""
        self.__session.add(obj)

    def save(self):
        """Commit the changes made to the database session (self.__session)"""
        self.__session.commit()

    def delete(self, obj=None):
        """Removes an object from the current
        database session (self.__session)"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads the database session (self.__session)"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Call the remove() method on the private session attribute."""
        self.__session.close()
