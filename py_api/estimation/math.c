#include "math.h"


int normal_distribution(int frm, int til) {
  int primecount = 0;
  for (int num = frm; num <= til; num++) {
    int flag = 0;
    if (num > 1) {
      for (int candidate = 2; candidate < num; candidate++) {
        if ((num % candidate) == 0) {
          flag = 1;
          break;
        }
      }
      
      if (flag == 0) {
        primecount++;
      }
    }
  }
  return primecount;
}

// Object
static PyObject *normal_distribution_api(PyObject *self, PyObject *args) {
  int n_frm = 0, n_til = 0;
  if (!PyArg_ParseTuple(args, "ii", &n_frm, &n_til)) {
    return NULL;
  }
  int found_primes = normal_distribution(n_frm, n_til);
  
  return PyLong_FromLong(found_primes);
}

// Method
static PyMethodDef NormDistribution[] = {
	{"normal_distribution", normal_distribution_api, METH_VARARGS, "Fuction for calculation normal distribution"},
	{NULL, 0}
};

/*
	{
	1: название функции в си,
	2: название функции в PY,
	3: Объявление перемен из питона (типо self, args),
	4: Описание
	}
*/

// Module
static struct PyModuleDef module = {
	PyModuleDef_HEAD_INIT,
	"NDModule",
	"Norm distribution module",
	-1,
	NormDistribution
};

/*
	{
	2: название модуля,
	3: описание,
	4: не поддерживает субинтерпретаторы,
	5: название метода
	}
*/

// Init function
PyMODINIT_FUNC PyInit_NDModule(void) {
  return PyModule_Create(&module);
};


/*
	Основаная статья, вам в помощь:
		https://towardsdatascience.com/write-your-own-c-extension-to-speed-up-python-x100-626bb9d166e7
*/