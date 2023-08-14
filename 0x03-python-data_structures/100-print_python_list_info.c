#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	PyTypeObject *type = Py_TYPE(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated Memory = %ld\n", allocated);
	printf("[*] Element Type = %s\n", type->tp_name);
}
