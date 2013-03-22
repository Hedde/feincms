from django.forms.widgets import RadioFieldRenderer
from django.forms import RadioSelect
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe


class ThumbnailRenderer(RadioFieldRenderer):
    def render(self):
        """Outputs a <ul> for this set of radio fields."""
        def _is_active(choice, value):
            if choice == value:
                return 'active'
            return 'inactive'
        return mark_safe(u'<ul class="thumbnail_select_widget">\n%s\n</ul>' % u'\n'.join([
            u"""
            <li class="%s">
                <img onclick="$(this).parent().find('input').select()" src="/static/feincms/img/templates/%s.jpg" />
                <span style="display:none">%s</span>
            </li>
            """ % (_is_active(w.choice_value, self.value),
                   force_unicode(w.choice_value.split('.')[0]),
                   force_unicode(w)) for w in self])
        )

class ThumbnailSelect(RadioSelect):
    renderer = ThumbnailRenderer

    class Media:
        css = {
            'all': ('/static/feincms/css/thumbnail_select.css',)
        }