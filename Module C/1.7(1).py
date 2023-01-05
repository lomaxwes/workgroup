class Event:
    def __init__(self, timestamp=0, event_type="", session_id=""):
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id

    def init_from_dict(self, event_dict):
        self.timestamp = event_dict.get("timestamp")
        self.type = event_dict.get("type")
        self.session_id = event_dict.get("session_id")

    def show_description(self):
        print("This is generic event.")


class ItemViewEvent(Event):
    type = "itemViewEvent"

    def __init__(self, timestamp=0, session_id="", number_of_views=0):
        self.timestamp = timestamp
        self.session_id = session_id
        self.number_of_views = number_of_views

    def show_description(self):
        print("This event means someone has browsed an item.")


if __name__ == "__main__":
    test_view_event = ItemViewEvent(timestamp=1549461608000, session_id="0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct", number_of_views=6)
    test_view_event.show_description()
    print(test_view_event.type)


print(isinstance("foo", str))
# True
print(isinstance(test_view_event, ItemViewEvent))
# True

# Но у этого метода есть загвоздка:
print(isinstance(test_view_event, Event))
# True

# Мы видим, что для родительского класса функция также вернёт True.
# На самом деле, по этой и ряду других причин не всегда хорошо завязывать логику на проверку типа через isinstance.
# Мы уже говорили о том, что в некотором смысле в Python всё — объект.
# Это означает, что «под капотом» все классы и типы в Python наследуются от object.

print(isinstance("foo", object))
# True