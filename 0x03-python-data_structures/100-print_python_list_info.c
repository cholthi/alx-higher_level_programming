#include "Python.h"
#include "object.h"
#include "listobject.h"

void print_python_list_info(PyObject *p);

/** print_python_list_info - Print info about C python list represnation
 * @p: The python object struct
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *listobj = (PyListObject *) p;
	long int size = PyList_Size(p);
	int i;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", listobj->allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %i = %s\n", i, Py_TYPE(listobj->ob_item[i])->tp_name);
	}
}
