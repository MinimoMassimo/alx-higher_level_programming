#include <stdlib.h>
#include <stdio.h>
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
	int len = 1, temp_len = 0;
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
	
	temp_len = len - 1;
	if (len % 2 == 0)
		len /= 2;
	else
		len = (len -1) / 2;
	for (; len > 0; len--)
	{
		
		for (i = 0; temp->next && i < temp_len; i++)
			temp = temp->next;
		
		printf("main:%d ", main->n);
		printf("temp:%d ", temp->n);
		
		if (main->n != temp->n)
			return (0);
		
		if (main->next)
		       main = main->next;
		temp = *head;
		temp_len--;
	}

	return (1);
}
