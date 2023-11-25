from .topic_handler import TopicHandler
from .topics.fraction_adding import FractionAdding
from .topics.fraction_subtracting import FractionSubtracting
from .topics.fraction_multiplication import FractionMultiplication
from .topics.fraction_dividing import FractionDividing


topics = TopicHandler()
topics.add_topic(FractionAdding())
topics.add_topic(FractionSubtracting())
topics.add_topic(FractionMultiplication())
topics.add_topic(FractionDividing())
