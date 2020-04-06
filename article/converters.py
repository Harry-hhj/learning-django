from django.urls import register_converter


class CatergoryConverter(object):
    regex = r'\w+|(\w+\+\w+)+'

    def to_python(self, value):
        result = value.split('+')
        return result

    def to_url(self, value):
        if isinstance(value, list):
            result = "+".join(value)
            return result
        else:
            raise RuntimeError("转换url的时候，转换参数必须为列表！")


register_converter(CatergoryConverter, 'cate')
