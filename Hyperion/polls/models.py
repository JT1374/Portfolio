
# Imports.
from django.db import models


# Models for polls.
class Question(models.Model):
    """
    Model for a question in a poll.
    
    It's attributes are:
    - question_text(str): The text of the question.
    - pub_date(datetime): The date the question was published.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    """
    Model for a choice in a poll.
    
    It's attributes are:
    - question(Question): The question this choice belongs to.
    - choice_text(str): The text of the choice.
    - votes(int): The number of votes this choice has received.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
