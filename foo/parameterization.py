import numpy as np

class Parameterization:
    """
    This computes the parameterization for sea-spray physics defined by Foo et. al

    The parameterization is defined by 3 distinct, computationally intensive steps that are
    built off of each other. This class allows the extension of original methods.

    """

    def __init__(self, step1, step2, step3):
        """
        Parameters
        ----------
        step1 : callable
            The first step of the parameterization. This is the first step to get the argument 
        step2 : callable
            The first step of the parameterization. This is passsed the result of step 1.
        step3 : callable
            The first step of the parameterization. This is passsed the result of step 2.
        """
        self.step1 = step1
        self.step2 = step2
        self.step3 = step3

    def compute(self, R):
        """ Run the three stesp of the parameterizaiton

        Parameters
        ----------
        R : array_like
            The radius of the particle being parameterized

        Returns
        ----------
        v : array_like
            The parameterized vaule
        """
        v = self.step1(R)
        v = self.step2(v)
        v = self.step3(v)
        return v



class Foo22(Parameterization):
    """
    Compute the parameterized value as in Foo et. al
    
    This class defines the steps as laid out in the original paper with no modifications.
    """

    def __init__(self, **kwargs):
        """
        Parameters
        ----------
        **kwargs : dict
            Additional arguments passed to Parameterization
        """
        super().__init__(self.step1, self.step2, self.step3, **kwargs)
    
    def step1(self, x):
        """
        The first step.

        Parameters
        ----------
        x : array_like
            Foo et. al defines this first value to be the radius
        """
        return x**3

    def step2(self, x):
        """
        The second step.

        Parameters
        ----------
        x : array_like
            The result of the first step
        """
        return x * np.pi

    def step3(self, x):
        """
        The third step.

        Parameters
        ----------
        x : array_like
            The result of the first step
        """
        return x * (4.0 / 3.0)


class ModifiedFoo22(Foo22):
    """
    Compute the parameterized value as in Bar et. al
    
    Bar et. al modified the algorithm in Foo et. al by changing only a single step.
    That step is the second and is redefined here
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    

    def step2(self, x):
        """
        The modified second step.

        Parameters
        ----------
        x : array_like
            The result of the first step
        """
        return x * 2 * (1 / 2) * np.pi
