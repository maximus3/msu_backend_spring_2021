class CustomMeta(type):
    def __new__(cls, name, bases, attrs):
        new_attrs = {
            key if key.startswith('__') and key.endswith('__') else
            f'custom_{key}': value for key, value in attrs.items()
        }

        return super().__new__(cls, name, bases, new_attrs)
