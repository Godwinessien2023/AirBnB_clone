#!/usr/bin/python3
"""
defines a base class module
"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """
    parent class for all other classes
    """
    def __init__(self, *args, **kwargs):
        time_format = '%Y-%m-%dT%H:%M:%S.%f'

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

        models.storage.new(self)

    def save(self):
        """
        update the updaated attribute wth the
        current datetime
        """

        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        to convert instance to dictionary(serialization)
        """
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__

        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()

        return inst_dict

    def __str__(self):
        """
        to incorporate a string to instance or object
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)


if __name__ == "__main__":
    main()
