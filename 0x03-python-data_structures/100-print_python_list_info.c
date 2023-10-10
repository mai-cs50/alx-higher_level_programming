#include <Python.h>
/**
 *
 *
 *
 *
 *
*/
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	pyobject *obj;

	size = py_SIZE(p);
	alloc = ((pylistobject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0, i < size, i++)
	{
		printf("Element %d: ", i);

		obj = pylist_GetItem(p, i);
		printf("%s\n", PY-TYPE(obj)->tp-name);
	}
}
