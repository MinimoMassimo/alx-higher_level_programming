#include "lists.h"
/*#include <Python.h>*/

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list - the list to be checked
 * Return: 0 if there is no cycle, 1 otherwise
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *temp1 = NULL;

	temp1 = list;

	while (list)
	{
		temp1 = temp1->next;
		if (!list || !temp1)
			return (0);
		if (temp1 == list)
			return (1);
	}
	return (0);
}
