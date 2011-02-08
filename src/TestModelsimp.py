#!/usr/bin/env python

from modelsimp import *
from matlab import *
import numpy as np
import unittest

class TestModelsimp(unittest.TestCase):
    def testHSVD(self):
        A = np.matrix("1. -2.; 3. -4.")
        B = np.matrix("5.; 7.")
        C = np.matrix("6. 8.")
        D = np.matrix("9.")
        sys = ss(A,B,C,D)
        hsv = hsvd(sys)
        hsvtrue = np.matrix("24.42686 0.5731395")
        np.testing.assert_array_almost_equal(hsv, hsvtrue)

    def testMarkov(self):
        U = np.matrix("1.; 1.; 1.; 1.; 1.")
        Y = U
        M = 3
        H = markov(Y,U,M)
        Htrue = np.matrix("1.; 0.; 0.")
        np.testing.assert_array_almost_equal( H, Htrue )

    def testModredMatchDC(self):
        #balanced realization computed in matlab for the transfer function:
        # num = [1 11 45 32], den = [1 15 60 200 60]
        A = np.matrix('-1.958, -1.194, 1.824, -1.464; \
        -1.194, -0.8344, 2.563, -1.351; \
        -1.824, -2.563, -1.124, 2.704; \
        -1.464, -1.351, -2.704, -11.08')
        B = np.matrix('-0.9057; -0.4068; -0.3263; -0.3474')
        C = np.matrix('-0.9057, -0.4068, 0.3263, -0.3474')
        D = np.matrix('0.')
        sys = ss(A,B,C,D)
        rsys = modred(sys,np.matrix('3, 4'),'matchdc')
        Artrue = np.matrix('-4.431, -4.552; -4.552, -5.361')
        Brtrue = np.matrix('-1.362; -1.031')
        Crtrue = np.matrix('-1.362, -1.031')
        Drtrue = np.matrix('-0.08384')
        np.testing.assert_array_almost_equal(sys.A, Artrue)
        np.testing.assert_array_almost_equal(sys.B, Brtrue)
        np.testing.assert_array_almost_equal(sys.C, Crtrue)
        np.testing.assert_array_almost_equal(sys.D, Drtrue)

    def testModredTruncate(self):
        #balanced realization computed in matlab for the transfer function:
        # num = [1 11 45 32], den = [1 15 60 200 60]
        A = np.matrix('-1.958, -1.194, 1.824, -1.464; \
        -1.194, -0.8344, 2.563, -1.351; \
        -1.824, -2.563, -1.124, 2.704; \
        -1.464, -1.351, -2.704, -11.08')
        B = np.matrix('-0.9057; -0.4068; -0.3263; -0.3474')
        C = np.matrix('-0.9057, -0.4068, 0.3263, -0.3474')
        D = np.matrix('0.')
        sys = ss(A,B,C,D)
        rsys = modred(sys,np.matrix('3, 4'),'truncate')
        Artrue = np.matrix('-1.958, -1.194; -1.194, -0.8344')
        Brtrue = np.matrix('-0.9057, -0.4068')
        Crtrue = np.matrix('-0.9057, -0.4068')
        Drtrue = np.matrix('0.')
        np.testing.assert_array_almost_equal(sys.A, Artrue)
        np.testing.assert_array_almost_equal(sys.B, Brtrue)
        np.testing.assert_array_almost_equal(sys.C, Crtrue)
        np.testing.assert_array_almost_equal(sys.D, Drtrue)

    def testBalredMatchDC(self):
        #controlable canonical realization computed in matlab for the transfer function:
        # num = [1 11 45 32], den = [1 15 60 200 60]
        A = np.matrix('-15., -7.5, -6.25, -1.875; \
        8., 0., 0., 0.; \
        0., 4., 0., 0.; \
        0., 0., 1., 0.')
        B = np.matrix('2.; 0.; 0.; 0.')
        C = np.matrix('0.5, 0.6875, 0.7031, 0.5')
        D = np.matrix('0.')
        sys = ss(A,B,C,D)
        orders = 1
        rsys = balred(sys,orders,'elimination','matchdc')
        Artrue = np.matrix('-0.566')
        Brtrue = np.matrix('-0.414')
        Crtrue = np.matrix('-0.5728')
        Drtrue = np.matrix('0.1145')
        np.testing.assert_array_almost_equal(sys.A, Artrue)
        np.testing.assert_array_almost_equal(sys.B, Brtrue)
        np.testing.assert_array_almost_equal(sys.C, Crtrue)
        np.testing.assert_array_almost_equal(sys.D, Drtrue)

    def testBalredTruncate(self):
        #controlable canonical realization computed in matlab for the transfer function:
        # num = [1 11 45 32], den = [1 15 60 200 60]
        A = np.matrix('-15., -7.5, -6.25, -1.875; \
        8., 0., 0., 0.; \
        0., 4., 0., 0.; \
        0., 0., 1., 0.')
        B = np.matrix('2.; 0.; 0.; 0.')
        C = np.matrix('0.5, 0.6875, 0.7031, 0.5')
        D = np.matrix('0.')
        sys = ss(A,B,C,D)
        orders = 2
        rsys = balred(sys,orders,'elimination','truncate')
        Artrue = np.matrix('-1.95, 0.6203; 2.314, -0.8432')
        Brtrue = np.matrix('0.7221; -0.6306')
        Crtrue = np.matrix('1.132, -0.2667')
        Drtrue = np.matrix('0.')
        np.testing.assert_array_almost_equal(sys.A, Artrue)
        np.testing.assert_array_almost_equal(sys.B, Brtrue)
        np.testing.assert_array_almost_equal(sys.C, Crtrue)
        np.testing.assert_array_almost_equal(sys.D, Drtrue)



if __name__ == '__main__':
    unittest.main()
