from collections import defaultdict

from fractions_app.helper import Topic, Level


class TopicHandler:
    """TopicHandler is used for storing all Topics. It is singleton."""

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
        self.__subtopics_by_level = defaultdict(list)

    def add_topic(self, topic: Topic) -> None:
        """Add topic to topics list.

        Raises:
            ValueError: if type of `topic` is not Topic.
        """

        if not isinstance(topic, Topic):
            raise ValueError(
                f"Argument 'topic' must be type {Topic}, not {type(topic)}."
            )

        self.__topics.append(topic)

        for subtopic in topic.subtopics:
            self.__subtopics_by_level[subtopic.level].append(subtopic)

    def get_topics(self):
        yield from self.__topics

    def get_subtopics_by_level(self, level: Level) -> list:
        return self.__subtopics_by_level[level]
