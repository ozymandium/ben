# Tests from ndarray lib
import test_ben
import unittest
import numpy


class TestEigenWrappers(unittest.TestCase):

    def setUp(self):
        self.matrix_i = numpy.matrix([[1,2,3],[4,5,6]], dtype=int)
        self.matrix_d = numpy.matrix([[1,2,3],[4,5,6]], dtype=float)
        self.vector_i = numpy.array([1,2,3,4], dtype=int)
        self.vector_d = numpy.array([1,2,3,4], dtype=float)

    def testAcceptMatrix(self):
        self.assert_(test_ben.acceptMatrix_23d_cref(self.matrix_d))
        self.assert_(test_ben.acceptMatrix_X3d_cref(self.matrix_d))
        self.assert_(test_ben.acceptMatrix_2Xd_cref(self.matrix_d))
        self.assert_(test_ben.acceptMatrix_XXd_cref(self.matrix_d))

    def testAcceptVector(self):
        self.assert_(test_ben.acceptVector_41d_cref(self.vector_d))
        self.assert_(test_ben.acceptVector_X1d_cref(self.vector_d))
        self.assert_(test_ben.acceptVector_14d_cref(self.vector_d))
        self.assert_(test_ben.acceptVector_1Xd_cref(self.vector_d))

    def testReturnMatrix(self):
        self.assert_((test_ben.returnMatrix_23d() == self.matrix_d).all())
        self.assert_((test_ben.returnMatrix_X3d() == self.matrix_d).all())
        self.assert_((test_ben.returnMatrix_2Xd() == self.matrix_d).all())
        self.assert_((test_ben.returnMatrix_XXd() == self.matrix_d).all())
        self.assert_((test_ben.returnMatrix_23d_c() == self.matrix_d).all())
        self.assert_((test_ben.returnMatrix_X3d_c() == self.matrix_d).all())
        self.assert_((test_ben.returnMatrix_2Xd_c() == self.matrix_d).all())
        self.assert_((test_ben.returnMatrix_XXd_c() == self.matrix_d).all())

    def testReturnObject(self):
        self.assert_((test_ben.returnObject_23d() == self.matrix_d).all())
        self.assert_((test_ben.returnObject_X3d() == self.matrix_d).all())
        self.assert_((test_ben.returnObject_2Xd() == self.matrix_d).all())
        self.assert_((test_ben.returnObject_XXd() == self.matrix_d).all())

if __name__=="__main__":
    unittest.main()
