from .topic_handler import TopicHandler
from .topics.fraction_adding import FractionAdding


topics = TopicHandler()
topics.add_topic(FractionAdding())
