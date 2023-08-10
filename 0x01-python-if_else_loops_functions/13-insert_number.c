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

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || (*head->n) >= new->n)
	{
		new->next = head
		*head = new;
	}
	else
	{
		while (current->next != NULL && current->next->n < new->n)
		{
			current = current->next;
		}

		new->next = current->next;
		current->next = new;
	}

	return (new);
}

