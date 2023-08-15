#!include "Python.h"
#!include "listobject.h"
#!include "object.h"

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

	print("[*] Size of the Python List = %li\n", size);
	print("[*] Allocated = %li\n", listobj->allocated);
	for (i = 0; i < size; i++)
	{
		print("Element %i = %s\n", i, Py_TYPE(listobj->ob_item[i])->tp_name);
	}
}
