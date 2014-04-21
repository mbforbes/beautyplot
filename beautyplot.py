'''
Make matplotlib (pyplot) plots beautiful, because matplotlibrc is totally
broken, and prettyplotlib doesn't work either.

Thanks to Olga Botvinnik for her blog post of the long (bad) way to do things in
matplotlib

    http://blog.olgabotvinnik.com/post/58941062205/prettyplotlib-painlessly-
        create-beautiful-matplotlib

which, because her released code doesn't work, is exactly what I'm doing. There
are several stackoverflow articles that made this possible, which I only thought
of listing quite late, but here are a few:

- http://stackoverflow.com/questions/9051494/customizing-just-one-side-of-tick-
      marks-in-matplotlib-using-spines
- (use also http://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes.
      tick_params)
- http://stackoverflow.com/questions/6406368/matplotlib-move-x-axis-label-
      downwards-but-not-x-axis-ticks (though we want the 'wrong' answer, posed
      in the question, to move the tick numbers)
'''

__author__ = 'mbforbes'

# IMPORTS

# 3rd party
import matplotlib.pyplot as plt

# FUNCTIONS

def beautify():
    '''Apply beautiful settings to an existing graph (figure 1, specifically).

    FEATURES:
    ----------------------------------------------------------------------------

    General:
    - set all things that were black (axis lines, labels, title, major tick
          labels, major ticks marks) to be off-black (a dark grey)
    Axes:
    - remove the top and right axis lines ('spines')
    - make remaining axis lines thinner
    - make dotted grid for major y lines

    Ticks:
    - turn off only right and top ticks
    - set tick direction to be out (pointing out of graph)
    - set all minor ticks labels and marks to be a lighter grey
    - make major and minor ticks longer
    - make tick numbers farther away (padded) to accomodate longer ticks

    Fonts:
    - set all fonts to be serif (like Times New Roman)


    Things you need to do on your own (that aren't generalizable to put here):
    ----------------------------------------------------------------------------

    - Make sure major and minor ticks are specified correctly. Check out:
          [example] http://matplotlib.org/examples/pylab_examples/
                        major_minor_demo1.html
          [api] http://matplotlib.org/api/ticker_api.html

    - Set plotting color. Use better colors than 'blue'. Check out:
          [example] http://wiki.scipy.org/Cookbook/Matplotlib/Show_colormaps
          [example] http://colorbrewer2.org/

    - Set plotting style. Lines should be very differentiable, with lots of
      visual redundancy. This means the following should be different:
        - markers [e.g. circles, triangles, 'x's, ...]
        - color (see above)
        - and style [e.g. dashed, dotted, line, variations in-between]

    - Set error bar width and cap sizes. Error bars should be thinner than
      plotting lines. Check out:
          [example] http://stackoverflow.com/questions/7601334/how-to-set-the-
                        line-width-of-error-bar-caps-in-matplotlib

    '''
    # Settings
    almost_black = '#262626'
    more_grey = '#929292'
    text_font = 'serif'
    number_font = 'serif'

    # Get the figure and axes.
    #fig = plt.figure(1)
    ax = plt.axes()

    # Remove 'spines' (axis lines)
    spines_to_remove = ['top', 'right']
    for spine in spines_to_remove:
        ax.spines[spine].set_visible(False)

    # Make ticks only on the left and bottom (not on the spines that we removed)
    ax.yaxis.tick_left()
    ax.xaxis.tick_bottom()

    # To remove the ticks all-together (like in prettyplotlib), do the following
    # instead of tick_left() and tick_bottom()
    #ax.xaxis.set_ticks_position('none')
    #ax.yaxis.set_ticks_position('none')

    # Now make them go 'out' rather than 'in'
    for axis in ['x', 'y']:
        ax.tick_params(axis=axis, which='both', direction='out', pad=7)
        ax.tick_params(axis=axis, which='major', color=almost_black, length=6)
        ax.tick_params(axis=axis, which='minor', color=more_grey, length=4)

    # Make thinner and off-black
    spines_to_keep = ['bottom', 'left']
    for spine in spines_to_keep:
        ax.spines[spine].set_linewidth(0.5)
        ax.spines[spine].set_color(almost_black)

    # Change the labels & title to the off-black and change their font
    for label in [ax.yaxis.label, ax.xaxis.label, ax.title]:
        label.set_color(almost_black)
        label.set_family(text_font)

    # Change the tick labels' color and font and padding
    for axis in [ax.yaxis, ax.xaxis]:
        # padding
        #axis.labelpad = 20
        # major ticks
        for major_tick in axis.get_major_ticks():
            label = major_tick.label
            label.set_color(almost_black)
            label.set_family(number_font)
        # minor ticks
        for minor_tick in axis.get_minor_ticks():
            label = minor_tick.label
            label.set_color(more_grey)
            label.set_family(number_font)

    # Turn on grid lines for y-only
    plt.grid(axis='y', color=more_grey)
