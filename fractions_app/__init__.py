from .topic_handler import TopicHandler
from .topics.fraction_adding import FractionAdding
from .topics.fraction_substracting import FractionSubstracting
from .topics.fraction_multiplicating import FractionMultiplicating
from .topics.fraction_dividing import FractionDividing


topics = TopicHandler()
topics.add_topic(FractionAdding())
topics.add_topic(FractionSubstracting())
topics.add_topic(FractionMultiplicating())
topics.add_topic(FractionDividing())
