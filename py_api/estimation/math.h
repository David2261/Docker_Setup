#ifndef MATH_H_
#define MATH_H_
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#if PY_MAJOR_VERSION >= 3

int normal_distribution(int, int);


#endif

#endif // MATH_H_