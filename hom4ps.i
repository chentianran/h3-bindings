%module hom4ps
%{
#include <hom4ps/hom4ps.hh>
%}

%include "typemaps.i"
%include "std_string.i"
%include "std_complex.i"
%include "std_vector.i"

namespace std
{
  %template(StringVector) vector<string>;
  %template(DoubleVector) vector<double>;
  %template(CplxDoubleVector) vector< std::complex<double> >;
}

%include "hom4ps.hh"

