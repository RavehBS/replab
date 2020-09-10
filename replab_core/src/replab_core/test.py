#!/usr/bin/env python

import rospy
import numpy as np
import matplotlib.pyplot as plt
from controller import WidowX


def main():   	
	a = np.array((1,1) (2,2))
	b = ([3,3])
	x, _, _, _ = np.linalg.lstsq(a, b, rcond=None)


if __name__ == '__main__':
    main()
