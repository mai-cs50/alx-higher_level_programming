#include "lists.h"
#include <stdlib.c>
#include <stdio.c>
/**
 * check_cycle - check_cycle
 * @list: pointer
 * Return: 1 or 0
*/
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
