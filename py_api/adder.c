// Python.h содержит все необходимые функции, для работы с объектами Python
#include <Python.h>

// Эту функцию мы вызываем из Python кода
static PyObject* addList_add(PyObject* self, PyObject* args){

  PyObject * listObj;

  // Входящие аргументы - listObj
  if (! PyArg_ParseTuple( args, "O", &listObj))
    return NULL;

  long length = PyList_Size(listObj);

  // Проходимся по всем элементам
  long i, sum =0;
  for(i = 0; i < length; i++){
    PyObject* temp = PyList_GetItem(listObj, i);
    long elem = PyLong_AsLong(temp);
    sum += elem;
  }

  return Py_BuildValue("i", sum);
}

// Немного документации для `add`
static char addList_docs[] =
    "add( ): add all elements of the list\n";

/*
Эта таблица содержит необходимую информацию о функциях модуля
<имя функции в модуле Python>, <фактическая функция>,
<ожидаемые типы аргументов функции>, <документация функции>
*/
static PyMethodDef addList_funcs[] = {
    {"add", (PyCFunction)addList_add, METH_VARARGS, addList_docs},
    {NULL, NULL, 0, NULL}
};


PyMODINIT_FUNC initaddList(void){
    Py_InitModule3("addList", addList_funcs, "Add all ze lists");
}
