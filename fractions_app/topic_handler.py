from .helper import Topic


class TopicHandler:
    __INSTANCE = None
    __INITIALIZED = False

    def __new__(cls):
        if TopicHandler.__INSTANCE is None:
            TopicHandler.__INSTANCE = super(TopicHandler, cls).__new__(cls)
        return TopicHandler.__INSTANCE

    def __init__(self) -> None:
        if TopicHandler.__INITIALIZED:
            return
        TopicHandler.__INITIALIZED = True

        self.__topics: list[Topic] = []

    def add_topic(self, topic: Topic):
        if not hasattr(topic, "subtopics"):
            raise AttributeError(
                f"Object '{type(topic)}' haven't got an attribute 'subtopics'."
            )
        if not hasattr(topic, "title"):
            raise AttributeError(
                f"Object '{type(topic)}' haven't got an attribute 'title'."
            )

        self.__topics.append(topic)

    def get_topics(self):
        yield from self.__topics
