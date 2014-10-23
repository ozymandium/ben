#ifndef _EIGEN_NUMPY_H_
#define _EIGEN_NUMPY_H_

#include <Eigen/Eigen>
#include <boost/numpy.hpp>
#include <glog/logging.h>
#include <numpy/arrayobject.h>
#include <numpy/ndarraytypes.h>


namespace bp = boost::python;
namespace np = boost::numpy;

using namespace Eigen;

void SetupEigenConverters();

#endif
