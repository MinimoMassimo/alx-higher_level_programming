#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if list is a palindrome
 * @head: pointer to pointer to head
 *
 * Return: 0 if not palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *main;
	int len = 1;
	int i = 0;

	if (head == NULL || *head == NULL)
		return 1;
	temp = *head;
	main = *head;
	while (temp->next)
	{
		temp = temp->next;
		len++;
	}
	for (; len > 0; len--)
	{
		if (main->n != temp->n)
			return (0);
		if (main)
		       main = main->next;
		temp = *head;
		for (i = 0; temp && i < len; i++)
			temp = temp->next;
	}	
	return (1);
}
