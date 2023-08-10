#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Insert node into a sorted singly linked list
 * @head: Head of the linked list
 * @number: element to insert
 *
 * Return: listint_t *new - New node inserted
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *prev = NULL;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current != NULL && current->n < number)
		{
			prev = current;
			current = current->next;
		}

		if (prev == NULL;)
			new->next = current;
		else
		{
			new->next = current;
			prev->next = new;
		}
	}

	return (new);
}

