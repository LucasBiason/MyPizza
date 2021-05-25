

def set_fields(class_model):

    for field in class_model._meta.fields:
        if hasattr(field, 'max_length'):
            setattr(class_model, field.name+"_max_length", field.max_length)

        if hasattr(field, 'verbose_name'):
            setattr(class_model, field.name+"_verbose", field.verbose_name)

        if hasattr(field, 'max_digits'):
            setattr(class_model, field.name+"_max_digits", field.max_digits)

        if hasattr(field, 'decimal_places'):
            setattr(class_model, field.name+"_decimal_places", field.decimal_places)

        if hasattr(field, 'choices'):
            setattr(class_model, field.name+"_choices", field.choices)

    return class_model
