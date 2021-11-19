```python
test = [
    "My neighbors have a cat. It has a bushy tail.",
    "Here is the book now take it.",
    "The sign was too far away for the boy to read it.",
    "Dog is man's best friend. It is always loyal.",
    "The girl said she would take the trash out.",
    "I voted for Nader because he is clear about his values. His ideas represent a majority of the nation. He is better than Rajeev.",
    "Jack von Doom is one of the top candidates in the elections. His ideas are unique compared to Neha's.",
    "Members voted for John because they see him as a good leader.",
    "Leaders around the world say they stand for peace.",
    "My neighbours just adopted a puppy. They care for it like a baby.",
    "I have many friends. They are an important part of my life.",
    "Jarbas has a dog named Jurebes. He loves his dog!",
    "London is the capital and most populous city of England and the United Kingdom. Standing on the River Thames in the south east of the island of Great Britain, London has been a major settlement for two millennia. It was founded by the Romans, who named it Londinium."
]
for utt in test:
    print(NeuralCoreferenceDemo().transform([utt])[0])
```

output
```python
['My neighbors have a cat. It has a bushy tail.', 'My neighbors have a cat. a cat has a bushy tail.']
['Here is the book now take it.', 'Here is the book now take the book.']
['The sign was too far away for the boy to read it.', 'The sign was too far away for the boy to read the sign.']
["Dog is man's best friend. It is always loyal.", "Dog is man's best friend. It is always loyal."]
['The girl said she would take the trash out.', 'The girl said the girl would take the trash out.']
['I voted for Nader because he is clear about his values. His ideas represent a majority of the nation. He is better than Rajeev.', 'I voted for Nader because nader is clear about nader values. nader ideas represent a majority of the nation. nader is better than Rajeev.']
["Jack von Doom is one of the top candidates in the elections. His ideas are unique compared to Neha's.", "Jack von Doom is one of the top candidates in the elections. jack von doom ideas are unique compared to Neha's."]
['Members voted for John because they see him as a good leader.', 'Members voted for John because members see john as a good leader.']
['Leaders around the world say they stand for peace.', 'Leaders around the world say leaders around the world stand for peace.']
['My neighbours just adopted a puppy. They care for it like a baby.', 'My neighbours just adopted a puppy. my neighbours care for a puppy like a baby.']
['I have many friends. They are an important part of my life.', 'I have many friends. many friends are an important part of my life.']
['Jarbas has a dog named Jurebes. He loves his dog!', 'Jarbas has a dog named Jurebes. jarbas loves jarbas dog!']
['London is the capital and most populous city of England and the United Kingdom. Standing on the River Thames in the south east of the island of Great Britain, London has been a major settlement for two millennia. It was founded by the Romans, who named it Londinium.', 
 'London is the capital and most populous city of England and the United Kingdom. Standing on the River Thames in the south east of the island of Great Britain, London has been a major settlement for two millennia. london was founded by the Romans, who named london Londinium.']
```