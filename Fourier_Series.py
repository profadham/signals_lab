# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from sympy import fourier_series, pi, plot
from sympy.abc import x
f = x**2
s = fourier_series(f,(x,-pi,pi))
s1 = s.truncate(n=3)
s2 = s.truncate(n=5)
s3 = s.truncate(n=10)
p = plot(f,s1,s2,s3,(x,-pi,pi),ylim=None,show=False,legend=True,title="lab task")

p[0].line_color = (0, 0, 0)
p[0].label = 'f'
p[1].line_color = (0, 1, 0)
p[1].label = 'n=3'
p[2].line_color = (1, 0, 0)
p[2].label = 'n=5'
p[3].line_color = (0, 0, 1)
p[3].label = 'n=710'

p.show()
