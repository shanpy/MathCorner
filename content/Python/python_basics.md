Title: Python Basics
Date: 2015-01-13
Modified: 2015-05-30
Category: Python
Tags: Python
Slug: python-basics
Authors: Pengyin Shan
Summary: This post is transferred from my <a href="blogpengyin.herokuapp.com">old blog site</a>. This is a reading note for Appendix in the book of **Python for Data Analysis**, published by *O'Reilly, 2012*. The appendix of this book describes python basic syntax and information, which I think is very useful for python beginners like me.

This post is transferred from my <a href="blogpengyin.herokuapp.com">old blog site</a>. 

This is a reading note for Appendix in the book of **Python for Data Analysis**, published by *O'Reilly, 2012*. The appendix of this book describes python basic syntax and information, which I think is very useful for python beginners like me.

##Basic Information

{% notebook python-basics-basic-information.ipynb %}

##List

{% notebook python-basics-list.ipynb %}

##Tuple

{% notebook python-basics-tuple.ipynb %}

##Dictionary and Set

{% notebook python-basics-dictionary-and-set.ipynb %}

##Function

{% notebook python-basics-functions.ipynb %}

##IPython Basics

In IPython, `print` is used to print more *readable* result.

Same as what's happening in terminal, `<tab>` button in IPython can do *auto-complete*.

`object introspection`: `?variable_name` in IPython can provide information about this variable:
{% img ../images/posts/?ipython.png %}

`function_name??` will show this function's source code if exists.

`*name*` is *wildcard* operation. It can list result that is combined by 'XXnameX' or 'nameXXX'

`%paste` and `%cpaste` can takes code on clipboard then execute it in a single block in the shell

*magic command*: It is prefixed by the percentage symbol `%`