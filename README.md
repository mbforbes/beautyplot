#beautyplot

A single function call to make `matplotlib.pyplot` plots look better. Because neither prettyplotlib nor matplotlibrc worked for me.

<table>
	<tr>
		<td><img alt="without" src="without.png"></td>
		<td><img alt="with" src="with.png"></td>
	</tr>
</table>

## Setup
Add `beautyplot.py` to your `PYTHONPATH` so that Python can find it.
`source setup.sh`

## Usage
```python
import matplotlib.pyplot as plt
from beautyplot import beautify

# Build your plot
plt.figure()
plt.title('Plot title')
plt.errorbar(xs, ys, yerr=stds, ...)
#...

# Here's the function call
beautify()

# Then take a look
plt.show()
```

## Features
### General
- set all things that were black (axis lines, labels, title, major tick labels, major ticks marks) to be off-black (a dark grey)

### Axes
- remove the top and right axis lines ('spines')
- make remaining axis lines thinner
- make dotted grid for major y lines

### Ticks
- turn off only right and top ticks
- set tick direction to be out (pointing out of graph)
- set all minor ticks labels and marks to be a lighter grey
 - make major and minor ticks longer
- make tick numbers farther away (padded) to accomodate longer ticks

### Fonts
- set all fonts to be serif (like Times New Roman)

## Things you need to do on your own
A lot of things that you need to do to make your graph look good (or that you need to do to make this function work) aren't generalizable enough to put here.

What I have now might also be too specific (I'm only plotting `errorbar` graphs currently).

I may in the future do some digging to detect more information about the 

0. Make sure major and minor ticks are specified correctly. Check out:
   - [example](http://matplotlib.org/examples/pylab_examples/major_minor_demo1.html)
   - [api](http://matplotlib.org/api/ticker_api.html)

0. Set plotting color. Use better colors than 'blue'. Check out:
   - [example](http://wiki.scipy.org/Cookbook/Matplotlib/Show_colormaps)
   - [example](http://colorbrewer2.org/)

0. Set plotting style. Lines should be very differentiable, with lots of visual redundancy. This means the following should be different:
   - markers [e.g. circles, triangles, 'x's, ...]
   - color (see above)
   - and style [e.g. dashed, dotted, line, variations in-between]

0. Set error bar width and cap sizes. Error bars should be thinner than plotting lines. Check out:
   - [example](http://stackoverflow.com/questions/7601334/how-to-set-the-line-width-of-error-bar-caps-in-matplotlib)
 