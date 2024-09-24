import ormar
from db.connection import BaseMeta


class Data1(ormar.Model):
    class Meta(BaseMeta):
        tablename = "data_1"

    id = ormar.Integer(primary_key=True)
    name = ormar.String(max_length=300)


class Data2(ormar.Model):
    class Meta(BaseMeta):
        tablename = "data_2"

    id = ormar.Integer(primary_key=True)
    name = ormar.String(max_length=300)


class Data3(ormar.Model):
    class Meta(BaseMeta):
        tablename = "data_3"

    id = ormar.Integer(primary_key=True)
    name = ormar.String(max_length=300)

