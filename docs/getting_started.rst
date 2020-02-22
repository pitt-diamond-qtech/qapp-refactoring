**Getting Started**
===================

Code Methodologies
******************
| As with many large collaborative software projects, version control is very important, which means
  that learning to effectively use both **git** and **GitHub** is important.
  The general steps for working on assigned issues are:
#. Fork the repository onto your own **GitHub** account and then clone the forked repository onto your local machine.
#. Familarize yourself with the test functions corresponding to the functionality that you are contributing to.
   Test functions are created using **PyTest**.
  
   * If you must write new test functions, you must consult with Dr. Dutt or other team members before moving forward.

#. While writing new code, keep commits to your forked repository well-commented and functionality-specific. 
   
   * For example, if you write new code and also change the static documentation, commit these changes separately.
#. Run **PyTest** to verify that your code works and does not introduce any errors.
#. *If your code passes testing*, submit a pull request on **GitHub** to merge with the main repository.
   
   * Make sure that your changes are well documented so that they can be reviewed before the pull request is accepted.

Documentation
*************

| The documentation for this project is being automatically 
  generated using `Sphinx <https://www.sphinx-doc.org/en/master/>`_. 
  **reStructuredText** is used to create the static elements of the documentation. 
  A very useful guide for getting started with **reStructuredText** can be 
  found `here <https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html>`_.
| Part of the functionality of Sphinx is the automatic generation of documentation 
  directly from the source files. This means that for comments to be parsed by Sphinx
  and to be ultimately included in the documentation, they must follow a specific form.
  An example can be found `here <https://thomas-cokelaer.info/tutorials/sphinx/docstring_python.html>`_, 
  and a basic example is provided below:
.. code-block::

   class MainClass1(object):
    """This class docstring shows how to use sphinx and rst syntax

    The first line is brief explanation, which may be completed with 
    a longer one. For instance to discuss about its methods.
    """

    def function1(self, arg1, arg2, arg3):
      """returns (arg1 / arg2) + arg3

      This is a longer explanation, which may include math with latex syntax
      :math:`\\alpha`.

      :param arg1: the first value
      :param arg2: the first value
      :param arg3: the first value
      :type arg1: int, float,...
      :type arg2: int, float,...
      :type arg3: int, float,...
      :returns: arg1/arg2 +arg3
      :rtype: int, float
      """
      return arg1/arg2 + arg3
