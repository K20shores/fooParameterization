# fooParameterization
Mock atmospheric sea-spray physics parameterization package
___

## Prompt

You are asked to write a software package that calculates the complex (yet entirely fictitious) Foo et al. parameterization for atmospheric sea-spray physics. For our purposes, the parameterization can take the radius of a sphere and return its volume. However, imagine that this parameterization is complex enough to warrant its own software package.


You may implement the parameterization in a language of your choice (you will not be asked to justify your choice of language or be asked about performance considerations). Your design should be based on the following considerations:


* This will be a community project and you expect continuous introduction of new science features over the course of many years by many contributors
* You want to target a wide range of users: from those who want to use your software directly and interactively to those who want to incorporate your implementation of Foo physics in larger software packages


Be prepared to discuss the reasoning behind specific design choices. We expect this task to take only a couple hours. If there are features of your software that are not feasible to implement in this short time, indicate what these would be and be prepared to discuss them during the interview.

## Instructions for Running

`foo` can be run interactively or integrated into other software packages. The python notebook, `Interactive.ipynb`, shows example
of real-time usage, while `incorporated.py` shows usage within a larger program. A simple program is shown below

```python
from foo.parameterization import Foo22

param = Foo22()
print(param.compute(2))
```

## Contributing
Fork the repository and do your work in a new branch. After you've completed your work with thorough testing, make a pull request and someone will review it!