#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, const int n)
{
	listint_t *temp = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = NULL;
	if (*head == NULL)
		*head = new;
	else
	{
		while (temp->next && temp->next->n < n)
			temp = temp->next;
		new->next = temp->next;
		temp->next = new;
	}
	return (new);
}
