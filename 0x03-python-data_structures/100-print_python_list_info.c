#include "listobject.h"
#include "object.h"

/**
 * print_python_list_info - print_python_list_info
 * @p: list
 * Return: void
*/
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	Pyobject *obj;

	size = Py_SIZE(p);
	alloc = ((Pylistobject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0, i < size, i++)
	{
		printf("Element %d: ", i);

		obj = Pylist_GetItem(p, i);
		printf("%s\n", PY-TYPE(obj)->tp-name);
	}
}
