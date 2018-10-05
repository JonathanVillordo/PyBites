import re


vowels = '[aeiouAEIOU]'
count = 0

def strip_vowels(text: str ) ->   str :

     
    replace: str = text.replace('a','*').replace('e','*').replace('i','*').replace('o','*').replace('u','*').replace('A','*').replace('E','*').replace('I','*').replace('O','*').replace('U','*') 
    count: int = len(re.findall(vowels,text))
    
    return (replace,count)


def test_strip_vowels_on_other_text():
    text = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

    output, number_replacements = strip_vowels(text)
    print(number_replacements)
    print(output)

    
    

    #assert number_replacements == 43

    #assert 'H*ll* w*rld!' in output
    #assert 'H*v* f*n w*th **r B*t*s *f Py' in output
    #assert 'B*c*m* * PyB*t*s n*nj*!' in output

    assert number_replacements == 262

    assert 'Th* Z*n *f Pyth*n, by T*m P*t*rs' in output
    assert 'B***t*f*l *s b*tt*r th*n *gly' in output
    assert 'N*m*sp*c*s *r* *n* h*nk*ng gr**t *d**' in output
 


#print(test_strip_vowels_on_other_text())



text = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
 
print(test_strip_vowels_on_other_text())





