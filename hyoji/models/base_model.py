from peewee import ForeignKeyField

from hyoji.models import db

class BaseModel(db.Model):
    def to_dict(model, fields=None, exclude=None):
        """
        Taken from flask_peewee.utils.py
        https://github.com/coleifer/flask-peewee/blob/master/flask_peewee/utils.py
        https://github.com/coleifer/peewee/issues/134
        """
        model_class = type(model)
        data = {}

        fields = fields or {}
        exclude = exclude or {}
        curr_exclude = exclude.get(model_class, [])
        curr_fields = fields.get(model_class, model._meta.sorted_field_names)

        for field_name in curr_fields:
            if field_name in curr_exclude:
                continue
            field_obj = model_class._meta.fields[field_name]
            field_data = model._data.get(field_name)
            if isinstance(field_obj, ForeignKeyField) and field_data and field_obj.rel_model in fields:
                rel_obj = getattr(model, field_name)
                data[field_name] = get_dictionary_from_model(rel_obj, fields, exclude)
            else:
                data[field_name] = field_data
        return data
