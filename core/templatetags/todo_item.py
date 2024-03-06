from django import template

register = template.Library()


@register.inclusion_tag('todo_item.html')
def todo_item(todo):
    return {'todo': todo}
