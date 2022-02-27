# nonsentence
A Python module that generates nonsense sentences under the scheme vowel-consonsant-vowel..., with customisable sentence and word length.
I'm not sure who this is intended for, but someday someone is going to find this very useful. Maybe.
## Usage
Install from PyPi:
`pip install nonsentence`
```py
import nonsentence
nonsentence.new_sentence(sentence_length, min_word_length, max_word_length)
```
### Example
```py
>>> nonsentence.new_sentence(10, 4, 12)
'xeratihut lux qihaci def zevepehot piroqihuc tegot wejijiquh tet gaza piqitadu.'
```

### About
One afternoon, I was writing some code to generate random, meaningless sentences for my computer to say aloud -- you know, for practical and educational purposes. I lamented the lack of existing options for programmatically generating rubbish, and thus nonsentence was born, to save other poor souls from having to deal with this problem ever again.

It was fun to learn how code goes from being a Python file on my laptop to being downloadable from pip! I highly recommend making your own modules. Maybe yours won't be as significant and important as mine, but we all have to start somewhere. [/j]
