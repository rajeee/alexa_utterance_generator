class PG(object): #phase group
    def __init__(self,*kwargs):
        self.phrase_list = list(kwargs)

    def append(self,word):
        self.phrase_list.append(word)
    def __iter__(self):
        return iter(self.phrase_list)

    def __len__(self):
        return len(self.phrase_list)

    def __add__(self, other):
        result = PG()
        if type(other) == str:
            other = PG(other)
        elif type(other) == PG:
            pass
        else:
            print(other)
            raise TypeError('Cannot convert type ' + str(type(other))+ ' to PhraseGroup')
        for my_word in self:
            for their_word in other:
                result.append(my_word + their_word)
        return result
    def __radd__(self, other):
        result = PG()
        if type(other) == str:
            other = PG(other)
        elif type(other) == PG:
            pass
        else:
            print(other)
            raise TypeError('Cannot convert type ' + str(type(other)) + ' to PhraseGroup')
        for their_word in other:
            for my_word in self:
                result.append(their_word + my_word)
        return result

    def __repr__(self):
        return '\n'.join([str(x) for x in self.phrase_list])

    def __str__(self):
        return '\n'.join([str(x) for x in self.phrase_list])


utterance = PG()
utterance.append("call_intent "+ PG("Phone ","Call ","Telephone ") + "{contact} " + PG("please",""))
utterance.append("add_intent "+ PG("Add ","Sum ") + PG(PG("those","the") + " " + PG("values","numbers","answers")
                                    ,"{first_number} and {second_number}"))
print(utterance)

with open('utterance.txt','w') as f:
    f.write(str(utterance))