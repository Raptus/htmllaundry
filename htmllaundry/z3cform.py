# coding=utf-8
from zope.interface import implementer
from zope.component import adapter
from zope.schema.interfaces import IText
from zope.schema import Text
from z3c.form.converter import FieldDataConverter
from z3c.form.interfaces import IWidget
from htmllaundry.utils import sanitize


class IHtmlText(IText):
    pass


@implementer(IHtmlText)
class HtmlText(Text):
    """A HTML field. This is similar to a standard Text field, but will
    sanitize all markup passed into it.
    """
    pass


@adapter(IHtmlText, IWidget)
class HtmlDataConverter(FieldDataConverter):
    """z3c.form data convertor for HTML forms. This convertor
    sanitizes all input, guaranteeing simple and valid markup
    as a result.
    """

    def toFieldValue(self, value):
        data = super(HtmlDataConverter, self).toFieldValue(value)
        if data:
            data = sanitize(data)
        return data
