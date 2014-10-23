#include "ben.h"

BOOST_PYTHON_MODULE(ben) {
  np::initialize();
  SetupEigenConverters();
}
