from bonobo.ext.jupyter.widget import BonoboWidget
from bonobo.plugins import Plugin

try:
    import IPython.core.display
except ImportError as e:
    import logging

    logging.exception(
        'You must install Jupyter to use the bonobo Jupyter extension. Easiest way is to install the '
        'optional "jupyter" dependencies with «pip install bonobo[jupyter]», but you can also install a '
        'specific version by yourself.'
    )


class JupyterOutputPlugin(Plugin):
    def initialize(self):
        self.widget = BonoboWidget()
        IPython.core.display.display(self.widget)

    def run(self):
        self.widget.value = [repr(node) for node in self.context.parent.nodes]

    finalize = run


"""
TODO JUPYTER WIDGET
###################

# close the widget? what does it do?
https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20Basics.html#Closing-widgets

"""
